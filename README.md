# ROS DIF

Bộ khung ROS 2 Humble và Gazebo Fortress cho robot vi sai hai bánh chủ động dùng LiDAR 2D. Mã nguồn cũ Mecanum/pallet đã được loại bỏ khỏi workspace này.

## Phạm vi ban đầu

- Mô hình hình học đơn giản: hai bánh chủ động và hai bánh đỡ thụ động dạng cầu ma sát thấp.
- Plugin DiffDrive của Gazebo điều khiển hai khớp bánh; odometry từ chuyển động bánh trong mô phỏng.
- LiDAR 360 độ, 720 mẫu, 10 Hz; phòng 6 × 6 m với một vật cản.
- Bridge `/clock`, `/cmd_vel`, `/odom`, `/tf`, `/joint_states`, `/scan` và cấu hình RViz.
- Chưa tích hợp SLAM, Nav2, nhiệm vụ phục vụ bàn hoặc driver phần cứng.

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

Kiểm tra chuyển động và dữ liệu LiDAR trước, sau đó thêm SLAM, lưu bản đồ, định vị/Nav2 và giao tiếp phần cứng. Tham khảo cấu hình plugin từ [Gazebo DiffDrive](https://gazebosim.org/api/gazebo/6/classignition_1_1gazebo_1_1systems_1_1DiffDrive.html) và [Gazebo Sensors](https://gazebosim.org/docs/fortress/sensors/).
