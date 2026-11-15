# ROS DIF

Bộ khung ROS 2 Humble và Gazebo Fortress cho robot vi sai hai bánh chủ động dùng LiDAR 2D. Mã nguồn cũ Mecanum/pallet đã được loại bỏ khỏi workspace này.

## Phạm vi ban đầu

- Mô hình hình học đơn giản: hai bánh chủ động và hai bánh đỡ thụ động dạng cầu ma sát thấp.
- Plugin DiffDrive của Gazebo điều khiển hai khớp bánh; odometry từ chuyển động bánh trong mô phỏng.
- LiDAR 360 độ, 720 mẫu, 10 Hz; phòng 6 × 6 m với một vật cản.
- Bridge `/clock`, `/cmd_vel`, `/odom`, `/tf`, `/joint_states`, `/scan` và cấu hình RViz.
- SLAM Toolbox tạo bản đồ từ LiDAR; chưa tích hợp điều hướng Nav2, nhiệm vụ phục vụ bàn hoặc driver phần cứng.

Kích thước, khối lượng và thông số cảm biến là giá trị khởi tạo, chưa được hiệu chỉnh theo robot thực. Sửa tại `src/dif_description/urdf/dif.urdf.xacro` và `gazebo.xacro`.

## Cấu trúc

```text
src/
├── dif_description/   # URDF/Xacro, quán tính và RViz
├── dif_gazebo/        # World và cấu hình bridge
└── dif_bringup/       # Launch mô phỏng và xem mô hình
```

## Môi trường

Mở workspace trong VS Code và chọn **Dev Containers: Rebuild and Reopen in Container**. Container cài ROS 2 Humble, ros_gz/Fortress và phụ thuộc từ `package.xml`. Không cần cài ROS trực tiếp trên máy host.

Terminal dùng Oh My Bash với theme `robbyrussell` và ble.sh để gợi ý lệnh, tô màu cú pháp. History được nạp sẵn từ `.devcontainer/history_seed.txt` khi chưa có lịch sử, sau đó lưu trong volume riêng `ros-dif-commandhistory` để giữ qua các lần rebuild. Các terminal ghi/đọc history mỗi khi hiện prompt; chạy lại setup không ghi đè lịch sử đã có. Lần tạo container đầu tiên cần mạng để tải Oh My Bash và bản ble.sh nightly.

Cấu hình GUI dùng X11 qua `DISPLAY` và `/tmp/.X11-unix`, mặc định render phần mềm để không phụ thuộc NVIDIA Container Toolkit. Nếu X server từ chối kết nối, trên host cho phép user hiện tại bằng `xhost +si:localuser:$(id -un)`. Để dùng NVIDIA, cấu hình NVIDIA Container Toolkit trên host, thêm `--gpus=all` trong `runArgs`, bỏ `LIBGL_ALWAYS_SOFTWARE` và thêm các biến NVIDIA phù hợp. LiDAR GPU vẫn cần môi trường OpenGL ngay cả khi tắt cửa sổ Gazebo.

Nếu dùng Ubuntu 22.04 với ROS Humble đã cài trực tiếp:

```bash
source /opt/ros/humble/setup.bash
rosdep update --rosdistro humble
rosdep install --from-paths src --ignore-src --rosdistro humble -r -y
```

## Build và chạy

Trong container hoặc môi trường ROS đã cài đủ phụ thuộc:

```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install --base-paths src
source install/setup.bash
ros2 launch dif_bringup sim.launch.py
```

Launch luôn dùng thời gian mô phỏng. Tùy chọn `rviz:=false` tắt RViz; `gui:=false` chỉ chạy Gazebo server. Khi đổi world qua `world:=/duong/dan/world.sdf`, world phải có tên `default` và nạp các plugin physics, user commands, sensors.

Chỉ xem mô hình, không chạy Gazebo:

```bash
ros2 launch dif_bringup display.launch.py
```

Trong terminal khác đã source ROS và workspace:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Dùng `i` để tiến, `,` để lùi, `j`/`l` để quay và `k` để dừng. Teleop chuẩn phát lệnh theo phím bấm; nhấn `k` để dừng trước khi rời terminal. Bản khởi tạo dùng trực tiếp plugin DiffDrive, chưa có watchdog độc lập khi node phát lệnh bị ngắt đột ngột.

## Joystick OpenTX Jumper T20

Chạy task **ROS DIF: joystick teleop** cùng một launch mô phỏng hoặc SLAM.
Dừng keyboard teleop trước khi dùng joystick. Cấu hình chỉ số trong
`src/dif_bringup/config/joy.yaml`:

- `axis 1`: tiến/lùi; `axis 0`: quay.
- Không dùng axis 2 và không cần btn; `require_enable_button: false`.
- Tối đa 0.25 m/s và 0.5 rad/s, tỷ lệ với độ lệch cần. Đưa axis 0 và axis 1 về giữa để dừng.
- Dùng trực tiếp `teleop_twist_joy`; không có timeout mất `/joy` trong cấu hình này.

Các chỉ số/dấu cần đối chiếu với `ros2 topic echo /joy` vì SDL có thể khác `jstest-gtk`.

Dev container bind-mount toàn bộ `/dev/input`, cho phép thiết bị input (major 13)
qua cgroup và đọc metadata `/run/udev` để nhận thiết bị khi rút/cắm lại. Thêm
GID 104 (nhóm `input` trên host hiện tại). Chọn
**Dev Containers: Rebuild Container** để áp dụng cấu hình; thay đổi này không áp dụng bằng cách
chỉ mở lại terminal. Nếu đổi host, kiểm tra GID bằng `stat -Lc '%g'` trên thiết bị
và cập nhật `--group-add` trong `.devcontainer/devcontainer.json`.
Sau khi rút/cắm lại, kiểm tra `ros2 run joy joy_enumerate_devices` và chạy lại task joystick
nếu driver chưa nhận lại. Không cần tạo lại container chỉ vì device node đổi.
Nếu ID joystick đổi sau khi cắm lại, dùng `device_id:=N` trong launch theo kết quả
của `joy_enumerate_devices`.

Trong container sau khi tạo lại:

```bash
colcon build --symlink-install --packages-select dif_bringup
source install/setup.bash
ros2 run joy joy_enumerate_devices
ros2 launch dif_bringup joy.launch.py
```

Terminal khác:

```bash
ros2 topic echo /joy
ros2 topic echo /cmd_vel
```

Để thử bộ chuyển đổi mà không điều khiển robot, chạy
`ros2 launch dif_bringup joy.launch.py start_joy:=false cmd_vel:=/cmd_vel_test`.
Phát Joy giả `[axis 0, axis 1] = [0.0, 1.0]`, `buttons: []` sẽ cho tốc độ tiến 0.25 m/s;
đưa cả hai axis về 0 sẽ dừng.

## Kiểm tra sau khi khởi chạy

```bash
ros2 topic hz /scan
ros2 topic echo /scan --once --field header
ros2 topic echo /odom --once
ros2 run tf2_ros tf2_echo odom laser_frame
```

Trong RViz, chọn fixed frame `odom`. LiDAR phải có `frame_id: laser_frame`, quét thấy tường/vật cản và gắn đúng vị trí trên thân robot. TF mong đợi:

```text
odom → base_footprint → base_link → laser_frame
                              ├→ left_wheel_link
                              ├→ right_wheel_link
                              ├→ front_caster_link
                              └→ rear_caster_link
```

Gazebo phát `odom → base_footprint` và joint states; `robot_state_publisher` phát các biến đổi bên trong robot. Không chạy thêm `joint_state_publisher_gui` cùng launch mô phỏng.

## Tạo bản đồ bằng SLAM

Với container đã tạo trước khi thêm SLAM, cài gói trong terminal container (không cần rebuild container):

```bash
sudo apt-get update
sudo apt-get install -y ros-humble-slam-toolbox ros-humble-nav2-map-server
colcon build --symlink-install --base-paths src
source install/setup.bash
```

Dừng launch mô phỏng/display cũ trước, rồi chạy lệnh dưới hoặc task **ROS DIF: SLAM mapping**.
Launch này đã bao gồm Gazebo, RViz và SLAM; không chạy thêm `sim.launch.py` song song.

```bash
ros2 launch dif_bringup slam.launch.py
```

Trong terminal khác, chạy teleop, giảm tốc độ bằng `z` và đưa robot đi chậm quanh phòng.
Quan sát Map trong RViz (Fixed Frame `map`), đi qua các khu vực chưa quét và quay lại vị trí ban đầu.
Nhấn `k` để dừng. Bản đồ cập nhật mỗi 2 giây theo thời gian mô phỏng.
SLAM phát TF `map → odom`, nối vào cây TF đã có.

Launch SLAM nạp `src/dif_description/rviz/slam.rviz` (Fixed Frame và camera Target Frame là `map`).
Launch mô phỏng thường nạp `dif.rviz` (frame `odom`); launch xem mô hình nạp `display.rviz` (frame `base_footprint`).
Trong Gazebo Fortress, để ẩn bảng bên phải, nhấp phải vào từng plugin **Component Inspector** và **Entity Tree**, chọn **Close**.
Mở lại các plugin qua nút ba chấm góc trên phải. Tham khảo [giao diện Fortress](https://gazebosim.org/docs/fortress/gui/).
Chọn **Save client configuration** trong menu góc trên trái để lưu vào
`~/.ignition/gazebo/6/gui.config` bên trong container. Muốn giữ qua lần tạo lại container,
chọn **Save client configuration as** và lưu thành
`/workspaces/ros-dif/src/dif_gazebo/config/gui.config`, sau đó chạy:

```bash
ros2 launch dif_bringup slam.launch.py gui_config:="$(pwd)/src/dif_gazebo/config/gui.config"
```

`sim.launch.py` cũng nhận `gui_config:=/duong/dan/gui.config`.
Để trống tham số sẽ dùng cấu hình mặc định của Gazebo; `gui:=false` bỏ qua GUI config.

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Khi bản đồ rõ tường và vật cản, giữ SLAM đang chạy và lưu từ terminal khác tại thư mục workspace:

```bash
mkdir -p maps
ros2 run nav2_map_server map_saver_cli -f maps/room --ros-args -p use_sim_time:=true -p map_subscribe_transient_local:=true
```

Kết quả là `maps/room.yaml` và ảnh bản đồ `maps/room.pgm`, dùng cho định vị/Nav2 sau này.
Đây là bản đồ occupancy để điều hướng; không chứa pose graph để tiếp tục phiên SLAM.
Kiểm tra dữ liệu nếu chưa thấy bản đồ:

```bash
ros2 topic hz /scan
ros2 topic echo /map --once --field info
ros2 run tf2_ros tf2_echo map base_footprint
```

Cấu hình tại `src/dif_bringup/config/slam.yaml`, dựa trên
[launch Humble của SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox/blob/humble/launch/online_async_launch.py).
Ngưỡng góc quay là 0.1 rad. Ngưỡng tịnh tiến đặt 0.0 m vì bộ lọc scan bên ngoài của
SLAM Toolbox Humble chỉ xét khoảng cách tịnh tiến; đặt khác 0 sẽ bỏ qua scan khi robot quay tại chỗ.

## Kiểm tra cấu trúc trước khi chạy

Trong môi trường có `xacro` và `python3-yaml`:

```bash
python3 -m unittest discover -s tests -v
```

Bộ kiểm tra xác nhận cây TF liên thông, quán tính hợp lệ, hình học hai bánh khớp cấu hình DiffDrive, frame LiDAR và các topic bridge. Các kiểm tra này không thay thế chạy thử Gazebo.

## Tài liệu và bước tiếp theo

- [Phân tích báo cáo tham khảo](docs/phan-tich-bao-cao.md).
- [Báo cáo gốc và tài nguyên](docs/README.md).
- [Lộ trình triển khai](docs/chuyen-doi-robot-vi-sai.md).

Kiểm tra chuyển động và dữ liệu LiDAR trước, sau đó chạy SLAM, lưu bản đồ, tích hợp định vị/Nav2 và giao tiếp phần cứng. Tham khảo cấu hình plugin từ [Gazebo DiffDrive](https://gazebosim.org/api/gazebo/6/classignition_1_1gazebo_1_1systems_1_1DiffDrive.html) và [Gazebo Sensors](https://gazebosim.org/docs/fortress/sensors/).
