![](assets/do-an-cdt/media/image1.jpeg)

> **BỘ CÔNG THƯƠNG**
>
> **TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP HÀ NỘI KHOA CƠ KHÍ**

ĐỒ ÁN MÔN HỌC CƠ ĐIỆN TỬ

> **NGHIÊN CỨU, THIẾT KẾ ROBOT PHỤC VỤ LỄ TÂN**
>
> Giáo viên hướng dẫn : TS. Nguyễn Văn Trường
>
> Sinh viên thực hiện : 1. Phạm Đức Huy – 2019600339

2.  Tạ Văn Mạnh – 2019600907

3.  Nguyễn Văn Nghĩa – 2019600434

> Hà Nội – 2022

<a id="mục-lục"></a>

# MỤC LỤC

[MỤC LỤC 2](#mục-lục)

[DANH MỤC HÌNH ẢNH 3](#danh-mục-hình-ảnh)

[DANH MỤC BẢNG BIỂU 5](#danh-mục-bảng-biểu)

[CHƯƠNG 1: TỔNG QUAN VỀ MOBILE ROBOT 6](#chương-1-tổng-quan-về-mobile-robot)

1.  [Lịch sử nghiên cứu 6](#lịch-sử-nghiên-cứu)

2.  [Mục tiêu của đề tài 7](#mục-tiêu-của-đề-tài)

3.  [Phương pháp nghiên cứu 8](#phương-pháp-nghiên-cứu)

4.  [Giới hạn, phạm vi nghiên cứu 10](#giới-hạn-phạm-vi-nghiên-cứu)

[CHƯƠNG 2: CƠ SỞ LÝ THUYẾT 11](#chương-2-cơ-sở-lý-thuyết)

1.  [Nguyên lý làm việc, chức năng của từng module trong hệ thống 11](#nguyên-lý-làm-việc-chức-năng-của-từng-module-trong-hệ-thống)

2.  [Hệ điều hành Ubuntu và mô phỏng mobile robot trên Gazebo 23](#hệ-điều-hành-ubuntu-và-mô-phỏng-mobile-robot-trên-gazebo)

3.  [Phương pháp quét bản đồ bằng Lidar trên Gazebo 26](#phương-pháp-quét-bản-đồ-bằng-lidar-trên-gazebo)

4.  [Tổng quan về ROS 27](#tổng-quan-về-ros.)

5.  [Xây dựng mô hình hệ thống 30](#xây-dựng-mô-hình-hệ-thống)

[CHƯƠNG 3: TÍNH TOÁN, THIẾT KẾ HỆ THỐNG 41](#chương-3-tính-toán-thiết-kế-hệ-thống)

1.  [Thiết kế sơ đồ tổng thể hệ thống 41](#thiết-kế-sơ-đồ-tổng-thể-hệ-thống)

2.  [Tính toán, thiết kế hệ thống cơ khí 42](#_bookmark37)

3.  [Tính toán, thiết kế hệ thống điều khiển 47](#tính-toán-thiết-kế-hệ-thống-điều-khiển)

4.  [Lập bản đồ sử dụng LiDAR 53](#lập-bản-đồ-sử-dụng-lidar)

[CHƯƠNG 4: KẾT LUẬN VÀ ĐỊNH HƯỚNG PHÁT TRIỂN 66](#chương-4-kết-luận-và-định-hướng-phát-triển)

1.  [Kết quả đạt được 66](#kết-quả-đạt-được)

2.  [Đánh giá và định hướng phát triển 67](#đánh-giá-và-định-hướng-phát-triển)

[PHỤ LỤC 69](#phụ-lục)

[TÀI LIỆU THAM KHẢO 86](#tài-liệu-tham-khảo)

<a id="danh-mục-hình-ảnh"></a>

# DANH MỤC HÌNH ẢNH

> [Hình 1.1: Robot Perseverance trên sao Hoả 7](#_bookmark5)
>
> [Hình 1.2: Robot hình người ASIMO 7](#_bookmark6)
>
> [Hình 1.3: Robot UAV VA–1000 7](#_bookmark7)
>
> [Hình 1.4: Robot phục vụ nhà hàng Pudu 8](#_bookmark10)
>
> [Hình 1.5: Robot CLOi ServeBot của hãng LG Electronic 9](#_bookmark11)
>
> [Hình 2.1: Sơ đồ cấu trúc hệ thống robot phục vụ lễ tân 12](#_bookmark15)
>
> [Hình 2.2: Cơ cấu vi sai 13](#_bookmark16)
>
> [Hình 2.3: Động cơ bước 22](#_bookmark19)
>
> [Hình 2.4: Động cơ DC servo 23](#_bookmark20)
>
> [Hình 2.5: Giao diện hệ điều hành Ubuntu 24](#_bookmark22)
>
> [Hình 2.6: Mô phỏng Mobile robot trên Gazebo 25](#_bookmark23)
>
> [Hình 2.7: Quét bản đồ từ LiDAR 2D 26](#_bookmark25)
>
> [Hình 2.8: Mô phỏng quét LiDAR trên Rviz 26](#_bookmark26)
>
> [Hình 2.9: ROS kết nối 27](#_bookmark28)
>
> [Hình 2.10: Thành phần của ROS 28](#_bookmark29)
>
> [Hình 2.11: Mô hình robot 30](#_bookmark31)
>
> [Hình 2.12: Mô hình robot và các thông số động học 31](#_bookmark32)
>
> [Hình 2.13: Mô hình robot và các thông số động lực học 35](#_bookmark33)
>
> [Hình 3.1: Sơ đồ khối hệ thống 41](#_bookmark36)
>
> [Hình 3.2: Bản vẽ thiết kế hệ thống cơ khí của mô hình 42](#_bookmark38)
>
> [Hình 3.3: Các thành phần cơ bản của mô hình cơ khí 43](#_bookmark39)
>
> [Hình 3.4: Bánh xe dẫn động 44](#_bookmark40)
>
> [Hình 3.5: Bánh xe dẫn hướng bị động 44](#_bookmark41)
>
> [Hình 3.6: Phân tích các lực tác dụng lên xe 45](#_bookmark42)
>
> [Hình 3.7: Động cơ giảm tốc planet 46](#_bookmark43)
>
> [Hình 3.8: Sơ đồ tổng thể hệ thống điều khiển 47](#_bookmark45)
>
> [Hình 3.9: Sơ đồ khối hệ thống điều khiển trung tâm 48](#_bookmark46)
>
> [Hình 3.10: MCU STM32F407 thiết kế trên phần mềm Altium Designer 49](#_bookmark47)
>
> [Hình 3.11: Board mạch vi điều khiển STM32F407VET6 49](#_bookmark48)
>
> [Hình 3.12: Giao diện phần mềm KeilC V5 50](#_bookmark49)
>
> [Hình 3.13: Drive Smart PID V4.0 51](#_bookmark50)
>
> [Hình 3.14: Module LM2596 52](#_bookmark51)
>
> [Hình 3.15: Động cơ giảm tốc planet 24V 53](#_bookmark52)
>
> [Hình 3.16: Giao diện Ubuntu 20.04 LTS Desktop 54](#_bookmark54)
>
> [Hình 3.17: Gazebo in ROS 55](#_bookmark55)
>
> [Hình 3.18: Mô phỏng quét bản đồ nhờ cảm biến LiDAR 55](#_bookmark56)
>
> [Hình 3.19: Kết quả kiểm tra dữ liệu /tf 56](#_bookmark57)
>
> [Hình 3.20: Kết quả kiểm tra dữ liệu /scan 56](#_bookmark58)
>
> [Hình 3.21: Quét bản đồ thực sau khi cài đặt hệ thống 57](#_bookmark59)
>
> [Hình 3.22: Lưu đồ sử dụng lidar lập bản đồ 57](#_bookmark60)
>
> [Hình 3.23: Lưu đồ sử dụng Lidar lập bản đồ và điều khiển động cơ 58](#_bookmark61)
>
> [Hình 3.24: Sơ đồ topic của bài toán navigation 58](#_bookmark62)
>
> [Hình 3.25: Ví dụ về khoảng cách giữa 2 khung tọa độ 59](#_bookmark63)
>
> [Hình 4.1: Mô hình thực tế 66](#_bookmark66)
>
> [Hình 4.2: Bản đồ quét được trên không gian thực tế 67](#_bookmark67)

<a id="danh-mục-bảng-biểu"></a>

# DANH MỤC BẢNG BIỂU

[Bảng 2.1: Bảng phân tích ưu điểm, nhược điểm của các loại vi điều khiển 15](#_bookmark17)

[Bảng 2.2: Bảng phân tích ưu, nhược điểm của các loại cảm biến phát hiện vật cản 18](#_bookmark18)

<a id="chương-1-tổng-quan-về-mobile-robot"></a>

# CHƯƠNG 1: TỔNG QUAN VỀ MOBILE ROBOT

<a id="lịch-sử-nghiên-cứu"></a>

## Lịch sử nghiên cứu

> Thuật ngữ “Robot” xuất hiện lần đầu tiên vào năm 1921 trong tác phẩm “Rossum’s Universal Robot” của Karel Capek. Trong tác phẩm nhân vật Rossum và con trai đã tạo ra chiếc máy giống con người để phục vụ cho con người.
>
> Ngành công nghiệp robot có những bước phát triển đáng kể trong hơn nửa thế kỷ qua nhờ những quan điểm như thay thế con người làm các công việc nặng nhọc trong môi trường nguy hiểm, độc hại, có thể thực hiện nhiều nhiệm vụ và hoạt động với độ chính xác cao. Bên cạnh đó, nhờ khả năng tích hợp với các thiết bị ngoại vi làm tang khả năng thích ứng với sự thay đổi môi trường làm việc. Việc ứng dụng các giải pháp điều khiển thông minh giúp robot có khả năng tự học và tự giải quyết vấn đề, tạo tiền đề cho phạm vi ứng dụng robot không chỉ giới hạn trong các dây chuyền gia công, chế tạo, mà ngày càng được ứng dụng rộng rãi trong nhiều lĩnh vực của đời sống như: robot trong công nghiệp, nông nghiệp, đóng tàu, xây dựng, y học, an ninh quốc gia và trong lĩnh vực dân dụng.
>
> Robot tự hành hay robot di động là những robot có thể tự động di chuyển tới các vị trí khác nhau mà không cần đến sự hỗ trợ từ bên ngoài của con người. Khác với phần lớn các loại robot công nghiệp chỉ có thể di chuyển trong một không gian nhất định, robot di động có những tính năng đặc biệt về di chuyển để có thể di chuyển tự do trong một không gian được thiết lập trước để đi đến các vị trí mong muốn. Khả năng di chuyển này giúp robot di động có nhiều ứng dụng trong môi trường làm việc khác nhau.
>
> Robot di động di chuyển trong môi trường của chúng, không cố định vào một vị trí thực. Robot di động có thể là “tự trị” có nghĩa là chúng có khả năng điều hướng một môi trường không kiểm soát được mà không cần các thiết bị hướng dẫn vật lý hoặc cơ điện. Ngoài ra, robot di động có thể dựa vào các thiết bị hướng dẫn cho phép nó di chuyển tuyến đường định hướng được xác định trước trong không gian tương đối được kiểm soát (robot tự điều khiển). Nó khác với robot công nghiệp thường đặt gần cố định và hoạt động bằng các cánh tay.
>
> Robot hoạt động trên mặt đất (Ground Robot di động WMRs) có thể phân loại robot di chuyển bằng bánh xe (Wheeled Robot di động) và robot di chuyển bằng chân (Legged Robot di động LMRs).

<table style="width:95%;">
<colgroup>
<col style="width: 52%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><img src="assets/do-an-cdt/media/image6.jpeg" style="width:3.25314in;height:1.955in" alt="Mô phỏng robot Perseverance hoạt động tại miệng hố Jezero trên sao Hỏa. Ảnh: NASA." /></p>
<p><span id="_bookmark5" class="anchor"></span><em>Hình 1.1: Robot Perseverance trên sao Hoả</em></p>
</blockquote></th>
<th><blockquote>
<p><img src="assets/do-an-cdt/media/image7.jpeg" style="width:1.48851in;height:1.98458in" alt="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/HONDA_ASIMO.jpg/800px-HONDA_ASIMO.jpg" /></p>
<p><span id="_bookmark6" class="anchor"></span><em>Hình 1.2: Robot hình người ASIMO</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Robot di động còn bao gồm các loại phương tiện bay không người lái (Unmanned Aeria Vehices) và phương tiện dưới nước tự trị (Autonomous Underwater Vehices).

<img src="assets/do-an-cdt/media/image8.jpeg" style="width:5.19097in;height:2.05208in" alt="Robot bay" />

> <span id="_bookmark7" class="anchor"></span>_Hình 1.3: Robot UAV VA–1000_
>
> Robot di động di chuyển bằng bánh xe được sử dụng rộng rãi vì chúng phù hợp với các ứng dụng đặc trưng, có kết cấu cơ khí đơn giản hơn các loại robot khác và tiêu thụ ít năng lượng hơn. Các loại robot di chuyển bằng chân phù hợp với các địa hình phức tạp, phi tiêu chuẩn. Robot di động còn có thể kể đến các loại tay máy di động (Mobile Manipulator), là robot di động có thể di chuyển bằng bánh xe hoặc chân được trang bị một hoặc nhiều tay máy hạng nhẹ để thực hiện các nhiệm vụ khác nhau.

<a id="mục-tiêu-của-đề-tài"></a>

## Mục tiêu của đề tài

> Mục tiêu của đề tài chính là nghiên cứu và thiết kế Robot phục vụ lễ tân làm việc trong một không gian năng động nhiệt huyết với nhiệm vụ của Robot là vận chuyển các món ăn cùng với thực đơn đến các vị trí bàn khác nhau.
>
> Robot phục vụ lễ tân là một hệ thống cơ điện tử phức tạp, phải có sự phối hợp hài hoà giữa cơ khí, điện và điều khiển. Thêm vào đó, chương trình hoạt động phải chạy đúng yêu cầu các bài toán đặt ra đặt ra của một Robot phục vụ lễ tân:

- Di chuyển và tìm đến vị trí các bàn.

- Hiển thị menu cho khách hàng chọn món.

- Tìm đường về nhà bếp.

- Chở đồ ăn đến những bàn đã chỉ định.

- Giao tiếp một số câu thoại đơn giản

<a id="phương-pháp-nghiên-cứu"></a>

## Phương pháp nghiên cứu

- Phương pháp quan sát thực tế: nhóm chúng em đã có thời gian tiếp cận với các sản phẩm trong thực tế qua quan sát các robot lễ tân trong các khách sạn, nhà hàng...

<a id="robot-phục-vụ-pudu"></a>

### + Robot phục vụ Pudu

- Hãng sản xuất: Shenzhen Pudu Technology-hãng công nghệ cung cấp Robot phục vụ đến hàng ngàn chủ nhà hàng Trung Quốc.

- Chức năng: phục vụ được từ 300 đến 400 bữa ăn mỗi ngày.

- Tuổi thọ: 10 năm

- Giá thành: khoảng 5.650 USD đến 7.060 USD

<img src="assets/do-an-cdt/media/image9.jpeg" style="width:5.66887in;height:3.32562in" />

> <span id="_bookmark10" class="anchor"></span>_Hình 1.4: Robot phục vụ nhà hàng Pudu_

<a id="robot-cloi-servebot"></a>

### + Robot CLOi ServeBot

- Hãng sản xuất: LG Electronics – Hàn Quốc.

- Thông số: cao 130 cm, trọng lượng 15kg.

- Chức năng: Serving Robot sẽ xuất hiện ở các khách sạn, phòng chờ sân bay và thậm chí là nhà hàng – nơi nó sẽ bưng bê đồ ăn, đồ uống cho khách hàng nhờ khay đựng của nó.

<img src="assets/do-an-cdt/media/image10.jpeg" style="width:5.69416in;height:3.70531in" alt="LG launches CLOi ServeBot in the US - Mobile Robot Guide" />

> <span id="_bookmark11" class="anchor"></span>_Hình 1.5: Robot CLOi ServeBot của hãng LG Electronic_

- Phương pháp nghiên cứu lý thuyết: Trong thời gian nghiên cứu, nhóm đồ án đã tìm hiểu qua các sách tài liệu, các đồ án sinh viên khóa trước, các trang web… liên quan đến đề tài Mobile Robot.

> Từ quá trình bên trên, nhóm đồ án đã quyết định tiến hành xây dựng một robot phục vụ lễ tân bao gồm các kệ để phục vụ trong các quán ăn hay nhà hàng, khách sạn… Để đạt được việc chế tạo ra một con robot tự động phục vụ các yêu cầu trên thì những vấn đề sau cần được tìm hiểu và nghiên cứu:

- Bài toán quét bản đồ tìm đường sử dụng cảm biến Lidar qua bộ điều khiển STM32. Tính toán bài toán động học xác định mối liên hệ giữa các chuyển động và tìm quy luật thay đổi vị trí, quy luật chuyển hướng của robot.

- Tính toán bài toán động lực học tìm hiểu nguyên nhân gây chuyển động và sự liên kết giữa các robot.

- Bài toán điều khiển động cơ giảm tốc và điều khiển tốc độ bằng xung PWM qua giao thức truyền UART.

> Sau khi đã tìm hiểu và nghiên cứu, việc tiến hành làm ra sản phẩm cũng rất quan trọng. Khi sản phẩm được hoàn thành thì sản phẩm phải đạt được những tiêu chí sau:

- Robot tự hành lễ tân phải đi chính xác trên quỹ đạo đã định sẵn từ trước.

- Phát hiện được vật cản bằng cảm biến đồng thời ngừng hoạt động và báo hiệu bằng còi.

- Kích thước nhỏ gọn nhưng vẫn đảm bảo độ cứng vững và tính linh hoạt.

- Vận tốc di chuyển và dừng đỗ chính xác.

- Năng suất làm việc cao, đảm bảo tính ổn định trong quá trình làm việc.

- Khung vỏ dễ dàng tháo lắp, thuận lợi cho việc sửa chữa, nâng cấp.

<a id="giới-hạn-phạm-vi-nghiên-cứu"></a>

## Giới hạn, phạm vi nghiên cứu

> Do điều kiện làm việc trong thời gian ngắn và khả năng kiến thức có hạn nên đề tài được giới hạn trong điều kiện sau:

- Nghiên cứu, thiết kế mô hình “Robot phục vụ lễ tân dạng vi sai”.

- Cho phép hoạt động trong phòng thí nghiệm.

- Sử dụng màn hình hiển thị và nút nhấn để tương tác trực tiếp với con người.

- Sử dụng các loại cảm biến khác nhau để tránh va chạm, đảm bảo an toàn cho robot và con người.

<a id="chương-2-cơ-sở-lý-thuyết"></a>

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT

<a id="nguyên-lý-làm-việc-chức-năng-của-từng-module-trong-hệ-thống"></a>

## Nguyên lý làm việc, chức năng của từng module trong hệ thống

1.  **Nguyên lý làm việc**

> Robot lễ tân được xem là một trong những ứng dụng công nghệ khách sạn hiệu quả nhất, robot giúp nâng cao mức độ hài lòng của khách hàng.
>
> Robot là thiết bị hoặc hệ thống được thiết kế để thực hiện một tập hợp các nhiệm vụ cụ thể ở mức độ hiệu quả và độ chính xác gần như tuyệt đối. Ví dụ các robot làm trong dây chuyền lắp ráp và máy CNC, được thiết kế để tạo ra các bộ phận cực kỳ phức tạp mà con người yêu cầu. Ở ngành khách sạn, mục đích chính của robot là nâng cao năng suất lao động và trải nghiệm tổng thể của khách hàng.
>
> Có một vài lý do cho xu hướng này. Ở góc độ tài chính, chi phí triển khai công nghệ khách sạn đã rẻ hơn rất nhiều so với trước kia. Điều này cho thấy rằng bất cứ loại khách sạn nào, thậm chí là rất nhỏ vẫn có thể tận dụng những lợi thế liên quan. Tuy nhiên, chúng ta cũng cần lưu ý các yêu cầu của khách đang bắt đầu thay đổi.
>
> Nhờ kết nối không dây và sự hiện diện gần như khắp nơi của điện thoại thông minh, khách hàng mong đợi chất lượng dịch vụ nhiều hơn trong suốt thời gian lưu trú. Điều này rõ ràng liên quan đến sự hiện diện của công nghệ ở một mức độ nhất định. Robot lễ tân có thể mang lại lợi thế cạnh tranh, vì vậy các nhà quản lý có lý do để tận dụng cơ hội mà robot mang lại.
>
> Như bạn có thể đã tưởng tượng, có rất nhiều loại Robot lễ tân và mỗi loại được thiết kế để phù hợp với một mục đích riêng.
>
> Khi bạn kích hoạt chế độ làm việc cho robot lễ tân, hệ thống quét bản đồ được trang bị cho robot sẽ tiến hành lấy mẫu bản đồ từ môi trường xung quanh. Tiếp theo robot tự động định vị và thiết lập phương án di chuyển và phục vụ cách tối ưu nhất. Một số cảm biến siêu âm được trang bị có thể giúp robot tránh vật cản hoặc dừng tại vị trí mong muốn. Chức năng chạy theo bản đồ giúp cho robot lễ tân có thể lên kế hoạch làm việc nhanh và hiệu quả giúp tiết kiệm thời gian phục vụ.
>
> Màn hình HMI và chức năng phục vụ bằng giọng nói được trang bị thêm khi đến vị trí mong muốn để hiển thị các bàn đã được phục vụ. Quá trình này diễn ra liên tục cho đến khi hoàn thành quá trình phục vụ tại các bàn mong muốn. Khi robot gặp sự cố thì
>
> robot dừng hoạt động kiểm tra vị trí và thông báo cho đến khi được sửa chữa hoặc thiết lập lại từ xa để robot có thể tiếp tục hoạt động.
>
> Hầu như các loại robot lễ tân đều được trang bị nhiều bộ cảm biến thông minh giúp máy có thể tự động dừng lại và tìm kiếm hướng đi khác khi gặp chướng ngại vật, vật cản hoặc cầu thang, hay tìm kiếm và quay trở lại trạm sạc khi gần hết điện.

2.  **Chức năng của từng module trong hệ thống**

<img src="assets/do-an-cdt/media/image11.png" style="width:5.54743in;height:2.095in" />

> <span id="_bookmark15" class="anchor"></span>_Hình 2.1: Sơ đồ cấu trúc hệ thống robot phục vụ lễ tân_
>
> Cấu trúc của một robot phục vụ lễ tân bao gồm hai module chính đó là:

- Module di chuyển: đảm bảo cho việc di chuyển trong không gian nhà hàng, khách sạn. Module di chuyển được chia thành hai hệ thống nhỏ là: Hệ thống cảm biến và hệ thống di chuyển.

> +) Hệ thống cảm biến đảm nhiệm thu thập thông tin vật lý từ môi trường như đường line và vật cảm đảm bảo cho robot đi đúng đường và tránh va chạm không mong muốn.
>
> +) Hệ thống di chuyển có nhiệm vụ đưa đưa robot phục vụ lễ tân đến những nơi đã chỉ định.

- Module phục vụ lễ tân: Đảm bảo cho việc phục vụ trở nên dễ dàng và thuận tiện cho khách hàng. Bên trong module phục vụ lễ tân được chia thành hai hệ thống nhỏ: Hệ thống thông báo và hiển thị, hệ thống thu thập thông tin.

> +) Hệ thống thông báo và hiển thị có chức năng thông báo và hiển thị những thông tin đảm bảo cho chức năng của module lễ tân như: giới thiệu về thực đơn, giới thiệu về nhà hàng, chúc quý khách ngon miệng…
>
> +) Hệ thống thu thập thông tin giúp robot thu thập thông tin từ khách hàng như: thực đơn món ăn, sự hài lòng của khách hàng…
>
> _a, Module di chuyển_
>
> Để có phương án di chuyển phù hợp, nhóm sẽ sử dụng cơ cấu vi sai (Differential drive). Cơ cấu này điều khiển với hai bánh dẫn động phía sau để đạt được vận tốc và góc xoay mong muốn. Xe cần có bánh xe tự lựa để giữ cân bằng.

<img src="assets/do-an-cdt/media/image12.jpeg" style="width:3.44329in;height:2.3625in" />

<span id="_bookmark16" class="anchor"></span>_Hình 2.2: Cơ cấu vi sai_

**+ Ưu điểm**

- Đơn giản về cơ khí và dễ dàng áp dụng.

- Không cần cơ cấu bẻ lái.

- Bán kính quay xe bằng không.

- Điều khiển đồng thời vận tốc và hướng của xe bằng hai động cơ.

> **+ Nhược điểm**

- Khó điều khiển chạy thẳng do hai động cơ độc lập.

- Dễ lật đối với xe chỉ có một bánh tự lựa trên địa hình gồ ghề.

> _b, Module phục vụ lễ tân_
>
> Chức năng chính của module là lên list phục vụ cho khách hàng giúp cho khách hàng được thoải mái.
>
> Các chức năng được xem là một trong những ứng dụng công nghệ khách sạn hiệu quả nhất, robot khách sạn giúp nâng cao mức độ hài lòng của khách hàng. Từ đó tang trải nghiệm của khách hàng và uy tín của nhà hàng hay khách sạn.

<a id="giới-thiệu-thực-đơn"></a>

### Giới thiệu thực đơn

> Chức năng giới thiệu đa phần quan trọng cho mọi loại hình robot phục vụ nói chúng cũng như robot lễ tân nói riêng. Khi một khách hàng mới đến thì đây là điểm đầu tiên mà khách hàng nhìn vào chưa kể là người đến họ chưa biết gì về nơi mà họ sắp thưởng thức các bữa tiệc.
>
> Robot sẽ chào hỏi khách hàng và trực tiếp giới thiệu thực đơn cho khách hàng thông qua hệ thống loa tích hợp sẵn trên robot sau đó thực hiện công việc thu thập thông tin thực đơn của khách hàng thông qua hệ thống nút nhấn và màn hình hiển thị.

<a id="lên-menu-danh-sách-thực-đơn-khách-yêu-cầu"></a>

### Lên menu danh sách thực đơn khách yêu cầu

> Khách hàng sẽ lên thực đơn thông qua hệ thống nút ấn và màn hình hiển thị trên robot. Sau khi đã được đặt yêu cầu các món mà khách hàng muốn đặt thì robot có nhiệm vụ ghi lại thông tin yêu cầu từ các vị trí mà khách hàng đặt để tránh sai sót. Vị trí bàn và các món ăn đã đặt sẽ được hiển thị trên màn hình sau khi robot về tới vị trí xuất phát. Thực đơn sau đó sẽ được thông báo cho người quản lý thông quan màn hình hiển thị.

<a id="hỏi-xem-khách-cần-thêm-gì-cho-thực-đơn-đã-chọn-hay-không"></a>

### Hỏi xem khách cần thêm gì cho thực đơn đã chọn hay không?

> Sau khi ghi lại thông tin thì robot có nhiệm vụ hỏi thêm khách hàng cần gì thêm không để cũng như là xác nhận rằng khách hàng đã yêu cầu những thực đơn có trong danh sách. Hoặc là khách hàng có thể quên 1 số món mà đã đặt.
>
> Chức năng này cũng giúp cho chủ khách sạn có thêm được số lượng mà khách hàng yêu cầu, thay vì giới thiệu thực đơn như bình thường thì hỏi người dùng cần thêm đồ gì để có thể cung cấp.

<a id="giới-thiệu-về-nhà-hàng-khách-sạn"></a>

### Giới thiệu về nhà hàng, khách sạn

> Trong quá trình di chuyển trên đường line. Robot sẽ sử dụng loa để phát âm thanh giới thiệu về nhà hàng, khách sạn giúp cho khách hàng hiểu rõ hơn về nhà hàng, khách sạn đó. Đây sẽ là một cách marketing hiệu quả. Ngoài ra, robot sẽ nói them một số câu thoại như “Cảm ơn quý khách đã đến nhà hàng, khách sạn …”, “Chúc quý khách có một ngày tuyệt vời”, “Chúc quý khách ăn ngon miệng”,…để tăng thêm độ thân thiện cho robot.

3.  **Hệ thống điều khiển**

> Hệ thống điều khiển là hệ thống quản lý và ra lệnh, chỉ dẫn các thiết bị hoặc hệ thống khác. Trong dự án này, hệ thống điều khiển có vai trò đặc biệt quan trọng giúp robot phục vụ vừa có thể di chuyển đến những nơi được chỉ định một cách chính xác vừa tạo được các hiệu ứng giao diện người dùng thân thiện.
>
> Để đáp ứng được những yêu cầu của bài toán đặt ra thì hệ thống điều khiển phải sử dụng vi xử lý có công suất mạnh mẽ và có thể hoạt động một cách độc lập. Một số dòng vi điều khiển được đề xuất ở đây là: 8051, PIC, AVR, ARM.
>
> <span id="_bookmark17" class="anchor"></span>_Bảng 2.1: Bảng phân tích ưu điểm, nhược điểm của các loại vi điều khiển_

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>STT</p>
</blockquote></th>
<th><blockquote>
<p>Loại vi điều khiển</p>
</blockquote></th>
<th><blockquote>
<p>Tổng quan</p>
</blockquote></th>
<th><blockquote>
<p>Ưu điểm</p>
</blockquote></th>
<th><blockquote>
<p>Nhược điểm</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Vi điều khiển 8051</p>
</blockquote></td>
<td><blockquote>
<p>Vi điều khiển 8051 là dòng vi điều khiển 8-bit được phát triển bởi Intel vào năm 1981. Vi điều khiển này có 128 byte RAM, 4 KB ROM, 2 bộ hẹn giờ, 1 cổng</p>
<p>nối tiếp và 4 cổng trên một chip. CPU cũng có thể hoạt động với 8 bit dữ liệu tại một thời điểm vì 8051 là bộ xử lý 8 bit. Hầu hết vi điều khiển 8051 đều chứa 4 KB ROM, cũng có trường hợp số lượng ROM có thể vượt quá lên đến 64 KB.</p>
</blockquote></td>
<td><ul>
<li><p>Giá thành rẻ.</p></li>
<li><p>Dễ dàng lập trình.</p></li>
</ul></td>
<td><ul>
<li><p>Không ổn định</p></li>
<li><p>Không tích hợp sẵn board mạch điều khiển.</p>
<ul>
<li><p>Số lượng chân vi điều khiển còn hạn chế.</p></li>
<li><p>Khó làm mạch điều khiển.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Vi điều khiển PIC của Microchip</p>
</blockquote></td>
<td><blockquote>
<p>- Bộ điều khiển giao diện ngoại vi (PIC) là vi điều khiển được phát triển bởi Microchip,</p>
<p>vi điều khiển PIC thực hiện chương trình nhanh chóng và</p>
</blockquote></td>
<td><ul>
<li><p>Dễ dàng lập trình.</p></li>
<li><p>Giá thành rẻ.</p></li>
</ul></td>
<td><ul>
<li><p>Hơi khó cho người mới bắt đầu tìm hiểu.</p></li>
<li><p>Khó thiết kế mạch.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th></th>
<th></th>
<th><blockquote>
<p>đơn giản khi so sánh với các vi điều khiển khác như 8051.</p>
<p>- Chúng ta biết rằng vi điều khiển là một chip tích hợp bao</p>
<p>gồm RAM, ROM, CPU, TIMER và COUNTER. PIC là</p>
<p>vi điều khiển cũng bao gồm RAM ROM, CPU, TIMER,</p>
<p>COUNTER, ADC (bộ chuyển đổi analog sang kỹ thuật số), DAC (bộ chuyển đổi kỹ thuật số sang analog). Vi điều khiển PIC cũng hỗ trợ các giao thức như CAN, SPI, UART để giao tiếp với các thiết bị ngoại vi bổ sung.</p>
</blockquote></th>
<th></th>
<th style="text-align: center;"><blockquote>
<p>- Số lượng chân vi điều khiển còn hạn chế.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vi điều khiển ATMega2560</p>
</blockquote></td>
<td><blockquote>
<p>ATMega2560 của hãng Atmel là vi điều khiển công</p>
<p>suất thấp 8 bit là board mạch Arduino Mega phổ biến. Có kiến trúc vi mạch AVR RISC 8 bit với bộ nhớ flash 256KB, 8KB SRAM và EEPROM 4KB. Hỗ trợ nhiều loại thiết bị ngoại vi, bao gồm bộ định thời, bộ đếm, bộ tạo</p>
<p>PWM, bộ so sánh và ADC. Có thể đạt tốc độ xử lý lên đến 16MHz với nguồn cấp 5V.</p>
</blockquote></td>
<td><ul>
<li><p>Dễ dàng lập trình và điều khiển.</p>
<ul>
<li><p>Cộng đồng sử dụng đông đảo.</p></li>
</ul></li>
<li><p>Thư viện hỗ trợ đa dạng.</p>
<ul>
<li><p>Phần mềm lập trình dễ tiếp cận và</p></li>
</ul></li>
</ul></td>
<td><blockquote>
<p>- Chỉ thực hiện được các project đơn giản</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th style="text-align: center;"><blockquote>
<p>dễ dàng nạp chương trình (phù hợp với người mới).</p>
</blockquote>
<ul>
<li><p>Có nhiều board mạch thiết kế sẵn.</p></li>
<li><p>Phù hợp với các chương trình phức tạp.</p></li>
</ul></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Bộ xử lý ARM</p>
</blockquote></td>
<td><blockquote>
<p>- ARM tạo ra bộ vi xử lý đa lõi RISC 32 bit và 64 bit.</p>
<p>- Bộ xử lý ARM được sử dụng rộng rãi trong các thiết bị điện tử như điện thoại thông minh, máy tính bảng, trình phát đa phương tiện và các thiết bị di động khác, chẳng hạn như</p>
<p>thiết bị đeo. Do được giảm thành tập lệnh, nên nó cần ít transistor hơn, cho phép kích thước khuôn IC nhỏ hơn. Vi xử lý ARM kích thước nhỏ, giảm độ khó và tiêu thụ điện năng</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>- Kích thước nhỏ gọn nhưng mạnh mẽ.</p>
</blockquote>
<ul>
<li><p>Giá thành phù hợp với hiệu năng.</p></li>
<li><p>Phù hợp với những chương trình hiệu suất cao.</p></li>
</ul></td>
<td><blockquote>
<p>- Khó cho người mới bắt đầu.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th></th>
<th></th>
<th><blockquote>
<p>thấp nên rất phù hợp với các thiết bị thu nhỏ.</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 🡪 Sau những ưu điểm và nhược điểm được phân tích ở trên, nhóm quyết định sử vi điều khiển dòng ARM bởi sự mạnh mẽ mà nó đem lại.

1.  **Hệ thống cảm biến**

> Đối với mô hình robot di động phục vụ lễ tân, cảm biến đóng vai trò cực kì quan trọng giúp cho robot có thể cảm nhận những tác nhân vật lý tác động lên robot trong quá trình hoạt động. Từ các số liệu hệ thống cảm biến robot có thể đo đạc, tính toán và đưa ra các quyết định của robot.
>
> Robot di chuyển luôn được trang bị các cảm biến phát hiện vật cản với mục đích chính để đảm bảo an toàn cho người và vật xung quanh khu vực di chuyển của robot. Mỗi vị trí lắp cảm biến trên xe có chức năng riêng. Ví dụ như:

- Tự động tính toán và duy trì tốc độ trong khu vực an toàn.

- Tự động phanh khẩn cấp khi nhận ra vật cản ở quá gần.

- Cảnh báo khi phát hiện vật cản hoặc người di chuyển ở trong vùng di chuyển của robot.

> <span id="_bookmark18" class="anchor"></span>_Bảng 2.2: Bảng phân tích ưu, nhược điểm của các loại cảm biến phát hiện vật cản_

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 39%" />
<col style="width: 16%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>STT</p>
</blockquote></th>
<th><blockquote>
<p>Tên cảm biến</p>
</blockquote></th>
<th><blockquote>
<p>Tổng quan</p>
</blockquote></th>
<th><blockquote>
<p>Ưu điểm</p>
</blockquote></th>
<th><blockquote>
<p>Nhược điểm</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Cảm biến Radar</p>
</blockquote></td>
<td><blockquote>
<p>- Cảm biến Radar là cảm biến vi sóng, hoạt động dựa trên hiệu ứng doppler, tần số 5.8 Ghz dưới</p>
<p>10m. Mọi loại Radar đều hoạt động bằng cách phát ra sóng rồi nhận tín hiệu phản xạ. Sau đó chuyển tín hiệu đó thành thông tin để đưa vào bộ xử lý trung tâm.</p>
</blockquote></td>
<td><ul>
<li><p>Vùng cảm biến rộng (tốt nhất trong bán kính 6-8m).</p></li>
<li><p>Góc quét rộng.</p></li>
<li><p>Phù hợp với xe tự</p></li>
</ul>
<blockquote>
<p>hành có vận</p>
</blockquote></td>
<td><blockquote>
<p>- Góc nhìn hẹp, không thể sử dụng cho góc nhìn 360 độ.</p>
<p>- Không nhận dạng được ký tự quang học: màu sắc, độ tương phản.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 39%" />
<col style="width: 16%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th></th>
<th></th>
<th><ul>
<li><p>Nguyên lý hoạt động: Sử dụng cụm sóng âm thanh để đo</p></li>
</ul>
<blockquote>
<p>khoảng cách.</p>
</blockquote>
<ul>
<li><p>Cảm biến Radar trên xe tự hành sử dụng loại Radar tầm</p></li>
</ul>
<blockquote>
<p>gần. Nó có thể thay thế cảm biến siêu âm, cảnh báo vật cản, hỗ trợ dừng xe khi vật cản ở quá gần.</p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p>tốc tương đối.</p>
<p>- Dữ liệu xử lý vừa phải.</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>- Giá thành khá cao so với cảm biến siêu âm.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Cảm biến siêu âm – Ultrasonic range sensor</p>
</blockquote></td>
<td><blockquote>
<p>- Nguyên lý hoạt động: Sử dụng sóng âm thanh tần số cao</p>
<p>để đo (40 -70 kHz)</p>
</blockquote>
<ul>
<li><p>Tín hiệu được bức xạ tới mục tiêu và phản xạ lại nguồn.</p></li>
<li><p>Chính vì chi phí thấp nên cảm biến siêu âm được sử dụng nhiều</p></li>
</ul>
<blockquote>
<p>với tính linh hoạt cao</p>
<p>- Ultrasonic chính là loại cảm biến thích hợp để xử lý các va chạm này. Chúng giúp xe tự hành AGV trở nên thông minh và thực hiện tốt công việc vận</p>
<p>chuyển nguyên vật liệu.</p>
</blockquote></td>
<td><ul>
<li><p>Thời gian phản hồi nhanh, độ chính xác tốt trong phạm vi ngắn, sai số khoảng 0,15% (2m)</p>
<ul>
<li><p>Chi phí thấp</p></li>
<li><p>Thường được lắp đặt tại điểm mù trên xe</p></li>
</ul></li>
</ul></td>
<td style="text-align: center;"><blockquote>
<p>- Cự li hoạt động ngắn</p>
<p>- Không nhận dạng ký tự quang học</p>
<p>- Cảm biến siêu âm sử dụng cho xe tự hành chịu ảnh hưởng nhiều bởi nhiệt độ và áp suất.</p>
<p>Vì thế nên AGV chỉ phù hợp hoạt động trong môi trường nhiệt độ nhỏ hơn 60 độ C và áp suất nhỏ hơn 1 bar.</p>
<p>- Dễ bị nhiễu tín hiệu khi lắp đặt, vì thế nên</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 39%" />
<col style="width: 16%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"><blockquote>
<p>cần chú ý lắp đặt đúng hướng dẫn.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Cảm biến LiDAR</p>
</blockquote></td>
<td><blockquote>
<p>- Nguyên lý hoạt động: Sử dụng laser để đo khoảng cách vật cản, từ đó tiến hành thao tác</p>
<p>phù hợp.</p>
</blockquote>
<ul>
<li><p>LiDAR hoạt động bằng cách phát ra tia laser rồi đo tín hiệu phản xạ trở lại với độ chính xác rất cao. LIDAR thường được ứng dụng để quét địa hình thành bản đồ 3D. Thậm chí với sự phát</p></li>
</ul>
<blockquote>
<p>triển công nghệ như hiện nay, LIDAR có thể giúp cho việc phanh khẩn cấp hiệu quả, chính xác hơn và tránh va chạm.</p>
</blockquote>
<ul>
<li><p>Chính vì sự chính xác của nó nên chi phí cho loại cảm biến này khá cao. Nên cân nhắc lại chi phí cho xe tự hành AGV khi</p></li>
</ul>
<blockquote>
<p>lựa chọn loại cảm biến này.</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>- Đo khoảng cách với độ chính xác cao, khoảng đo khá rộng (lên tới 200m).</p>
</blockquote>
<ul>
<li><p>Hình ảnh có độ phân giải lớn, có khả năng quét 3D theo tỉ lệ thời gian, đưa ra phân tích chính xác về môi trường xung quanh.</p></li>
<li><p>Hoạt động tốt ngay cả trong điều kiện ánh sáng yếu.</p></li>
</ul></td>
<td><ul>
<li><p>Không hoạt động hiệu quả bằng Radar.</p></li>
<li><p>Không nhận dạng ký tự quang học.</p></li>
<li><p>Dữ xử lý liệu lớn.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table style="width:97%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 39%" />
<col style="width: 16%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>Vision camera – Optic sensor</p>
</blockquote></th>
<th><blockquote>
<p>- Xe tự hành AGV cần tích hợp Vision camera để dẫn đường cho</p>
<p>AGV di chuyển. Nó thường được kết hợp với LiDAR để cung cấp khả năng điều hướng cho robot AGV.</p>
<p>- Nguyên lý hoạt động: Sử dụng thị giác máy tính vision camera để nhận dạng và đo</p>
<p>lường đối tượng.</p>
<p>- Bộ điều khiển của AGV sẽ nhận thông tin truyền về từ thị giác máy dưới dạng điện áp hoặc trên giao diện kỹ thuật số. Với cảm biến vạch quang, AGV có</p>
<p>thể phát hiện băng dính phát quang thông thường dù nó có bị bẩn hay mờ.</p>
</blockquote></th>
<th><ul>
<li><p>Cảm biến nhanh nhạy, trả về kết quả chính xác cao.</p></li>
<li><p>Chi phí rất vừa phải.</p></li>
</ul></th>
<th style="text-align: center;"><blockquote>
<p>- FOV giới hạn, góc quét hẹp, không quét được góc 360 độ</p>
<p>- Không hoạt động tốt trong điều kiện ánh sáng yếu hoặc điều kiện ánh sáng khác nhau</p>
<p>- Tiêu thụ nhiều năng lượng xử lý vì cần xử lý lượng dữ liệu lớn.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Từ những ưu điểm và nhược điểm kể trên. Nhóm chúng tôi quyết định lựa chọn cảm biến LiDAR cho dự án của mình vì cảm biến LiDAR vừa đảm bảo chất lượng hình ảnh của bản đồ, thời gian phản hồi nhanh, chính xác lại đảm bảo về yêu cầu về tốc độ xử lý của vi xử lý đã lựa chọn.

1.  **Cơ cấu chấp hành**

> Cơ cấu chấp hành của robot di động phục vụ lễ tân nằm toàn bộ ở bộ phận di chuyển của robot.
>
> Robot tự hành di động nên thông thường sử dụng động cơ dùng dòng điện DC. Một số loại động cơ dùng dòng điện DC như: động cơ bước, động cơ DC, động cơ DC servo. Robot tự hành cần điều khiển vận tốc nên động cơ DC phải có hồi tiếp vận tốc (mặc dù một số động cơ DC điều khiển được chính xác vận tốc, không cần hồi tiếp nhưng giá sẽ rất cao). Do đó chọn động cơ bước hoặc động cơ DC servo là phương án khả thi. Sau
>
> đây là những phân tích về ưu, nhược điểm của hai loại động cơ này, từ đó có thể xác định được loại động cơ cần dùng để phù hợp với yêu cầu đặt ra.
>
> _a, Động cơ bước_
>
> Động cơ bước thông thường là loại động cơ điều khiển vòng hở, biến đổi các xung điện rời rạc kế tiếp nhau thành chuyển động quay của rotor. Giá trị góc quay phụ thuộc và số xung điện cấp vào động cơ. Mỗi vòng quay có số bước cố định, thay đổi tốc độ quay bằng cách thay đổi tốc độ tín hiệu điện cấp cho động cơ.

<img src="assets/do-an-cdt/media/image13.jpeg" style="width:3.19067in;height:2.56281in" />

<span id="_bookmark19" class="anchor"></span>_Hình 2.3: Động cơ bước_

**Ưu điểm:**

- Không cần hồi tiếp tín hiệu.

- Điều khiển chính xác, không có vọt lố và có momen giữ tại một vị trí.

**Nhược điểm:**

- Dễ bị trượt bước khi mang tải lớn.

- Tốc độ của động cơ không cao, tối đa từ 1000 ÷ 2000 (rpm).

- Gây rung động.

_b, Động cơ DC servo_

> Động cơ DC servo là động cơ DC có thêm bộ phận đo thông số đầu ra của động cơ thông thường là góc quay, vận tốc quay. Từ các sai số góc quay, vận tốc quay thì bộ điều khiển sẽ tăng hay giảm dòng cấp cho động cơ để đạt góc quay, vận tốc mong muốn.
>
> <img src="assets/do-an-cdt/media/image14.jpeg" style="width:3.11018in;height:2.86031in" />
>
> <span id="_bookmark20" class="anchor"></span>_Hình 2.4: Động cơ DC servo_
>
> **Ưu điểm:**

- Momen khởi động và vận tốc lớn.

- Động cơ chạy êm khi đạt vận tốc cố định.

- Có tín hiệu hồi tiếp nên có thể điều khiển được góc quay và vận tốc.

> **Nhược điểm:**

- Khi dừng lại, tùy theo chất lượng của bộ điều khiển ảnh hưởng đến đáp ứng nên có thể gây dao động, rung lắc.

- Tín hiệu hồi tiếp có thể bị nhiễu.

- Dưới đây là bảng tổng kết các đặc điểm của hai loại động cơ đã được phân tích.

> Dựa vào phân tích và điều kiện hoạt động của robot, động cơ DC servo sẽ là phương án được lựa chọn để thiết kế robot.
>
> Từ những so sánh trên, lựa chọn phương án sử dụng động cơ DC servo và bộ truyền bánh răng. Kết hợp với những yêu cầu thiết kế robot như linh hoạt, nhỏ gọn nên chọn loại động cơ DC servo có tích hợp sẵn hộp giảm tốc.

<a id="hệ-điều-hành-ubuntu-và-mô-phỏng-mobile-robot-trên-gazebo"></a>

## Hệ điều hành Ubuntu và mô phỏng mobile robot trên Gazebo

1.  **Hệ điều hành Ubuntu**

_a, Tổng quan hệ điều hành Ubuntu_

> Ubuntu là một hệ điều hành máy tính dựa trên Debian GNU/Linux, một bản phân phối Linux thông dụng. Ubuntu là hệ điều hành mã nguồn mở tự do, có nghĩa là người dùng được tự do chạy, sao chép, phân phối, nghiên cứu, thay đổi và cải tiến phần mềm theo điều khoản của giấy phép GNU GPL.

<img src="assets/do-an-cdt/media/image15.jpeg" style="width:5.69026in;height:3.67583in" alt="Background pattern Description automatically generated" />

> <span id="_bookmark22" class="anchor"></span>_Hình 2.5: Giao diện hệ điều hành Ubuntu_

- **Ưu điểm của hệ điều hành Ubuntu:**
  - Ubuntu hoàn toàn miễn phí

  - Hệ điều hành Ubuntu hoàn toàn không có virus

  - Mọi phần mềm được auto update 100%

  - Ubuntu luôn bảo vệ mọi dữ liệu quý giá của người sử dụng

  - Ít tốn tài nguyên phần cứng

  - Khả năng tương thích cao

  - Kho ứng dụng là hoàn toàn miễn phí và môi trường khổng lồ

  - Chạy được nhiều ứng dụng có ở hệ điều hành Window.

> Phiên bản Ubuntu nhóm chúng em lựa chọn là phiên bản Ubuntu 20.04 LTS, bởi:

- Hiệu suất desktop được cải thiện với mức sử dụng CPU thấp

- Người dùng có tốc độ khung hình cao và mượt mà hơn

- Người dùng có thể cài đặt trực tiếp từ trình cài đặt

- Phiên bản Ubuntu 20.04 LTS tăng tốc độ khoa học dữ liệu, trên laptop và workstation bằng cách cung cấp các công cụ, trình điều khiển và thư viện mới nhất.

> _b, Mô phỏng Mobile robot trên Gazebo_
>
> Gazebo mô phỏng một hay nhiều robot trong một không gian mở. Có khả năng mô phỏng một loại robot, cảm biến và vật thể trong thế giới 3 chiều. Tạo ra phản hồi cho các cảm biến khi tương tác với các đối tượng trên bản đồ kỹ thuật số.
>
> Đặc tính kỹ thuật của Gazebo:

- Mô phỏng động.

- Đồ họa 3D nâng cao.

- Cảm biến và tiếng ồn.

- Không giản mở, có thể tự bổ sung, tùy chỉnh robot, cảm biến và môi trường điều khiển nhờ API của nó.

- Có nhiều mô hình robot.

<img src="assets/do-an-cdt/media/image16.jpeg" style="width:6.24267in;height:3.50781in" alt="Graphical user interface Description automatically generated" />

> <span id="_bookmark23" class="anchor"></span>_Hình 2.6: Mô phỏng Mobile robot trên Gazebo_

<a id="phương-pháp-quét-bản-đồ-bằng-lidar-trên-gazebo"></a>

## Phương pháp quét bản đồ bằng Lidar trên Gazebo

> ROS có một loại thông báo cụ thể cho dữ liệu quét laser 2D, được gọi là **sensor_msgs/LaserScan**. Mỗi **LaserScan** thông báo chứa dữ liệu cho một lần quét cảm biến và về cơ bản là một mảng các dấu nổi đại diện cho mỗi phép đo phạm vi (tính bằng mét), cùng với một số thông số bổ sung để hỗ trợ hiểu dữ liệu đúng cách. Thông báo LaserScan này cũng cho chúng ta biết khung TF nào được gắn vào lidar, để phần còn lại của hệ thống có thể tìm ra vị trí các điểm đánh trong không gian 3D. Điều này đặc biệt hữu ích cho những việc như kết hợp quét từ nhiều cảm biến cùng một lúc.

<img src="assets/do-an-cdt/media/image17.jpeg" style="width:4.72661in;height:3.04583in" alt="LaserScan" />

<span id="_bookmark25" class="anchor"></span>_Hình 2.7: Quét bản đồ từ LiDAR 2D_

<img src="assets/do-an-cdt/media/image18.jpeg" style="width:5.96807in;height:3.09146in" />

<span id="_bookmark26" class="anchor"></span>_Hình 2.8: Mô phỏng quét LiDAR trên Rviz_

<a id="tổng-quan-về-ros."></a>

## Tổng quan về ROS.

> Robot operating system (ROS) là một hệ thống phần mềm có tính linh hoạt và chuyên dụng cao dùng để lập trình và điều khiển robot. ROS bao gồm các thư viện, công cụ hỗ trợ lập trình, công cụ đồ họa, các công cụ hỗ trợ giao tiếp điều khiển trực tiếp với phần cứng cũng như các thư viện hỗ trợ việc lấy dữ liệu từ các cảm biến và các thuật toán phổ biến trong lập trình điều khiển robot.
>
> ROS giúp người dùng có thể dễ dàng kết nối các máy tính ở trên robot (Raspberry pi, Jetson Nano, các loại máy tính nhúng, mini computer, …) với laptop để điều khiển hoặc thao tác từ xa

<img src="assets/do-an-cdt/media/image19.jpeg" style="width:5.72489in;height:3.88333in" alt="Diagram Description automatically generated" />

> <span id="_bookmark28" class="anchor"></span>_Hình 2.9: ROS kết nối_
>
> Camera sẽ thu thập dữ liệu từ môi trường, thông qua Camera Node gửi tới Master, master sẽ chứa toàn bộ thông tin của hệ thống và giao tiếp với các node khác.
>
> ROS giúp đơn giản và tiết kiệm thời gian việc lập trình các hành vi phức tạp của robot. ROS như là một mạng lưới điểm (node) được kết nối bởi nhiều node mà mỗi node có nhiệm vụ riêng tương ứng với các thành phần cấu tạo nên robot. Mỗi node riêng có thể được tùy chỉnh phát triển và lập trình theo ý tưởng
>
> của người phát triển mà không cần quan tâm đến việc phải thống nhất sử dụng cùng một ngôn ngữ lập trình, điều đó có nghĩa là node này bạn phát triển trên ngôn ngữ C++ nhưng node khác bạn có thể phát triển trên ngôn ngữ Python. Python và C++ là hai ngôn ngữ nền tảng mà bạn cần phải học trước khi làm quen với ROS.
>
> ROS chạy trên nền Ubuntu, do đó bạn phải cài ROS trên nền Ubuntu. Hiện tại có hai phiên bản phổ biến là ROS Melodic và ROS Kinetic, phiên bản Melodic tương thích và chạy trên Ubuntu 18 trong khi đó Kinetic chạy trên nền Ubuntu 16. Ngoài ra còn có ROS Noetic cho bản Ubuntu 20. Các bạn có thể dễ dàng cài đặt ROS theo hướng dẫn trên trang chủ của ROS.
>
> ROS bao gồm các cấu thành bởi các thành phần như hình sau:

<img src="assets/do-an-cdt/media/image20.jpeg" style="width:5.06667in;height:3.13333in" alt="Diagram Description automatically generated" />

> <span id="_bookmark29" class="anchor"></span>_Hình 2.10: Thành phần của ROS_

- **Nodes**: là đơn vị cơ bản nhằm hỗ trợ giao tiếp với các thành phần cấu thành nên robot. Vì dụ như một con robot thường có các node như Laser scanner, Camera, Node gửi vận tốc đến thiết bị điều khiển động cơ. Các nodes này có thể giao tiếp và tương tác với nhau qua Master.

- **Master**: đóng vai trò kết nối các node với nhau. Do đó, master luôn được khởi động đầu tiên bằng cầu lệnh roscore sau đó thì bạn có thể gọi bất kỳ các node nào trong hệ thống. Sau khi gọi xong, các node có thể kết nối và tương tác với nhau.

- **Parameter Server**: Là một cấu trúc nhiều tham số có thể truy cập trong lúc chạy ROS. Các node sử dụng cấu trúc này nhằm lưu trữ và truy xuất các thông số trong thời gian chạy. Do nó không có hiệu suất cao nên thường dùng với kiểu dữ liệu tĩnh, chẳng hạn như các thông số cấu hình, thời gian hệ thống.

- **Message**: Đây là cấu trúc dữ liệu được các node sử dụng để trao đổi với nhau tương tự như các kiểu dữ liệu double, int trong các ngôn ngữ lập trình. Các node tương tác với nhau bằng cách send và receive ROS message.

- **Topics**: là phương pháp giao tiếp trao đổi dữ liệu giữa hai node, nó bao gồm nhiều cấp bậc thông tin mà chúng có thể giao tiếp thông qua ROS message. Hai phương thức trong topic bao gồm publish và subscribe.

<!-- -->

- publish là đăng kí gửi thông tin

- subscribe là đăng ký nhận thông tin

<!-- -->

- **Services**: Là một giao tiếp trao đổi dữ liệu/ thông tin giữa hai node thông qua phương thức request và response. Thường được áp dụng trong trường hợp việc thực hiện một lệnh cần nhiều thời gian xử lý nên dữ liệu tính toán được lưu ở server và sẽ dùng khi cần xử lý.

- **Bags**: là một định dạng tệp trong ROS dùng để lưu trữ dữ liệu message với phần mở rộng là _.bag_ có vai trò quan trọng và có thể được xử lý, ph

> ROS phát triển nhiều packages và meta packages ứng dụng cho xe tự hành, chẳng hạn như Navigation stack, ROS Gmapping, Ros_Industrial và perception_pcl…

- Navigation stack: mục đích chính của Navigation package là để di chuyển robot từ vị trí bắt đầu đến một vị trí đích mong muốn mà không gặp bất kỳ sự cản trở nào từ môi trường. ROS Navigation package đem đến sự bổ xung của nhiều thuật toán định vị liên quan giúp dễ dàng thực hiện định vị trong robot di động.

- ROS Gmapping: ROS Gmapping package chứa một node là slam_gmapping, giúp tạo ra lưới bản đồ 2D từ cảm biến laser và vị trí của robot.

- ROS-Industrial: cơ bản mở rộng các tính năng của ROS tới ngành công nghiệp robot, cái mà đang làm việc trong quá trình tạo ra sản phẩm. ROSIndustrial bao gồm nhiều gói phần mềm sử dụng để tương tác với robot công nghiệp.

- Perception_pcl: là một giao diện ROS cho thự viện PCL ( Point Cloud Library). Nó chứa các gói cho việc bơm dữ liệu điểm đám mây từ nhiều cảm biến khác nhau.

<a id="xây-dựng-mô-hình-hệ-thống"></a>

## Xây dựng mô hình hệ thống

1.  **Mô hình động học**

> Mô hình thiết kế robot lễ tân được mô tả như hình sau:

<img src="assets/do-an-cdt/media/image21.png" style="width:4.30191in;height:4.12687in" />

> <span id="_bookmark31" class="anchor"></span>_Hình 2.11: Mô hình robot_
>
> Trong đó:

<table style="width:65%;">
<colgroup>
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>1. Bánh xe dẫn động</p>
</blockquote></th>
<th style="text-align: right;">4. Khung robot</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>2. Cơ cấu truyền chuyển động</p>
</blockquote></td>
<td style="text-align: right;">5. Động cơ DC</td>
</tr>
</tbody>
</table>

<table style="width:67%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>3. Bánh xe phụ</p>
</blockquote></th>
<th><blockquote>
<p>6. Trục dẫn động</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> _a, Phương trình động học thuận_
>
> Phương trình động học được thiết lập dựa trên mô hình robot di động hệ vi sai với tốc độ bánh trái và tốc độ bánh phải lần lượt là 𝑉𝑙 và 𝑉𝑟

<img src="assets/do-an-cdt/media/image22.png" style="width:5.60409in;height:4.07917in" />

> <span id="_bookmark32" class="anchor"></span>_Hình 2.12: Mô hình robot và các thông số động học_
>
> Trong đó:

<table style="width:98%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 11%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Kí hiệu</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Đơn vị</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Ý nghĩa</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><blockquote>
<p>R</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Bán kính bánh xe.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>r</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Bán kính đường cong tạo bởi tốc độ quay của robot (tính đến tâm A).</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2L</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Khoảng cách 2 bánh dẫn.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:98%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 11%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p>𝜑𝑟, 𝜑𝑙</p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p>rad</p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p>Góc quay bánh xe phải, trái quay quanh trục.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><blockquote>
<p>𝜃</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>rad</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Góc nghiêng của thân robot.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>𝜑̇𝑟, 𝜑̇𝑙</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>rad/s</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Vận tốc quay bánh phải, trái.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>𝜃̇ = 𝜔</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>rad/s</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Vận tốc quay của robot.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>𝑉𝑎</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m/s</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Vận tốc dài của robot.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>r + L</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Bán kính đường cong tính đến bánh phải.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>r - L</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>m</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Bán kính đường cong tính đến bánh trái.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>mc = M</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>kg</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Khối lượng thân robot.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>mw</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>kg</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Khối lượng bánh xe + động cơ.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>1</p>
<p>𝐼𝑐 = 𝐽 = 𝑚𝑐(𝑎<sup>2</sup> + 𝑏<sup>2</sup>)</p>
<p>12</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>kg.m<sup>2</sup></p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Momen quán tính của robot về trục thẳng đứng qua tâm khối lượng.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote>
<p>𝐼𝑤 = 𝑚𝑤𝑟<sup>2</sup></p>
<blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>kg.m<sup>2</sup></p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Momen quán tính của mỗi động cơ về trục bánh xe.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Im</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>kg.m<sup>2</sup></p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Momen quán tính của mỗi động cơ về trục xe.</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Xét trong hệ tọa độ cố định XIYI và hệ tọa độ khung robot XrYr :

- Vận tốc bánh xe trái và phải:

<table style="width:66%;">
<colgroup>
<col style="width: 42%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑉𝑟 = 𝑅. 𝜑̇𝑟 = 𝑉𝑎 + 𝐿. 𝜃̇</p>
<p>{</p>
<p>𝑉𝑙 = 𝑅. 𝜑̇𝑙 = 𝑉𝑎 − 𝐿. 𝜃̇</p>
</blockquote></th>
<th style="text-align: right;">( 2-1 )</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Vận tốc tại điểm A:

𝑎

> \+ Ta có :

<table style="width:72%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑉𝑟 + 𝑉𝑙 (𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>𝑥̇<sup>𝑟</sup> = 𝑉 = = 𝑅.</p>
<p>𝑎 𝑎 2 2</p>
</blockquote></th>
<th style="text-align: right;">( 2-2 )</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>𝑉𝑟 − 𝑉𝑙 (𝜑̇𝑟 − 𝜑̇𝑙)</p>
<p>𝜔 = 𝜃̇ = = 𝑅.</p>
<p>2𝐿 2𝐿</p>
</blockquote></td>
<td style="text-align: right;">( 2-3 )</td>
</tr>
</tbody>
</table>

- Vận tốc robot trong hệ tọa độ khung robot chính là vận tốc của điểm A:

<table style="width:72%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑉𝑟 + 𝑉𝑙 (𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>𝑥̇<sup>𝑟</sup> = = 𝑅.</p>
<p><sup>𝑎</sup> 2 2</p>
<p>𝑦̇<sup>𝑟</sup> = 0</p>
</blockquote>
<p>𝑎</p>
<blockquote>
<p>𝑉𝑟 − 𝑉𝑙 (𝜑̇𝑟 − 𝜑̇𝑙)</p>
<p>{𝜃̇ = 𝜔 = 2𝐿 = 𝑅. 2𝐿</p>
</blockquote></th>
<th><blockquote>
<p>( 2-4 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Vận tốc của robot trong hệ tọa độ cố định: Chiếu 𝑉<sub>𝑎</sub> lên hệ tọa độ cố định XIYI ta được:

<table style="width:61%;">
<colgroup>
<col style="width: 35%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑥̇<sup>𝐼</sup> = 𝑉 . 𝑐𝑜𝑠𝜃</p>
<p>{ 𝑎 𝑎</p>
<p>𝑦̇<sup>𝐼</sup> = 𝑉 . 𝑐𝑜𝑠𝜃</p>
<p>𝑎 𝑎</p>
</blockquote></th>
<th style="text-align: right;">( 2-5 )</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Thay (2-2) vào (2-5) ta được:

<table style="width:68%;">
<colgroup>
<col style="width: 45%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>(𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>𝑥̇<sup>𝐼</sup> = 𝑅. . cos 𝜃</p>
<p>𝑎</p>
<p>{ 2</p>
<p>(𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>𝑦̇<sup>𝐼</sup> = 𝑅. . sin 𝜃</p>
<p>𝑎 2</p>
</blockquote></th>
<th><blockquote>
<p>( 2-6 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Ta có: 𝑉 − 𝑉 = 2𝐿𝜃̇ ⇔ 𝜃̇ = <u>𝑉𝑟−𝑉𝑙</u> = 𝑅. <u>(𝜑̇𝑟−𝜑̇𝑙)</u>

𝑟 𝑙

2𝐿

> 2𝐿
>
> Ta có mô hình động học:

<table style="width:68%;">
<colgroup>
<col style="width: 45%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>(𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>⎛𝑥̇<sup>𝐼</sup> = 𝑅. . cos 𝜃</p>
<p>𝑎</p>
<p>⎪ 2</p>
<p>(𝜑̇𝑟 + 𝜑̇𝑙)</p>
<p>𝑦̇<sup>𝐼</sup> = 𝑅. . sin 𝜃</p>
<p>⎨ <sup>𝑎</sup> 2</p>
<p>⎪ (𝜑̇𝑟 − 𝜑̇𝑙)</p>
<p>{ 𝜃̇ = 𝑅. 2𝐿</p>
</blockquote></th>
<th><blockquote>
<p>( 2-7 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Phương trình động học thuận:

<table style="width:74%;">
<colgroup>
<col style="width: 55%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑅 𝑅</p>
<p>⎡ . cos(𝜃) . cos (𝜃)⎤</p>
<p>𝑥̇ ⎢2 2 ⎥</p>
<p>[𝑦̇] = ⎢𝑅 . sin(𝜃) 𝑅 . sin (𝜃)⎥ [𝜑̇𝑟]</p>
<p>𝜃̇ ⎢2 2 ⎥ 𝜑̇𝑙</p>
<p>⎢ 𝑅 𝑅 ⎥</p>
<p>[ 2𝐿 − 2𝐿 ]</p>
</blockquote></th>
<th><blockquote>
<p>( 2-8 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

⇔ 𝑝̇ = 𝐽. 𝑞̇

> _b, Phương trình động học nghịch_
>
> Với các thông số đã có ở phần trước ta có phương trình động học nghịch của robot

- Mô hình động học nghịch:

𝑝̇

𝑞̇ = <img src="assets/do-an-cdt/media/image23.png" style="width:0.10333in" />

𝐽

<table style="width:75%;">
<colgroup>
<col style="width: 56%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>cos (𝜃) sin (𝜃) 𝐿 𝑥̇</p>
<p>[𝜑̇𝑟] = [ 𝑅 𝑅 𝑅] [𝑦̇]</p>
<p>𝜑̇<sub>𝑙</sub> cos (𝜃) sin (𝜃) 𝐿</p>
<p>− 𝜃̇</p>
<p>𝑅 𝑅 𝑅</p>
</blockquote></th>
<th><blockquote>
<p>( 2-9 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  **Mô hình động lực học**

> <img src="assets/do-an-cdt/media/image24.png" style="width:5.60307in;height:4.07917in" />
>
> <span id="_bookmark33" class="anchor"></span>_Hình 2.13: Mô hình robot và các thông số động lực học_
>
> Phương trình động học của một hệ robot di động với hệ tọa độ tổng quát \[q1, q2,…, qn\] được viết:

<table style="width:83%;">
<colgroup>
<col style="width: 67%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"><p><em>T</em> λ</p>
<blockquote>
<p><img src="assets/do-an-cdt/media/image25.png" /><em>M</em> (<em>q</em>)<em>q</em> + <em>V</em> (<em>q</em>, <em>q</em>)<em>q</em> + <em>F</em> (<em>q</em>) + <em>G</em>(<em>q</em>) + τ<em>d</em> = <em>B</em>(<em>q</em>)τ − Λ (<em>q</em>)</p>
</blockquote></th>
<th><blockquote>
<p>( 2-10 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Trong đó:
  - M(q) là một ma trận hệ số cho các đại lượng gia tốc;

  - 𝑉(𝑞, 𝑞̇) là một ma trận hệ số cho các đại lượng vận tốc;

  - 𝐹(𝑞̇) là ma trận hệ số ma sát bề mặt;

  - G(q) là vector trọng trường;

  - 𝜏𝑑 là vector giới hạn thành phần không xác định;

  - B(q) là ma trận các đại lượng đầu vào;

  - 𝜏 là các đại lượng đầu vào;

  - 𝚲<sup>𝑇</sup>(𝑞) là ma trận liên quan tới các hạn chế chuyển động;

  - 𝜆 là vector số nhân Lagrange.

- Phương pháp Lagrange được sử dụng để rút ra các phương trình động lực học bằng cách xem xét động năng và thế năng của hệ thống nhất định.

- Động lực học Lagrange :

<table style="width:72%;">
<colgroup>
<col style="width: 49%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑑 𝜕𝐿 𝜕𝐿</p>
<p>( ) + ( ) = 𝐹 − 𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup></p>
<p>𝑑𝑡 𝜕𝑞̇𝑖 𝜕𝑞𝑖</p>
</blockquote></th>
<th><blockquote>
<p>( 2-11 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Trong đó :
  - L = T-V là hàm Lagrangian đặc trưng cho các thành phần động học như T là động năng của hệ thống hay U là thế năng của hệ thống

  - T là động năng của hệ thống

  - qi là tọa độ tổng quát của hệ thống

  - F là vectơ lực tổng quát

  - 𝚲 là ma trận ràng buộc

  - 𝜆 là vectơ của hệ số nhân Lagrange liên kết với các ràng buộc.

> Việc đầu tiên để tìm ra được mô hình động lực học là phải tìm ra được động năng và thế năng chi phối chuyển động của hệ thống. Mà do robot chỉ di chuyển trên một mặt phẳng nên thế năng bằng 0.
>
> Động năng của hệ thống bằng tổng động năng của bản thân robot khi không có bánh với động năng của bánh xe và thiết bị truyền động (ở đây là động cơ DC)

<table style="width:73%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑇 = 𝑇𝑐 + 𝑇𝑤 = 𝑇𝑐 + 𝑇𝑤𝑟 + 𝑇𝑤𝑙</p>
</blockquote></th>
<th><blockquote>
<p>( 2-12 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Động năng của bản thân robot:

<table style="width:66%;">
<colgroup>
<col style="width: 41%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>1 1</p>
<p>𝑇𝐶 = 𝑚𝑐𝑉<sup>2</sup> + 𝐼𝑐𝜃̇2</p>
<p>2 <sup>𝑐</sup> 2</p>
</blockquote></th>
<th><blockquote>
<p>( 2-13 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Động năng tại 2 bánh bằng động năng của bánh và thiết bị truyền động:

<table style="width:72%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>1 1 1</p>
</blockquote>
<p>𝑇𝑟 = 𝑚𝑤𝑉<sup>2</sup> + 𝐼 𝜃̇2 + 𝐼 𝜑̇<sup>2</sup></p>
<p>2 𝑤𝑟 2 𝑚 2 𝑤 𝑟</p></th>
<th style="text-align: right;">( 2-14 )</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>1 1 1</p>
</blockquote>
<p>𝑇𝑙 = 𝑚𝑤𝑉<sup>2</sup> + 𝐼 𝜃̇2 + 𝐼𝑤𝜑̇<sup>2</sup></p>
<p>2 𝑤𝑙 2 𝑚 2 𝑙</p></td>
<td style="text-align: right;">( 2-15 )</td>
</tr>
</tbody>
</table>

- Phương trình vận tốc chung:

<table style="width:61%;">
<colgroup>
<col style="width: 34%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p>𝑉<sup>2</sup> = 𝑥̇<sup>2</sup> + 𝑦̇<sup>2</sup></p>
<p>𝑖 𝑖 𝑖</p></th>
<th style="text-align: right;">( 2-16 )</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Với:

<table style="width:65%;">
<colgroup>
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>{𝑥𝑐 = 𝑥𝑎 + 𝑑𝑐𝑜𝑠(𝜃)</p>
<p>𝑦𝑐 = 𝑦𝑎 + 𝑑𝑠𝑖𝑛(𝜃)</p>
</blockquote></th>
<th style="text-align: right;">( 2-17 )</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>{𝑥𝑤𝑟 = 𝑥𝑎 + 𝐿𝑠𝑖𝑛(𝜃)</p>
<p>𝑦𝑤𝑟 = 𝑦𝑎 − 𝐿𝑐𝑜𝑠(𝜃)</p>
</blockquote></td>
<td style="text-align: right;">( 2-18 )</td>
</tr>
<tr>
<td><blockquote>
<p>{𝑥𝑤𝑙 = 𝑥𝑎 − 𝐿𝑠𝑖𝑛(𝜃)</p>
<p>𝑦𝑤𝑙 = 𝑦𝑎 + 𝐿𝑐𝑜𝑠(𝜃)</p>
</blockquote></td>
<td style="text-align: right;">( 2-19 )</td>
</tr>
</tbody>
</table>

> Thay phương trình (2-17), (2-18), và (2-19) vào phương trình (2-14), (2-15) và (2-16) ta được phương trình động năng của hệ thống như sau:

<table style="width:94%;">
<colgroup>
<col style="width: 83%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>1 1 1</p>
<p>𝑇 = 𝑚(𝑥̇<sup>2</sup> + 𝑦̇<sup>2</sup>) − 𝑚 𝑑𝜃̇(𝑦̇ 𝑐𝑜𝑠𝜃 − 𝑥̇ 𝑠𝑖𝑛𝜃) + 𝐼 (𝜑̇<sup>2</sup> + 𝜑̇<sup>2</sup>) + 𝐼𝜃̇</p>
<p>2 𝑎 𝑎 𝑐 𝑎 𝑎 2 𝑤 𝑟 𝑙 2</p>
</blockquote></th>
<th><blockquote>
<p>( 2-20 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Với:
>
> 𝑚 = (𝑚𝑐 + 2𝑚𝑤) là khối lượng của hệ thống tính bằng tổng khối lượng của bản thân xe và khối lượng của 2 bánh xe.

<table style="width:71%;">
<colgroup>
<col style="width: 49%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝐼 = 𝐼𝑐 + 𝑚𝑐𝑑<sup>2</sup> + 2𝑚𝑤𝐿<sup>2</sup> + 2𝐼𝑚</p>
</blockquote></th>
<th><blockquote>
<p>( 2-21 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 𝐼𝑐 là momen quán tính của robot về trục thẳng đứng qua tâm khối lượng
>
> 𝐼𝑚 là momen quán tính của mỗi động cơ về trục xe
>
> 𝐼𝑤 là momen quán tính của mỗi động cơ về trục bánh xe Sử dụng phương trình (3) với L = T ta được:

<table style="width:79%;">
<colgroup>
<col style="width: 57%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p>𝑚𝑥̈𝑎 − 𝑚𝑑𝜃̈𝑠𝑖𝑛𝜃 − 𝑚𝑑𝜃̇<sup>2</sup>𝑐𝑜𝑠𝜃 = 𝐶1</p>
<p>𝑚𝑦̈𝑎 − 𝑚𝑑𝜃̈𝑐𝑜𝑠𝜃 − 𝑚𝑑𝜃̇<sup>2</sup>𝑠𝑖𝑛𝜃 = 𝐶2</p>
<p>𝐼𝜃̈ − 𝑚𝑑𝑥̈𝑎𝑠𝑖𝑛𝜃 + 𝑚𝑑𝑦̈𝑎𝑐𝑜𝑠𝜃 = 𝐶3</p>
<p>𝐼𝑤𝜑̈𝑟 = 𝜏𝑟 + 𝐶4</p>
<p>{ 𝐼𝑤𝜑̈𝑙 = 𝜏𝑙 + 𝐶5</p></th>
<th><blockquote>
<p>( 2-22 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Trong đó C1, C2, C3, C4 và C5 là các hệ số liên quan đến các hạn chế trong động học được giới thiệu trong phương trình (2-10).
>
> Ta thay hệ phương trình (2-22) vào phương trình (2-10) ta được:

<table style="width:75%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑀(𝑞)𝑞̈ + 𝑉(𝑞, 𝑞̇)𝑞̇ = 𝐵(𝑞)𝜏 − 𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup></p>
</blockquote></th>
<th><blockquote>
<p>( 2-23 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Trong đó:

<table style="width:84%;">
<colgroup>
<col style="width: 68%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"><blockquote>
<p>𝑚 0 −𝑚𝑑𝑠𝑖𝑛𝜃 0 0</p>
</blockquote>
<p>⎡ 0 𝑚 𝑚𝑑𝑐𝑜𝑠𝜃 0 0 ⎤</p>
<p>𝑀(𝑞) = ⎢−𝑚𝑑𝑠𝑖𝑛𝜃 𝑚𝑑𝑐𝑜𝑠𝜃 𝐼 0 0 ⎥</p>
<blockquote>
<p>⎢ ⎥</p>
<p>⎢ 0 0 0 𝐼𝑤 0 ⎥</p>
<p>[ 0 0 0 0 𝐼𝑤]</p>
</blockquote></th>
<th>( 2-24 )</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: right;"><p>⎡0 −𝑚𝑑𝜃̇𝑐𝑜𝑠𝜃 0 0 0⎤</p>
<p>⎢0 −𝑚𝑑𝜃̇𝑠𝑖𝑛𝜃 0 0 0⎥</p>
<p>𝑉(𝑞, 𝑞̇) = ⎢0 0 𝐼 0 0⎥</p>
<blockquote>
<p>⎢0 0 0 0 0⎥</p>
<p>[0 0 0 0 0]</p>
</blockquote></td>
<td>( 2-25 )</td>
</tr>
</tbody>
</table>

𝐵(𝑞) =

> 0 0
>
> ⎡0 0⎤
>
> 0 0
>
> ⎢1 0⎥
>
> \[0 1\]

<table style="width:72%;">
<colgroup>
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>−𝑠𝑖𝑛𝜃 𝑐𝑜𝑠𝜃 𝑐𝑜𝑠𝜃</p>
<p>⎡ 𝑐𝑜𝑠𝜃 𝑠𝑖𝑛𝜃 𝑠𝑖𝑛𝜃⎤</p>
<p>𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup> = 0 0 0</p>
<p>⎢ 0 0 0 ⎥</p>
<p>[ 0 0 0 ]</p>
</blockquote></th>
<th><blockquote>
<p>( 2-26 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Để thuận tiện cho mục đích điều khiển và mô phỏng ta loại bỏ các hạn chế trong
>
> chuyển động ngắn bớt:
>
> Λ*<sup>T</sup>* (_q_)λ . Điều này được thực hiện bằng cách xác định vecto được làm

<table style="width:58%;">
<colgroup>
<col style="width: 30%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝜂 = [𝜑̇𝑟]</p>
<p>𝜑̇𝑙</p>
</blockquote></th>
<th style="text-align: right;">( 2-27 )</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Ta biểu thị ma trận vận tốc bằng phương trình động học:

<table style="width:75%;">
<colgroup>
<col style="width: 55%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑅 𝑅</p>
<p>⎡ . cos(𝜃) . cos (𝜃)⎤</p>
<p>𝑥̇𝑎 ⎢2 2 ⎥</p>
<p>⎡𝑦̇𝑎 ⎤ ⎢ 𝑅 . sin(𝜃) 𝑅 . sin (𝜃) ⎥</p>
<p>⎢ ⎥ 1 𝜑̇𝑟</p>
<p>⎢ 𝜃̇ ⎥ = 2 ⎢ 2 𝑅 2 𝑅 ⎥ [𝜑̇ ]</p>
<p>⎢𝜑̇𝑟⎥ ⎢ − ⎥ 𝑙</p>
<p>[𝜑̇ ] ⎢ 2𝐿 2𝐿 ⎥</p>
</blockquote>
<p>𝑙 ⎢ 2 0 ⎥</p>
<p>[ 0 2 ]</p></th>
<th><blockquote>
<p>( 2-28 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Phương trình (2-28) có thể viết thành:

<table style="width:59%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑞̇ = 𝑆(𝑞)𝜂</p>
</blockquote></th>
<th style="text-align: right;">( 2-29 )</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Có thể chứng minh rằng ma trận biến đổi S(q) là không xác định trong không gian với các hạn chế 𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup> do đó ta có:

<table style="width:63%;">
<colgroup>
<col style="width: 36%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑆<sup>𝑇</sup>(𝑞)𝚲<sup>𝑇</sup>(𝑞) = 0</p>
</blockquote></th>
<th><blockquote>
<p>( 2-30 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Đạo hàm theo thời gian phương trình (2-29) ta được:

<table style="width:65%;">
<colgroup>
<col style="width: 39%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑞̈ = 𝑆̇(𝑞)𝜂 + 𝑆(𝑞)𝜂̇</p>
</blockquote></th>
<th><blockquote>
<p>( 2-31 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Thay phương trình (2-29) và (2-31) vào (2-23) ta được:

<table style="width:88%;">
<colgroup>
<col style="width: 74%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑀(𝑞)[𝑆̇(𝑞)𝜂 + 𝑆(𝑞)𝜂̇] + 𝑉(𝑞, 𝑞̇)[𝑆(𝑞)𝜂] = 𝐵(𝑞)𝜏 − 𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup></p>
</blockquote></th>
<th><blockquote>
<p>( 2-32 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Nhân cả 2 vế với 𝑆<sup>𝑇</sup>(𝑞) ta được:
>
> 𝑆<sup>𝑇</sup>(𝑞)𝑀(𝑞)\[𝑆̇(𝑞)𝜂 + 𝑆(𝑞)𝜂̇\] + 𝑉(𝑞, 𝑞̇)\[𝑆(𝑞)𝜂\] = 𝑆<sup>𝑇</sup>(𝑞)𝐵(𝑞)𝜏 − 𝑆<sup>𝑇</sup>(𝑞)𝚲<sup>𝑇</sup>(𝑞)<sup>𝜆</sup>
>
> Như phương trình (2-30) 𝑆<sup>𝑇</sup>(𝑞)𝚲<sup>𝑇</sup>(𝑞) = 0 do đó ta có:
>
> ⎡𝐼𝑤 +
>
> 𝑆<sup>𝑇</sup>(𝑞)𝑀(𝑞)𝑆(𝑞) = ⎢
>
> 𝑟2
>
> 4𝑏<sup>2</sup>
>
> (𝑚𝑏<sup>2</sup> + 𝐼)
>
> 𝑟2
>
> 4𝑏<sup>2</sup>

(𝑚𝑏<sup>2</sup> − 𝐼) ⎤

⎥

\]

\[ 4𝑏<sup>2</sup>

> (𝑚𝑏<sup>2</sup> − 𝐼) 𝐼𝑤 +
>
> 𝑟2
>
> 4𝑏<sup>2</sup>
>
> (𝑚𝑏<sup>2</sup> − 𝐼)⎥

𝑟2

> ⎡ 0 2𝑏 𝑚𝑐𝑑𝜃̇⎤

𝑆<sup>𝑇</sup>(𝑞)\[𝑀(𝑞)𝑆̇(𝑞) + 𝑉(𝑞, 𝑞̇)𝑆(𝑞)\] = ⎢

⎢

> ⎥
>
> 𝑟2 ⎥
>
> \[− 2𝑏 𝑚𝑐𝑑𝜃̇ 0 \]

𝑆<sup>𝑇</sup>(𝑞)𝐵(𝑞) = \[1 0\]

> 0 1
>
> − **Do đó ta có phương trình động lực học Lagrange:**

<table style="width:92%;">
<colgroup>
<col style="width: 80%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p>2𝐼𝑤 1</p>
</blockquote>
<p>(𝑚𝑐 + 2𝑚𝑤 + ) 𝑉̇ − 𝑚𝑐𝑑𝜔<sup>2</sup> = (𝜏𝑟 + 𝜏𝑙)</p>
<blockquote>
<p>𝑅<sup>2</sup> 𝑅</p>
<p>2𝐿<sup>2</sup> 𝐿</p>
</blockquote>
<p>(𝐼𝑐 + 𝑚𝑐𝑑<sup>2</sup> + 2𝑚𝑤𝐿<sup>2</sup> + 2𝐼𝑚 + 𝐼𝑤) 𝜔̇ + 𝑚𝑐𝑑𝜔𝑉 = (𝜏𝑟 − 𝜏𝑙)</p>
<p>{ 𝑅<sup>2</sup> 𝑅</p></th>
<th><blockquote>
<p>( 2-33 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 𝑅(𝜏𝑟 + 𝜏𝑙) + 𝑅<sup>2</sup>𝑚𝑐𝑑𝜔<sup>2</sup> 𝜏𝑟 + 𝜏𝑙 + 𝑅𝑚𝑐𝑑𝜔<sup>2</sup>
>
> ⎛ 𝑉̇ =
>
> ⎪
>
> ⇔
>
> 𝑅<sup>2</sup>(𝑚𝑐
>
> \+ 2𝑚𝑤

) + 2𝐼𝑤

> =
>
> 𝑅(𝑚𝑐 + 2𝑚𝑤) +
>
> <u>2𝐼</u>𝑤
>
> 𝑅
>
> ⎨ 𝑅𝐿(𝜏𝑟 − 𝜏𝑙) − 𝑅<sup>2</sup>𝑚𝑐𝑑𝜔𝑉
>
> 𝐿(𝜏𝑟 − 𝜏𝑙) − 𝑅𝑚𝑐𝑑𝜔𝑉
>
> ⎪𝜔̇ = (𝐼
>
> \+ 𝑚
>
> 𝑑<sup>2</sup> + 2𝑚
>
> 𝐿<sup>2</sup> + 2𝐼
>
> )𝑅<sup>2</sup> + 2𝐿<sup>2</sup>𝐼 =
>
> 2𝐿2𝐼
>
> 𝑐 𝑐
>
> {
>
> 𝑤 𝑚
>
> 𝑤 (𝐼𝑐 + 𝑚𝑐𝑑<sup>2</sup> + 2𝑚𝑤𝐿<sup>2</sup> + 2𝐼𝑚)𝑅 + 𝑅 𝑤

<a id="chương-3-tính-toán-thiết-kế-hệ-thống"></a>

# CHƯƠNG 3: TÍNH TOÁN, THIẾT KẾ HỆ THỐNG

<a id="thiết-kế-sơ-đồ-tổng-thể-hệ-thống"></a>

## Thiết kế sơ đồ tổng thể hệ thống

1.  **Sơ đồ tổng thể hệ thống**

<img src="assets/do-an-cdt/media/image26.png" style="width:6.24839in;height:1.7675in" />

> <span id="_bookmark36" class="anchor"></span>_Hình 3.1: Sơ đồ khối hệ thống_

2.  **Chức năng của từng khối**
    - Khối nguồn: có nhiệm vụ cung cấp nguồn 1 chiều ổn định cho khối xử lý trung tâm hoạt động.

    - Khối cảm biến: gồm các thiết bị dùng để thu nhận các tín hiệu từ môi trường bên ngoài: cảm biến IMU giúp xác định góc quay của robot; cảm biến LiDAR có chức năng quét bản đồ, xác định hướng di chuyển kết hợp với cảm biến siêu âm giúp robot tránh vật cản cho robot.

    - Khối xử lý trung tâm: Raspberry Pi 4 dùng để nhận dữ liệu quét được từ LiDAR thông qua Rviz và hiển thị bản đồ trên màn hình, vi điều khiển STM32F407VET6 dùng để lập trình điều khiển robot di chuyển đúng ý muốn.

    - Khối động cơ: Có chức năng truyền động cho các bánh xe để robot di chuyển, gửi và nhận tín hiệu xung từ encoder.

    - Khối hiển thị: hiển thị trực tiếp trên màn hình máy tính.

<!-- -->

2.  <span id="_bookmark37" class="anchor"></span>**Tính toán, thiết kế hệ thống cơ khí**

<img src="assets/do-an-cdt/media/image27.jpeg" style="width:5.325in;height:6in" alt="A picture containing diagram Description automatically generated" />

> <span id="_bookmark38" class="anchor"></span>_Hình 3.2: Bản vẽ thiết kế hệ thống cơ khí của mô hình_
>
> Hình 4.2 và 4.3 là mô hình cơ khí của hệ thống robot di động phục vụ lễ tân. Các thành phần chính của hệ thống bao gồm: 1. Thân vỏ xe Mobile Robot, 2. Nắp xe, 3. Khung giá, 4. Khay dưới, 5. Gá chữ L, 6. Phần đáy xe, 8. Gá động cơ, 9. Bánh tự lựa,
>
> 10\. Động cơ Planet, 11. Bánh xe, 12. Gá chữ L, 13. Khay trên, 14. Gá màn hình, 15. Gá chữ L, 16. Lidar. Thiết kế chi tiết cho các cụm chi tiết chính được thể hiện trong phần phụ lục. Trong phần này, tính toán lựa chọn một số chi tiết chính trong phần cơ khí của Mô hình Mobile Robot được trình bày.
>
> <img src="assets/do-an-cdt/media/image28.jpeg" style="width:5.66491in;height:4.06667in" alt="Diagram, engineering drawing Description automatically generated" />
>
> <span id="_bookmark39" class="anchor"></span>_Hình 3.3: Các thành phần cơ bản của mô hình cơ khí_

1.  **Tính toán lựa chọn bánh xe**

> Bánh xe động lực: Bánh động lực cần phải chịu tải tốt, ma sát giữa bánh với mặt đất phải lớn để tránh bị trượt khi di chuyển gây ra sự không ổn định của xe trong quá trình làm việc. Dựa vào khối lượng các linh điện và khung xe trong quá trình làm việc nhóm chọn bánh động lực có kích thước như sau: Đường kính bánh xe 150mm, có phần khung làm từ nhựa đủ khả năng chịu tải tốt, đồng thời lớp vỏ ngoài là cao su chia làm các rãnh làm tăng ma sát.
>
> Bánh dẫn hướng: hay còn gọi là bánh xe tự lựa giúp robot điều chỉnh hướng đi. Quay trái, quay phải, linh hoạt hơn.
>
> <img src="assets/do-an-cdt/media/image29.jpeg" style="width:4.14535in;height:3.81958in" alt="A picture containing outdoor, curb Description automatically generated" />
>
> <span id="_bookmark40" class="anchor"></span>_Hình 3.4: Bánh xe dẫn động_

<img src="assets/do-an-cdt/media/image30.jpeg" style="width:3.96427in;height:3.40948in" />

> <span id="_bookmark41" class="anchor"></span>_Hình 3.5: Bánh xe dẫn hướng bị động_

2.  **Tính toán chọn động cơ**

> Địa hình làm việc của robot là địa hình phẳng, giả thiết bỏ qua sự biến dạng của bánh xe, bỏ qua lực cản của không khí trong quá trình robot di chuyển.
>
> Các thông số của robot:

- Khối lượng ước tính: M = 15 (kg).

- Khối lượng hàng hoá tối đa: 18 (kg).

- Chọn bánh xe có đường kính: 2r = 150 (mm).

- Chọn tốc độ tối đa là: 0,5 (m/s).

- Thông số cơ bản của bánh xe là: đường kính 150 (mm), bề rộng của bánh xe là 30 (mm), tải trọng tối đa 43 (kg).

> Phân tích lực tác động lên một bánh xe chủ động gồm 4 lực tác dụng như sau:

<img src="assets/do-an-cdt/media/image31.jpeg" style="width:3.59453in;height:1.6875in" />

> <span id="_bookmark42" class="anchor"></span>_Hình 3.6: Phân tích các lực tác dụng lên xe_
>
> Trong đó:

- 𝐹⃗𝑚𝑠𝑛 là lực ma sát nghỉ giữa bánh xe và bề mặt sàn.

- 𝐹⃗𝑤 là lực kéo sinh ra do momen động cơ.

- 𝑁⃗⃗ là phản lực của mặt sàn.

- 𝑃⃗<sub>1</sub> là một nửa trọng lực của xe (P1 = P/2).

- 𝑀⃗⃗<sub>1</sub> là momen xoắn cho động cơ.

- 𝑚<sub>1</sub> là một nửa tổng trọng lượng của robot và hàng (m1 = m/2).

> Chọn phương án chuyển động của robot là chuyển động thẳng, hai bánh dẫn động di chuyển cùng tốc độ về phía trước với 𝑣 = 0,5 (m/s). Tốc độ quay của bánh xe là:

𝑛 =

> 60 × 1000 × 𝑣
>
> 2𝜋𝑟
>
> 60 × 1000 × 0.5
>
> =
>
> 150𝜋
>
> = 63.69 (𝑟𝑝𝑚)
>
> Phương trình cân bằng lực:

<table style="width:68%;">
<colgroup>
<col style="width: 46%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝐹⃗𝑚𝑠𝑛 + 𝐹⃗𝑤 + 𝑁⃗⃗ + 𝑃⃗1 = 𝑚1𝑎⃗</p>
</blockquote></th>
<th><blockquote>
<p>( 3-1 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Với 𝑎⃗ là gia tốc của xe.
>
> **Khi xe chuyển động đều**
>
> Vận tốc không đổi 𝑣 = 0,5 (m/s) nên gia tốc a = 0 (m/s<sup>2</sup>). Khi đó:

<table style="width:77%;">
<colgroup>
<col style="width: 59%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑃<sub>1</sub> 𝑚<sub>1</sub>𝑔 42.2 × 9.8</p>
<p>𝑁 = = = = 206.7 (𝑁)</p>
<p>2 2 2</p>
</blockquote></th>
<th><blockquote>
<p>( 3-2 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Lực kéo sinh ra do momen của động cơ là:

<table style="width:79%;">
<colgroup>
<col style="width: 62%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝐹𝑤 = 𝐹𝑚𝑠𝑛 = 𝜇𝑙𝑁 = 0.015 × 206.7 = 3.1 (𝑁)</p>
</blockquote></th>
<th><blockquote>
<p>( 3-3 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Với hệ số ma sát lăn 𝜇𝑙 = 0.015 khi di chuyển trên sàn bê tông. Công suất cần thiết để xe di chuyển ổn định với vận tốc 0.5 (m/s) là:

<table style="width:74%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑃1 = 𝐹𝑤 × 𝑣 = 3.1 × 0.5 = 1.55 (𝑊)</p>
</blockquote></th>
<th><blockquote>
<p>( 3-4 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **Khi xe tăng tốc**
>
> Xe tăng tốc với gia tốc a = 0.5 (m/s<sup>2</sup>) để hàng không rơi. Lực kéo sinh ra do momen của động cơ là:

<table style="width:92%;">
<colgroup>
<col style="width: 82%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝐹𝑤 = 𝐹𝑚𝑠𝑛 + 𝑚1𝑎 = 𝜇𝑛𝑁 + 𝑚1𝑎 = 1 × 206.7 + 42 × 0.5 = 228 (𝑁)</p>
</blockquote></th>
<th><blockquote>
<p>( 3-5 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Với hệ số ma sát tĩnh 𝜇𝑛 = 1
>
> Momen xoắn cần thiết để xe tăng tốc là:

<table style="width:75%;">
<colgroup>
<col style="width: 57%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑀1 = 𝐹𝑤𝑟 = 228 × 0.035 = 7.98 (𝑁𝑚)</p>
</blockquote></th>
<th><blockquote>
<p>( 3-6 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Công suất cần thiết để tăng tốc lên 0.5 (m/s) là:

<table style="width:72%;">
<colgroup>
<col style="width: 52%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>𝑃1 = 𝐹𝑤𝑟 = 228 × 0.5 = 114 (𝑊)</p>
</blockquote></th>
<th><blockquote>
<p>( 3-7 )</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Như vậy, công suất động cơ cần thiết là 114W và tốc độ động cơ yêu cầu là 63rpm.
>
> Nên chọn động cơ giảm tốc với tốc độ 70rpm sử dụng điện áp 24V, công suất 120W.

<img src="assets/do-an-cdt/media/image32.jpeg" style="width:3.31289in;height:2.40156in" />

> <span id="_bookmark43" class="anchor"></span>_Hình 3.7: Động cơ giảm tốc planet_

<a id="tính-toán-thiết-kế-hệ-thống-điều-khiển"></a>

## Tính toán, thiết kế hệ thống điều khiển

1.  **Nguyên lý hệ thống điều khiển**

<img src="assets/do-an-cdt/media/image33.png" style="width:4.61723in;height:3.60156in" />

> <span id="_bookmark45" class="anchor"></span>_Hình 3.8: Sơ đồ tổng thể hệ thống điều khiển_
>
> Sơ đồ hệ thống điện có dạng như hình vẽ với thiết bị điều khiển chính là STM32. Các cảm biến đầu vào là cảm biến LiDAR, IMU. Các thiết bị đầu ra bao gồm loa âm thanh, màn hình HMI, driver và động cơ. Nguồn cấp là pin Lithium 24V giúp hệ thống duy trì hoạt động ổn định.

2.  **Thiết bị điều khiển và phần mềm lập trình**

> _a, Mạch điều khiển trung tâm_

<img src="assets/do-an-cdt/media/image34.png" style="width:5.83032in;height:4.10667in" alt="Shape Description automatically generated with low confidence" />

> <span id="_bookmark46" class="anchor"></span>_Hình 3.9: Sơ đồ khối hệ thống điều khiển trung tâm_
>
> Loại vi điều khiển được sử dụng là STM32F407VET6 do nhóm tự thiết kế và chế tạo. Vi điều khiển STM32F407VET6 là loại được sử dụng ở rất nhiều trường đại học hiện nay trong giảng dạy và nghiên cứu, vi điều khiển có thiết kế ra chân đầy đủ với các ngoại vi cơ bản: USB, MicroSD, Flash, Pin RTC...và cổng nạp chuẩn Jtag tích hợp. Bản vẽ nguyên lí chi tiết về mạch điều khiển được thế hiện ở phần Phụ lục.
>
> <img src="assets/do-an-cdt/media/image35.png" style="width:5.13433in;height:3.88167in" alt="Diagram, schematic Description automatically generated" />

<span id="_bookmark47" class="anchor"></span>_Hình 3.10: MCU STM32F407 thiết kế trên phần mềm Altium Designer_

<img src="assets/do-an-cdt/media/image36.jpeg" style="width:4.41994in;height:4.29in" alt="https://f7-zpcloud.zdn.vn/5952769752258911879/6dcdd983700ba955f01a.jpg" />

<span id="_bookmark48" class="anchor"></span>_Hình 3.11: Board mạch vi điều khiển STM32F407VET6_

> **Thông số kỹ thuật:**

- Vi điều khiển chính: STM32F407VET6 (32-bit RISC Cortex-M4 Kernel, 512kB Flash Storage, 192kBRAM + 4kBSRAM, LQFP100 Package).

- Nguồn cấp từ cổng Mini USB qua các IC nguồn chuyển thành 3v3 để cấp cho MCU.

- Có sẵn các chân nguồn: 3V và 5V.

- Thạch anh: 168MHz, 210 DMIPS/1.25 DMIPS/MHz.

- Điện áp hoạt động: 1.8-3.6V.

- Chuẩn truyền thông: 3 SPI, 2 UART, 4 USART, 3 I2C, 2 I2S, 1 FSMC, 1 SDIO, 2 CAN, LX, USB 2 controller FS/HS ( with DMA) HSULPII USB (DM USB for HS PHY).

- 1x 10/100 Ethernet MAC.

- 1x 8 to 12-bit parallel camera interface.

- 3x ADC (12, LUS, time 24), 2xDAC (12bit).

> _b, Phần mềm lập trình_
>
> STM32F407VET6 sử dụng phần mềm KielC V5. KeilC V5 là một trong những IDE tốt nhất hiện nay được các lập trình viên sử dụng để phát triển code cho dòng vi điều khiển lõi ARM do hãng ST phát hành.

<img src="assets/do-an-cdt/media/image37.jpeg" style="width:4.0211in;height:2.0625in" />

> <span id="_bookmark49" class="anchor"></span>_Hình 3.12: Giao diện phần mềm KeilC V5_
>
> _c, Driver Smart PID_

<img src="assets/do-an-cdt/media/image38.jpeg" style="width:4.37239in;height:3.28125in" alt="https://file.hstatic.net/1000292825/file/h1__4__e8f32055a5284b13bbafa24a061a7c52_grande.jpg" />

> <span id="_bookmark50" class="anchor"></span>_Hình 3.13: Drive Smart PID V4.0_
>
> Driver được trang bị bộ vi xử lý ARM hiện đại nhất nên cung cấp nhiều chức năng cao cấp như sau:

- Chạy động cơ công suất lớn tới 700W, điện áp điều khiển 24VDC.

- Giao tiếp máy tính qua cổng COM, UART.

- Đèn LED báo trạng thái hoạt động.

- Chạy PID vị trí theo chuẩn 1 xung và 1 hướng hỗ trợ tần số lên tới 10 MHz, ứng dụng làm máy CNC, với các thông sô Kp, Kd, Ki điều chỉnh được bằng giao diện máy tính.

- Chạy PID vị trí theo chuẩn xung encoder AB hỗ trợ tần số lên tới 10 MHz, ứng dụng làm cánh tay máy , với các thông sô Kp, Kd, Ki điều chỉnh được bằng giao diện máy tính.

- Chạy PID vận tốc hỗ trợ các chuẩn giao tiếp: 1 PWM (tích cực mức 0 với độ phân giải 8 bit) và 1 hướng, hỗ trợ tần số điều xung (50 Hz – 5 KHz).

- UART với khung truyền 3 byte (byte đầu là thuộc tính gồm chiều quay bit thứ 7 và các bit còn lại là địa chỉ, byte giữa là tốc độ, byte cuối luôn luôn là 0xFF). Hỗ trợ giao tiếp mọi tốc độ baudrate và tối đa lên đến 128 thiết bị mà chỉ tốn 1 dây điều khiển từ mater, có giao diện tùy chọn cho người sử dụng.

- Có chức năng thông minh là chỉ cần bạn nhập thông số tốc độ max của động cơ tính theo vòng/phút và xung encoder quay được 1 vòng thì bộ điều khiển sẽ tự tính toán ra hết các hệ số Kp, Kd, Ki.

- Hỗ trợ chạy động cơ lên tới 20000 vòng/phút và encoder 20000 xung/vòng.

- Chạy theo chuẩn cầu H đơn thuần không cần encoder, cũng có 3 chuẩn giao tiếp PWM, UART.

> _d, Module LM2596_
>
> Là module giảm áp có khả năng điều chỉnh được dòng ra đến 3A. LM2596 là IC nguồn tích hợp đầy đủ bên trong. Tức là khi cấp nguồn 9V vào module, sau khi giảm áp ta có thể lấp được nguồn 3A \< 9v... như 5V hay 3.3V.

<img src="assets/do-an-cdt/media/image39.jpeg" style="width:3.12813in;height:2.44635in" />

> <span id="_bookmark51" class="anchor"></span>_Hình 3.14: Module LM2596_
>
> **Thông số kỹ thuật:**

- Module nguồn không sử dụng cách ly.

- Nguồn đầu vào từ 4V - 35V.

- Nguồn đầu ra: 1V - 30V.

- Dòng ra Max: 3A.

- Kích thước mạch: 53mm x 26mm.

> _e, Động cơ giảm tốc_

<img src="assets/do-an-cdt/media/image40.jpeg" style="width:4.2622in;height:3.075in" />

> <span id="_bookmark52" class="anchor"></span>_Hình 3.15: Động cơ giảm tốc planet 24V_

- Tên sản Phẩm: Động cơ hộp số hành tinh - động cơ cho robocon Planet 24V.

- Hộp số động cơ dùng bánh răng vệ tinh nên rất bền bỉ yên tâm khi sử dụng.

- Thích hợp dùng trong các cơ cấu băng tải, robocon và 1 số chi tiết trong các loại máy công cụ, ô tô…

- Thông số kỹ thuật:
  - Động cơ servo DC 24V, 120W.

  - Điện áp cấp vào 24V, 468 vòng/phút.

  - Lực kéo 15kgf/cm.

  - Encoder 7 or 13 xung/vòng sử dụng nguồn 3.3v – 5volt.

  - Đường kính ngoài 42mm, đường kính trục 10mm.

  - Dòng khi có tải \< 6.5A.

<a id="lập-bản-đồ-sử-dụng-lidar"></a>

## Lập bản đồ sử dụng LiDAR

1.  **Cài đặt và thiết lập hệ thống**

> \- B1: Cài đặt hệ điều hành Ubuntu 20.04 LTS desktop cho Raspberry pi 4
>
> Ubuntu 20.04 LTS là phiên bản mới nhất mà **Canonical** đã phát hành vào cuối tháng 04/2020. Trong bản cập nhật này bổ sung thêm một số tính năng mới, sử dụng kernel 5.4, cải thiện độ ổn định hơn. Là phiên bản hỗ trợ ROS

<img src="assets/do-an-cdt/media/image41.jpeg" style="width:5.58883in;height:3.255in" alt="Graphical user interface Description automatically generated" />

> <span id="_bookmark54" class="anchor"></span>_Hình 3.16: Giao diện Ubuntu 20.04 LTS Desktop_

- B2: Cài phần mềm Gazebo và Rviz trên Ras pi

> Gazebo là một chương trình mô phỏng đa robot 3 chiều trong nhà và ngoài trời, hỗ trợ vật lý động học và động lực học nhiều phương tiện khác. Các trình cắm Gazebo giúp kết hợp ROS và Gazebo với nhau để hỗ trợ nhiều loại robot và cảm biến. Vì các trình cắm này biểu diễn cùng giao diện thông điệp với hệ thống ROS nên ra có thể viết các node của ROS hoàn toàn tương thích với bộ mô phỏng, dữ liệu ghi nhật lý và phần cứng, cũng như có thể phát triển ứng dụng rồi thử nghiệm cho robot trong môi trường thực tế
>
> <img src="assets/do-an-cdt/media/image42.jpeg" style="width:5.66977in;height:4.67417in" alt="Graphical user interface, website Description automatically generated" />

<span id="_bookmark55" class="anchor"></span>_Hình 3.17: Gazebo in ROS_

> \- B3: Mô phỏng quét bản đồ LIDAR trên Gazebo

<img src="assets/do-an-cdt/media/image43.png" style="width:6.18383in;height:0.30312in" /><img src="assets/do-an-cdt/media/image44.jpeg" style="width:5.46532in;height:3.07708in" alt="Text Description automatically generated" />

<span id="_bookmark56" class="anchor"></span>_Hình 3.18: Mô phỏng quét bản đồ nhờ cảm biến LiDAR_

> Kiểm tra dữ liệu /tf: rostopic echo /tf

<img src="assets/do-an-cdt/media/image45.png" style="width:4.76685in;height:4.07333in" alt="Text Description automatically generated" />

<span id="_bookmark57" class="anchor"></span>_Hình 3.19: Kết quả kiểm tra dữ liệu /tf_

> Kiểm tra dữ liệu /scan:

<img src="assets/do-an-cdt/media/image46.jpeg" style="width:5.93017in;height:3.33594in" alt="Text Description automatically generated" />

<span id="_bookmark58" class="anchor"></span>_Hình 3.20: Kết quả kiểm tra dữ liệu /scan_

> Kết quả sau khi cài đặt và thiết lập hệ thống:
>
> <img src="assets/do-an-cdt/media/image47.jpeg" style="width:5.80962in;height:3.4075in" alt="Graphical user interface, website Description automatically generated" />
>
> <span id="_bookmark59" class="anchor"></span>_Hình 3.21: Quét bản đồ thực sau khi cài đặt hệ thống_

1.  **Lập bản đồ sử dụng LiDAR**
    - Lưu đồ :

<img src="assets/do-an-cdt/media/image48.png" style="width:2.59586in;height:4.54844in" alt="Diagram Description automatically generated" />

> <span id="_bookmark60" class="anchor"></span>_Hình 3.22: Lưu đồ sử dụng lidar lập bản đồ_

2.  **Chuyển đổi dữ liệu từ LiDAR sang vi điều khiển STM32f1**
    - Lưu đồ thuật toán của cả hệ thống

<img src="assets/do-an-cdt/media/image49.jpeg" style="width:6.06622in;height:2.88187in" alt="Diagram Description automatically generated" />

> <span id="_bookmark61" class="anchor"></span>_Hình 3.23: Lưu đồ sử dụng Lidar lập bản đồ và điều khiển động cơ_
>
> \- Navigation package tổng hợp dữ liệu và xử lý trên raspberry pi

<img src="assets/do-an-cdt/media/image50.jpeg" style="width:6.10551in;height:2.725in" alt="Diagram Description automatically generated" />

> <span id="_bookmark62" class="anchor"></span>_Hình 3.24: Sơ đồ topic của bài toán navigation_
>
> Sơ đồ trên cho thấy tổng quan về cấu hình này. Các thành phần màu trắng là các thành phần bắt buộc đã được triển khai, các thành phần màu xám là các thành phần tùy chọn đã được triển khai và các thành phần màu xanh lam phải được tạo cho mỗi nền tảng robot. Các điều kiện tiên quyết của navigation stack, cùng với hướng dẫn về cách đáp ứng từng yêu cầu, được cung cấp bao gồm:

1.  ROS

2.  Transform Configuration

3.  Sensor Information (Sensor sourses)

4.  Odometry Information (Odometry source)

5.  Base Controller

6.  Mapping (map_server)

> _a, Transform Configuration (Chuyển đổi cấu trúc)_
>
> Xác định hai khung tọa độ : điểm trung tâm của đế robot(base_link) ; điểm trung tâm của Lidar (base_laser). Xác định khoảng cách ( tọa độ) giữa 2 base.
>
> Ví dụ như hình 3.8: Giả sử chúng ta biết rằng tia laze được gắn về phía trước 10 cm và cao hơn 20 cm so với tâm của đế di động. Điều này mang lại cho chúng tôi một độ lệch tịnh tiến liên quan đến khung "base_link" với khung "base_laser". Cụ thể, chúng tôi biết rằng để lấy dữ liệu từ khung "base_link" sang khung "base_laser", chúng tôi phải áp dụng phép dịch (x: 0,1m, y: 0,0m, z: 0,2m) và để lấy dữ liệu từ " khung base_laser" sang khung "base_link" chúng ta phải áp dụng phép dịch ngược lại (x: -0,1m, y: 0,0m, z: -0,20m).

<img src="assets/do-an-cdt/media/image51.png" style="width:6.20812in;height:1.3125in" alt="Chart Description automatically generated" /><img src="assets/do-an-cdt/media/image52.jpeg" style="width:6.05834in;height:1.46875in" alt="Diagram Description automatically generated" />

> <span id="_bookmark63" class="anchor"></span>_Hình 3.25: Ví dụ về khoảng cách giữa 2 khung tọa độ_
>
> Code trên terminal:

<img src="assets/do-an-cdt/media/image53.png" style="width:6.23773in;height:0.43271in" /><img src="assets/do-an-cdt/media/image54.png" style="width:6.13445in;height:0.27323in" />

> Bây giờ chúng ta đã có gói của mình, chúng ta cần tạo node thực hiện công việc biến đổi base_laser → base_link qua ROS. Trong gói robot_setup_tf vừa tạo, kích hoạt trình chỉnh sửa và dán đoạn mã sau vào tệp src/tf_broadcaster.cpp :

<img src="assets/do-an-cdt/media/image55.jpeg" style="width:6.1314in;height:3.18979in" alt="Graphical user interface, text, application, email Description automatically generated" />

> _b, Sensor Information (Nguồn cảm biến)_
>
> Nếu Navigation stack không có thông tin từ các cảm biến của robot thì robot sẽ bị mù và rất có thể sẽ va phải vật cản. Trong dự án này, các cảm biến cung cấp thông tin cho navigation stack bao gồm: cảm biến Lidar, cảm biến đo góc IMU, encoder. Do dự án sử dụng công nghệ quét bản đồ 2D nên dữ liệu của cảm biến sẽ được cung cấp qua sensor_msgs/LaserScan

<img src="assets/do-an-cdt/media/image56.jpeg" style="width:6.06656in;height:1.87042in" alt="Graphical user interface, text, application Description automatically generated" />

> Đối với rô bốt có máy quét laze, ROS cung cấp một loại tin nhắn đặc biệt trong gói sensor_msgs có tên là _[<u>LaserScan</u>](http://wiki.ros.org/sensor_msgs)_ để chứa thông tin về một lần quét nhất định. Thông báo _LaserScan_ giúp mã dễ dàng hoạt động với hầu hết mọi loại laser miễn là dữ liệu quay lại từ máy quét có thể được định dạng để phù hợp với thông báo. Một số đặc điểm kỹ thuật của LaserScan:
>
> <img src="assets/do-an-cdt/media/image57.jpeg" style="width:6.16578in;height:2.34458in" alt="Text Description automatically generated" />
>
> Xuất bản một thông báo LaserScan qua ROS khá đơn giản. Trước tiên, chúng ta cung cấp mã mẫu bên dưới để thực hiện điều đó và sau đó chia nhỏ mã xuống từng dòng một:
>
> <img src="assets/do-an-cdt/media/image58.jpeg" style="width:6.23867in;height:7.44in" alt="Graphical user interface, text, application Description automatically generated" />
>
> _c, Odometry Information (Thông tin đo đường: vận tốc, gia tốc, chiều quay…)_
>
> Thông báo nav_msgs/Odometry qua ROS có chứa ước tính về vị trí và vận tốc của robot trong không gian:
>
> <img src="assets/do-an-cdt/media/image59.jpeg" style="width:6.25291in;height:1.96937in" alt="Graphical user interface, text, application Description automatically generated" />
>
> Pose trong thông báo này tương ứng với vị trí ước tính của rô-bốt trong khung đo đường cùng với một hiệp phương sai tùy chọn để đảm bảo tính chắc chắn của ước tính tư thế đó. Twist trong thông báo này tương ứng với vận tốc của rô-bốt, thường là khung tọa độ của đế di động, cùng với một phương sai tùy chọn để đảm bảo chắc chắn cho ước tính vận tốc đó.
>
> Viết code:
>
> Thêm phần dependancy vào manifest.xml gói của bạn:

<img src="assets/do-an-cdt/media/image60.png" style="width:6.22257in;height:0.58333in" />

> <img src="assets/do-an-cdt/media/image61.jpeg" style="width:6.17542in;height:7.69604in" alt="Graphical user interface, text, application Description automatically generated" />
>
> <img src="assets/do-an-cdt/media/image62.jpeg" style="width:6.28389in;height:4.7724in" alt="Text Description automatically generated" />
>
> _d, Base Controller (bộ điều khiển cơ sở)_
>
> Ngăn xếp điều hướng giả định rằng nó có thể gửi các lệnh vận tốc bằng cách sử dụng thông báo geometry_msgs/Twist được giả định là nằm trong khung tọa độ cơ sở của rô-bốt theo chủ đề "cmd_vel". Điều này có nghĩa là phải có một nút đăng ký chủ đề "cmd_vel" có khả năng lấy (vx, vy, vtheta) \<==\> (cmd_vel.linear.x, cmd_vel.linear.y, cmd_vel.angular.z) vận tốc và chuyển đổi chúng thành lệnh vận động để gửi đến cơ sở di động.
>
> _e, Mapping ( Map_server )_
>
> Navigation stack yêu cầu phải có một bản đồ để có thể hoạt động.

<a id="chương-4-kết-luận-và-định-hướng-phát-triển"></a>

# CHƯƠNG 4: KẾT LUẬN VÀ ĐỊNH HƯỚNG PHÁT TRIỂN

<a id="kết-quả-đạt-được"></a>

## Kết quả đạt được

1.  **Lý thuyết**
    - Thiết kế mô hình và lựa chọn cơ cấu hợp lý.

    - Tính toán bài toán động học, động lực học cho Robot di động.

    - Tính toán được bài toán phục vụ lễ tân.

    - Cách kết nối Lidar với Raspberry pi và liên kết Raspberry pi với HostComputer.

    - Truyền được dữ liệu góc và tốc độ từ IMU và Encoder lên Raspi và truyền ngược lại vận tốc về 2 bánh về STM32.

2.  **Thực nghiệm**
    - Lập được bản đồ phòng lễ tân.

    - Thiết kế thành công mô hình robot phục vụ lễ tân.

    - Đảm bảo an toàn sử dụng.

    - Đạt được mục tiêu đề ra.

<img src="assets/do-an-cdt/media/image63.png" style="width:2.58771in;height:3.45in" />

<span id="_bookmark66" class="anchor"></span>_Hình 4.1: Mô hình thực tế_

> ∗ **Kết quả bản đồ thực tế thu được nhờ cảm biến Lidar:**

<img src="assets/do-an-cdt/media/image64.png" style="width:5.89527in;height:4.02in" alt="Diagram Description automatically generated" />

> <span id="_bookmark67" class="anchor"></span>_Hình 4.2: Bản đồ quét được trên không gian thực tế_

3.  **Hạn chế**

> Do kiến thức và thời gian nghiên cứu phát triển hạn chế nên robot vẫn gặp một vài hạn chế sau:

- Kết cấu, hình dạng Robot chưa thực sự đạt tính thẩm mỹ, robot còn thô sở và chưa được cứng cáp.

- Hệ thống di chuyển chưa ổn định.

- Robot hoạt động chưa thật sự chính xác hoàn toàn so với mặt lý thuyết.

- Vẫn còn độ trễ so với tính toán ban đầu.

- Giao diện người dùng chưa thực sự bắt mắt.

- Bản đồ quét được còn bị nhiễu, chưa rõ ràng

<a id="đánh-giá-và-định-hướng-phát-triển"></a>

## Đánh giá và định hướng phát triển

- Nâng cấp thiết kế cơ khí để có thể chở được nhiều khay đồ ăn hơn, chở được nhiều sản phẩm nặng hơn.

- Thiết kế hình dáng bắt mắt cho Robot phục vụ lễ tân giúp robot có vóc dáng thân thiên với người dùng hơn.

- Thiết kế hệ thống tháo lắp pin dễ dàng hơn.

- Tích hợp thêm hệ thống IoT để khi khách đặt hàng có thể hiển thị trực tiếp trên thiết bị kết nối từ xa.

- Thêm tính năng xử lý giọng nói giúp Robot phục vụ lễ tân giao tiếp giọng nói với khách hàng.

- Chuẩn hoá các module để dễ dàng phát triển và sản xuất công nghiệp.

> Phát triển thêm về ROS, các bài toán liên quan đến định vị, điều hướng mobile robot.

<a id="phụ-lục"></a>

# PHỤ LỤC

> **Chương trình điều khiển động cơ qua Encoder:**
>
> /\* USER CODE BEGIN Header \*/
>
> /\*\*
>
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
>
> \*\*\*\*\*\*\*\*\*
>
> \* @file : main.c
>
> \* @brief : Main program body
>
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
>
> \*\*\*\*\*\*\*\*\*
>
> \* @attention
>
> \*
>
> \* Copyright (c) 2022 STMicroelectronics.
>
> \* All rights reserved.
>
> \*
>
> \* This software is licensed under terms that can be found in the LICENSE file
>
> \* in the root directory of this software component.
>
> \* If no LICENSE file comes with this software, it is provided AS-IS.
>
> \*
>
> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
>
> \*\*\*\*\*\*\*\*\*
>
> \*/
>
> /\* USER CODE END Header \*/
>
> /\* Includes \*/
>
> \#include "main.h"
>
> /\* Private includes \*/
>
> /\* USER CODE BEGIN Includes \*/ uint32_t time;
>
> uint8_t dulieuH; uint8_t dulieuL; int16_t angle;
>
> int16_t anglereal, anglereal1; int16_t agpre;
>
> uint8_t z = 'z'; uint8_t a = 'a'; int16_t ct = 0,
>
> ct_pre = 0,
>
> rate = 0,
>
> cm = 0;
>
> volatile float vfilt,
>
> vfilt1 ,
>
> E, E1, E2,
>
> output, lastoutput; volatile float P_part,
>
> I_part, D_part;
>
> float Ti = 0.01; float Kp = 1.2, Ki = 0.1,
>
> Kd = 0.021;
>
> unsigned int setv = 40; volatile short count = 0,
>
> count_pre=0, v = 0,
>
> vpre = 0;
>
> //===============================================
>
> unsigned int setag; volatile float agfilt,
>
> agfilt1 ,
>
> Eag, E1ag, E2ag, outputag, lastoutputag;
>
> volatile float Pag_part,
>
> Iag_part, Dag_part;
>
> float Kpag = 0.0002, Kiag = 0.001,
>
> Kdag = 0.0021;
>
> /\* USER CODE END Includes \*/
>
> /\* Private typedef \*/
>
> /\* USER CODE BEGIN PTD \*/
>
> /\* USER CODE END PTD \*/
>
> /\* Private define \*/
>
> /\* USER CODE BEGIN PD \*/
>
> /\* USER CODE END PD \*/
>
> /\* Private macro \*/
>
> /\* USER CODE BEGIN PM \*/
>
> /\* USER CODE END PM \*/
>
> /\* Private variables \*/
>
> I2C_HandleTypeDef hi2c1;
>
> TIM_HandleTypeDef htim2; TIM_HandleTypeDef htim3;
>
> UART_HandleTypeDef huart1; UART_HandleTypeDef huart2; UART_HandleTypeDef huart3;
>
> /\* USER CODE BEGIN PV \*/
>
> /\* USER CODE END PV \*/
>
> /\* Private function prototypes \*/
>
> void SystemClock_Config(void); static void MX_GPIO_Init(void);
>
> static void MX_USART1_UART_Init(void);
>
> static void MX_TIM2_Init(void); static void MX_I2C1_Init(void); static void MX_TIM3_Init(void);
>
> static void MX_USART2_UART_Init(void); static void MX_USART3_UART_Init(void);
>
> /\* USER CODE BEGIN PFP \*/
>
> //========================================= Dieu khien dong co
>
> =============================================
>
> void send_motor(uint8_t dia_chi, uint8_t chieu_quay, uint8_t toc_do)
>
> {
>
> uint8_t byte_send\[3\] = {0, 0, 0}; byte_send\[0\] = chieu_quay \<\< 7 \| dia_chi; byte_send\[1\] = toc_do;
>
> byte_send\[2\] = 255;
>
> HAL_UART_Transmit(&huart1, byte_send, 3, 1);
>
> }
>
> void Straight(uint8_t x)
>
> {
>
> send_motor(1, 1, x);
>
> send_motor(2, 1, x);
>
> }
>
> void Lui(uint8_t x)
>
> {
>
> send_motor(1, 0, x);
>
> send_motor(2, 0, x);
>
> }
>
> void Left(uint8_t x)
>
> {
>
> send_motor(1, 0, x);
>
> send_motor(2, 1, x);
>
> }
>
> void Right(uint8_t x)
>
> {
>
> send_motor(1, 1, x);
>
> send_motor(2, 0, x);
>
> }
>
> /\* USER CODE END PFP \*/
>
> /\* Private user code \*/
>
> /\* USER CODE BEGIN 0 \*/
>
> //================================== La Ban
>
> ==================================
>
> uint16_t LaBan()
>
> {
>
> HAL_UART_Transmit(&huart3, &z, 1,1);//================== bat dau gui du lieu =====================
>
> HAL_UART_Receive(&huart3, &dulieuH, 1,1);//================== nhan byte cao =====================
>
> HAL_UART_Receive(&huart3, &dulieuL, 1,1);//================== nhan byte thap =====================
>
> angle =(dulieuH\<\<8)\|dulieuL;//================== ghep thanh gia tri goc
>
> \*10 =====================
>
> HAL_Delay(10); return angle;
>
> }
>
> void Encoder()
>
> {
>
> ct = HAL_TIM_GET_COUNTER(&htim2); cm = ( fabs(ct)/500)\*37.699;
>
> }
>
> /\* USER CODE END 0 \*/
>
> int main(void)
>
> {
>
> /\* USER CODE BEGIN 1 \*/
>
> //time = HAL_GetTick();
>
> /\* USER CODE END 1 \*/
>
> /\* MCU Configuration \*/
>
> /\* Reset of all peripherals, Initializes the Flash interface and the Systick. \*/ HAL_Init();
>
> /\* USER CODE BEGIN Init \*/
>
> /\* USER CODE END Init \*/
>
> /\* Configure the system clock \*/
>
> SystemClock_Config();
>
> /\* USER CODE BEGIN SysInit \*/
>
> /\* USER CODE END SysInit \*/
>
> /\* Initialize all configured peripherals \*/ MX_GPIO_Init(); MX_USART1_UART_Init();
>
> MX_TIM2_Init(); MX_I2C1_Init(); MX_TIM3_Init(); MX_USART2_UART_Init(); MX_USART3_UART_Init();
>
> /\* USER CODE BEGIN 2 \*/
>
> HAL_TIM_Encoder_Start(&htim2, TIM_CHANNEL_1 \| TIM_CHANNEL_2);
>
> //HAL_TIM_Base_Start_IT(&htim3); HAL_Delay(200);
>
> HAL_UART_Transmit(&huart3, &a, 1,1);//================== set goc ve 0
>
> =====================
>
> HAL_Delay(1000);
>
> /\* USER CODE END 2 \*/
>
> /\* Infinite loop \*/
>
> /\* USER CODE BEGIN WHILE \*/
>
> while (1)
>
> {
>
> anglereal = LaBan();
>
> if(anglereal\<900)
>
> {
>
> Left(7);
>
> }
>
> else Straight(7);
>
> /\* USER CODE END WHILE \*/
>
> /\* USER CODE BEGIN 3 \*/
>
> }
>
> /\* USER CODE END 3 \*/
>
> }
>
> /\*\*
>
> \* @brief System Clock Configuration
>
> \* @retval None
>
> \*/
>
> void SystemClock_Config(void)
>
> {
>
> RCC_OscInitTypeDef RCC_OscInitStruct = {0}; RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
>
> /\*\* Initializes the RCC Oscillators according to the specified parameters
>
> \* in the RCC_OscInitTypeDef structure.
>
> \*/
>
> RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE; RCC_OscInitStruct.HSEState = RCC_HSE_ON; RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1; RCC_OscInitStruct.HSIState = RCC_HSI_ON; RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON; RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE; RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
>
> if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> /\*\* Initializes the CPU, AHB and APB buses clocks
>
> \*/
>
> RCC_ClkInitStruct.ClockType =
>
> RCC_CLOCKTYPE_HCLK\|RCC_CLOCKTYPE_SYSCLK
>
> \|RCC_CLOCKTYPE_PCLK1\|RCC_CLOCKTYPE_PCLK2;
>
> RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK; RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1; RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2; RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
>
> if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> }
>
> /\*\*
>
> \* @brief I2C1 Initialization Function
>
> \* @param None
>
> \* @retval None
>
> \*/
>
> /\* USER CODE BEGIN TIM3_Init 1 \*/
>
> /\* USER CODE END TIM3_Init 1 \*/ htim3.Instance = TIM3; htim3.Init.Prescaler = 7199;
>
> htim3.Init.CounterMode = TIM_COUNTERMODE_UP; htim3.Init.Period = 99;
>
> htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1; htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE; if (HAL_TIM_Base_Init(&htim3) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
>
> if (HAL_TIM_ConfigClockSource(&htim3, &sClockSourceConfig) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET; sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
>
> if (HAL_TIMEx_MasterConfigSynchronization(&htim3, &sMasterConfig) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> /\* USER CODE BEGIN TIM3_Init 2 \*/
>
> /\* USER CODE END TIM3_Init 2 \*/
>
> }
>
> /\*\*
>
> \* @brief USART1 Initialization Function
>
> \* @param None
>
> \* @retval None
>
> \*/
>
> static void MX_USART1_UART_Init(void)
>
> {
>
> /\* USER CODE BEGIN USART1_Init 0 \*/
>
> /\* USER CODE END USART1_Init 0 \*/
>
> /\* USER CODE BEGIN USART1_Init 1 \*/
>
> /\* USER CODE END USART1_Init 1 \*/
>
> huart1.Instance = USART1; huart1.Init.BaudRate = 115200;
>
> huart1.Init.WordLength = UART_WORDLENGTH_8B; huart1.Init.StopBits = UART_STOPBITS_1; huart1.Init.Parity = UART_PARITY_NONE; huart1.Init.Mode = UART_MODE_TX_RX; huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE; huart1.Init.OverSampling = UART_OVERSAMPLING_16; if (HAL_UART_Init(&huart1) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> /\* USER CODE BEGIN USART1_Init 2 \*/
>
> /\* USER CODE END USART1_Init 2 \*/
>
> }
>
> /\*\*
>
> \* @brief USART2 Initialization Function
>
> \* @param None
>
> \* @retval None
>
> \*/
>
> static void MX_USART2_UART_Init(void)
>
> {
>
> /\* USER CODE BEGIN USART2_Init 0 \*/
>
> /\* USER CODE END USART2_Init 0 \*/
>
> /\* USER CODE BEGIN USART2_Init 1 \*/
>
> /\* USER CODE END USART2_Init 1 \*/
>
> huart2.Instance = USART2; huart2.Init.BaudRate = 115200;
>
> huart2.Init.WordLength = UART_WORDLENGTH_8B; huart2.Init.StopBits = UART_STOPBITS_1; huart2.Init.Parity = UART_PARITY_NONE; huart2.Init.Mode = UART_MODE_TX_RX; huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE; huart2.Init.OverSampling = UART_OVERSAMPLING_16; if (HAL_UART_Init(&huart2) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> /\* USER CODE BEGIN USART2_Init 2 \*/
>
> /\* USER CODE END USART2_Init 2 \*/
>
> }
>
> /\*\*
>
> \* @brief USART3 Initialization Function
>
> \* @param None
>
> \* @retval None
>
> \*/
>
> static void MX_USART3_UART_Init(void)
>
> {
>
> /\* USER CODE BEGIN USART3_Init 0 \*/
>
> /\* USER CODE END USART3_Init 0 \*/
>
> /\* USER CODE BEGIN USART3_Init 1 \*/
>
> /\* USER CODE END USART3_Init 1 \*/
>
> huart3.Instance = USART3; huart3.Init.BaudRate = 115200;
>
> huart3.Init.WordLength = UART_WORDLENGTH_8B; huart3.Init.StopBits = UART_STOPBITS_1; huart3.Init.Parity = UART_PARITY_NONE; huart3.Init.Mode = UART_MODE_TX_RX; huart3.Init.HwFlowCtl = UART_HWCONTROL_NONE; huart3.Init.OverSampling = UART_OVERSAMPLING_16; if (HAL_UART_Init(&huart3) != HAL_OK)
>
> {
>
> Error_Handler();
>
> }
>
> /\* USER CODE BEGIN USART3_Init 2 \*/
>
> /\* USER CODE END USART3_Init 2 \*/
>
> }
>
> /\*\*
>
> \* @brief GPIO Initialization Function
>
> \* @param None
>
> \* @retval None
>
> \*/
>
> static void MX_GPIO_Init(void)
>
> {
>
> /\* GPIO Ports Clock Enable \*/
>
> HAL_RCC_GPIOD_CLK_ENABLE();
>
> HAL_RCC_GPIOA_CLK_ENABLE();
>
> HAL_RCC_GPIOB_CLK_ENABLE();
>
> }
>
> /\* USER CODE BEGIN 4 \*/
>
> /\* USER CODE END 4 \*/
>
> /\*\*
>
> \* @brief This function is executed in case of error occurrence.
>
> \* @retval None
>
> \*/
>
> void Error_Handler(void)
>
> {
>
> /\* USER CODE BEGIN Error_Handler_Debug \*/
>
> /\* User can add his own implementation to report the HAL error return state \*/
>
> disable_irq(); while (1)
>
> {
>
> }
>
> /\* USER CODE END Error_Handler_Debug \*/
>
> }
>
> void assert_failed(uint8_t \*file, uint32_t line)
>
> {
>
> /\* USER CODE BEGIN 6 \*/
>
> /\* User can add his own implementation to report the file name and line number, ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) \*/
>
> /\* USER CODE END 6 \*/
>
> }
>
> \#endif /\* USE_FULL_ASSERT \*/

<a id="tài-liệu-tham-khảo"></a>

# TÀI LIỆU THAM KHẢO

1.  PGS. TS. Trịnh Chất – TS. Lê Văn Uyển, Tính toán thiết kế hệ thống dẫn động cơ khí, Nhà xuất bản Giáo Dục, 2007.

2.  Lê Ngọc Duy, Giáo trình Cảm biến và hệ thống đo, Đại học Công nghiệp Hà Nội, 2019.

3.  Spyros G. Tzafestas, Introduction to Mobile Robot Control

4.  Prof. Alessandro De Luca, Wheel Mobile Robots Introduction anh Kinematic Modeling.

5.  Ronal Siegward - Illah Reza Nourbakhsh - Davide Scaramuzza, Introduction to Autonomous Mobile Robots.

6.  Gang Peng (2018), _“An Improved AMCL Algorithm Based on Laser Scanning Match in a Complex and Unstructured Environment”_, pp. 1-4.

7.  D. F. D. F. Global planner, _"The Dynamic Window Approach to Collision Avoidance",_ pp. 10-12.

8.  Viktor Kozák (2013), _“Local planning for a mobile robot”_, Czech Technical University In Prague.

9.  R. N. Wiki, "Robot Operating System Wiki," Navigation, \[Online\]. Available: [<u>http://wiki.ros.org/navigation/Tutorials/RobotSetup</u>.](http://wiki.ros.org/navigation/Tutorials/RobotSetup)

10. W. C. ROS, "Robot Operating System Wiki," Costmap 2D, \[Online\]. Available: [<u>http://wiki.ros.org/costmap_2d.s</u>.](http://wiki.ros.org/costmap_2d.s)

11. M. Seder, K. Maˇcek, I. Petroviˇc, _“An integrated approach to real-time mobile robot control in partially known indoor environments”,_ Industrial Electronics Society, 2005. IECON 2005.

12. A. Koubaa (2018), _“Introduction to Mobile Robot Path Planning”_, Springer International Publishing AG.

13. YoonSeok Pyo \| HanCheol Cho \| RyuWoon Jung \| TaeHoon Lim (2017), _“ROS Robot Programming”_, ROBOTIS Co.,Ltd.

14. Francisco Valero, Carlos Llopis-Albert, Carlos Llopis-Albert (2019), _“A review of mobile robots: Concepts, methods, theoretical framework, and applications”._

15. J. Minguez and L. Montano, Nearness diagram (ND), _“Collision avoidance in troublesome scenarios”._ IEEE Transactions on Robotics and Automation, 2004.

16. Thaker Nayl, Mohammed Q Mohammed, and Saif Q Muhamed. 2017. _“Obstacles avoidance for an articulated robot using modified smooth path planning”._ 2017 international conference on computer and applications (ICCA), IEEE.

17. J. Borenstein and Y. Koren, _“The Vector Field Histogram-Fast Obstacle Avoidance for Mobile Robots”._ IEEE TRANSACTIONS ON ROBOTICS AND AUTOMATION, 1991.
