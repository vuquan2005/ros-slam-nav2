# Chuyển sang robot vi sai hai bánh dùng LiDAR

Đây là danh sách công việc chuẩn bị; mã nguồn hiện tại chưa được chuyển sang robot mới. Giữ các package cũ để đối chiếu trong quá trình thay từng phần.

## Những phần cần thay

| Thành phần | Hiện tại | Công việc cho robot mới |
| --- | --- | --- |
| Mô hình robot | 4 bánh Mecanum, càng nâng, camera | Hai bánh chủ động trái/phải, bánh đỡ, khung và `laser_frame` đúng kích thước thực |
| Điều khiển | `kinematics_node.py` xuất 4 vận tốc bánh | Điều khiển vi sai với bán kính bánh và khoảng cách hai bánh thực tế; không nhận chuyển động ngang |
| Gazebo | `PlanarVelocityControl` áp vận tốc trực tiếp lên thân | Thay bằng mô phỏng truyền động hai bánh; bỏ plugin toàn hướng để tránh hai nguồn điều khiển |
| Odometry | Ground truth từ Gazebo | Odometry từ truyền động khi mô phỏng và encoder khi chạy thật; một nguồn phát TF `odom` đến thân robot |
| LiDAR | Chưa có | Thêm mô hình cảm biến, `/scan` và bridge mô phỏng; driver theo model LiDAR khi chạy thật |
| Điều khiển tay | Có `linear.y` và nâng hàng | Chỉ dùng tiến/lùi và quay; bỏ các lệnh nâng nếu robot không có cơ cấu này |
| Dẫn đường | Dò line, tọa độ sa bàn và nhiệm vụ pallet | Thêm SLAM, lưu bản đồ, định vị và cấu hình Nav2 cho robot vi sai |
| Bringup | Launch mô phỏng và ứng dụng pallet | Tách launch mô phỏng/chạy thật; các tính năng pallet chỉ bật khi cần |

`robot0_navigation` hiện là nhiệm vụ pallet tự viết, chưa phải cấu hình Nav2 cho LiDAR. Các package vision, dò line và mesh cơ cấu nâng chỉ nên loại bỏ sau khi mô hình và launch mới không còn tham chiếu đến chúng.

## Thông số cần xác định trước khi cấu hình

- Bán kính bánh trái/phải, khoảng cách giữa tâm hai bánh, kích thước và khối lượng khung.
- Vị trí bánh đỡ và vị trí, hướng lắp LiDAR so với `base_link`.
- Model LiDAR, giao tiếp USB/serial/Ethernet và tên frame do driver phát.
- Board điều khiển động cơ, giao thức kết nối, độ phân giải encoder và tỉ số truyền.
- Giới hạn vận tốc, gia tốc và timeout dừng khi mất lệnh.
- Phiên bản ROS/Gazebo sẽ dùng; cấu hình cũ trong devcontainer là Humble/Fortress.

## Trình tự thực hiện

1. Tạo mô hình robot hai bánh và kiểm tra TF, chiều quay khớp, collision và quán tính.
2. Thay truyền động trong Gazebo, kiểm tra tiến/lùi, quay tại chỗ và dừng khi mất lệnh.
3. Thêm LiDAR và `/scan`; kiểm tra vật cản hiển thị đúng trong RViz.
4. Kiểm tra chuỗi TF từ `odom` qua thân robot đến `laser_frame`, thời gian mô phỏng và odometry.
5. Thêm SLAM, lưu bản đồ rồi cấu hình định vị và Nav2.
6. Kết nối phần cứng, hiệu chỉnh odometry và chỉ sau đó gỡ các tài nguyên cũ không còn sử dụng.
