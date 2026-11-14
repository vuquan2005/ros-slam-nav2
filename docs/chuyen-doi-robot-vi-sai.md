# Lộ trình robot vi sai dùng LiDAR

## Bộ khung hiện tại

Workspace có ba package mới: `dif_description`, `dif_gazebo`, `dif_bringup`. Mô hình dùng hình học cơ bản, hai bánh chủ động, hai bánh đỡ ma sát thấp, plugin DiffDrive và LiDAR 2D. Mã Mecanum/pallet cũ đã được bỏ khỏi dự án.

Đây là cấu hình ban đầu, chưa hiệu chỉnh kích thước thực và chưa tích hợp SLAM/Nav2/phần cứng. Xem [hướng dẫn chạy](../README.md).

## Các bước tiếp theo

1. Build trong môi trường Humble/Fortress, kiểm tra spawn và RViz.
2. Kiểm tra tiến/lùi, quay tại chỗ, odometry và TF từ `odom` đến `laser_frame`.
3. Kiểm tra `/scan`, thời gian mô phỏng và vật cản trong phòng thử.
4. Hiệu chỉnh kích thước, khối lượng, vị trí LiDAR và giới hạn vận tốc theo robot thực.
5. Thêm SLAM, lưu bản đồ rồi cấu hình định vị và Nav2 cho robot vi sai.
6. Thêm driver LiDAR thật, giao tiếp board động cơ, odometry encoder/IMU và watchdog độc lập.
7. Xây dựng nhiệm vụ đến bàn và quay về điểm xuất phát sau khi điều hướng đạt yêu cầu.

## Thông số cần đo

- Bán kính bánh trái/phải và khoảng cách giữa tâm hai bánh.
- Kích thước khung, khối lượng, vị trí trọng tâm và bánh đỡ.
- Model LiDAR, vị trí/hướng lắp, giao tiếp và tần số quét.
- Board động cơ, giao thức kết nối, độ phân giải encoder và tỉ số truyền.
- Giới hạn vận tốc/gia tốc, thời gian dừng khi mất lệnh và sai số odometry.

## Tiêu chí nghiệm thu ban đầu

- Robot tiến theo trục X, quay đúng chiều; không nhận điều khiển trượt ngang.
- Mỗi quan hệ TF có một nguồn phát; dấu thời gian đồng bộ với `/clock`.
- LiDAR quét thấy tường đúng vị trí, không lệch frame hoặc mất scan kéo dài.
- Đo và ghi lại sai số quãng đường, góc quay và độ ổn định trước khi cấu hình điều hướng.
