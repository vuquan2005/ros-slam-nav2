# Phân tích báo cáo robot phục vụ lễ tân

Nguồn: [bản Markdown của báo cáo năm 2022](report-old/do-an-cdt.md), gồm cả các ảnh chụp và lưu đồ đính kèm. Phân tích này mô tả nội dung báo cáo; không khẳng định mọi chức năng đề xuất đã được thực hiện.

## Mục tiêu

Mục tiêu tổng thể là robot phục vụ nhà hàng: đến bàn, hiển thị menu, quay về bếp và vận chuyển đồ ăn. Phạm vi được giới hạn trong phòng thí nghiệm với robot vi sai, tương tác qua màn hình/nút nhấn và cảm biến phát hiện vật cản (chương 1).

Phần mô phỏng và tích hợp tập trung vào chuyển động robot vi sai, quét môi trường bằng LiDAR 2D trong Gazebo, hiển thị trên RViz, kiểm tra `/tf` và `/scan`, rồi hình thành bản đồ phục vụ định vị/điều hướng (mục 2.3 và 3.4). Phần thực nghiệm báo cáo kết quả quét bản đồ phòng và mô hình robot; không có bộ phép đo đầy đủ về độ chính xác định vị, tỷ lệ đến đích hay tránh vật cản.

## Kỹ thuật và mức độ bằng chứng

| Nội dung | Bằng chứng trong báo cáo | Nhận định |
| --- | --- | --- |
| Robot vi sai | Hai bánh chủ động, bánh tự lựa; chương 2 có động học thuận/nghịch và động lực học | Cơ cấu di chuyển chính; không có chuyển động ngang độc lập |
| ROS | Có `roscore`, `roslaunch`, `rostopic`, ROS Master, Navigation stack | Là ROS 1; báo cáo nhắc Noetic và Ubuntu 20.04 nhưng chưa đủ để xác nhận chính xác distro đã dùng ở mọi hình |
| Gazebo và RViz | Mô tả mô phỏng robot/cảm biến, kiểm tra TF và quét laser | Gazebo mô phỏng vật lý/cảm biến; RViz trực quan hóa dữ liệu |
| Driver LiDAR | Hình ngay trước hình 3.18 có `roslaunch rplidar_ros rplidar.launch` | Có sử dụng/tham khảo driver RPLIDAR; chưa đủ thông tin chốt model thiết bị |
| SLAM | Mục tổng quan nhắc `slam_gmapping`; terminal trong hình 3.18 hiển thị tham số `/hector_mapping/...` và Hector SLAM | Có bằng chứng ảnh cho Hector Mapping; chưa đủ để khẳng định Gmapping là thuật toán đã dùng trong thực nghiệm |
| TF | Mục 3.4 mô tả `base_link`, `base_laser` và TF broadcaster | Cần hiệu chỉnh phép biến đổi theo vị trí lắp LiDAR; độ lệch 0.1 m/0.2 m trong báo cáo là ví dụ |
| Cảm biến và odometry | LiDAR, IMU, encoder; `sensor_msgs/LaserScan`, `nav_msgs/Odometry` | LaserScan dùng cho LiDAR; IMU và encoder cần luồng xử lý riêng. Không có cấu hình đủ để khẳng định dùng EKF |
| Navigation | Mô tả map server, sensor sources, odometry, base controller và `geometry_msgs/Twist` trên `/cmd_vel` | Là kiến trúc Navigation ROS 1; chưa có cấu hình planner đầy đủ để tái lập hệ thống |
| Điều khiển tầng thấp | Raspberry Pi 4 xử lý phía ROS; STM32 điều khiển động cơ, encoder, IMU; Smart PID, UART/PWM | Báo cáo có chỗ ghi STM32F407, chỗ ghi STM32F1 nên chưa chốt firmware/board theo tài liệu này |
| Cơ khí | Bánh đường kính 150 mm, mục tiêu tốc độ tối đa 0.5 m/s, động cơ DC giảm tốc 24 V | Là thông số thiết kế tham khảo; chưa thay thế phép đo robot hiện tại |

Không thể kết luận AMCL, DWA hay một thuật toán tìm đường cụ thể đã được triển khai chỉ vì chúng xuất hiện trong tài liệu tham khảo. `map_server` cung cấp bản đồ, không tự thực hiện SLAM. Ảnh khởi chạy RPLIDAR/Hector là bằng chứng cho quét LiDAR qua ROS/RViz; riêng ảnh đó không chứng minh cảm biến đang được mô phỏng trong Gazebo.

## Kết quả và giới hạn

Chương 4 ghi nhận xây dựng mô hình robot, truyền dữ liệu IMU/encoder lên Raspberry Pi và vận tốc hai bánh về STM32, đồng thời lập được bản đồ phòng. Tác giả cũng nêu di chuyển chưa ổn định, có sai lệch/độ trễ và bản đồ còn nhiễu. Chưa đủ bằng chứng để coi toàn bộ chu trình đặt món, tự đi đến bàn, tránh vật cản và quay về bếp đã được kiểm chứng hoàn chỉnh.

## Áp dụng cho workspace mới

Giữ bài toán cốt lõi: robot vi sai → LiDAR và odometry → SLAM → bản đồ → định vị và điều hướng. Workspace mới dùng ROS 2 Humble/Fortress, vì vậy cần cấu hình ROS 2 tương ứng thay vì sao chép lệnh ROS 1 trong báo cáo. Bộ khung ban đầu mới cung cấp mô hình, truyền động mô phỏng, LiDAR, TF và bridge; SLAM/Nav2 được bổ sung sau khi dữ liệu đầu vào hoạt động đúng.
