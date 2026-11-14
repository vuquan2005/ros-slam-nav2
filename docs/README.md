# Tài liệu dự án

- [Tài liệu Word gốc](<Đồ án CĐT.docx>).
- [Bản Markdown](do-an-cdt.md).
- [Ảnh và tài nguyên trích xuất](assets/do-an-cdt/media/).
- [Kế hoạch chuyển đổi robot vi sai hai bánh dùng LiDAR](chuyen-doi-robot-vi-sai.md).

## Bản chuyển đổi

`do-an-cdt.md` được chuyển từ Word bằng Pandoc, giữ nội dung tham khảo gốc về robot phục vụ lễ tân. Nội dung này không mô tả trạng thái triển khai của workspace hiện tại.

Các bảng phức tạp và công thức được trình bày bằng bảng HTML nhúng để giữ cấu trúc hàng/cột. Ảnh dùng đường dẫn tương đối; bookmark và mục lục được giữ lại. Số trang trong mục lục thuộc bản Word, không phải phân trang Markdown. Các đoạn code và ảnh chụp code giữ nguyên như tài liệu nguồn, chưa được kiểm thử chạy.

Thư mục tài nguyên chứa đủ 64 ảnh gốc; 60 ảnh được bản Markdown tham chiếu. Bốn ảnh `image2.png`, `image3.png`, `image4.png`, `image5.jpeg` không được Pandoc đưa vào phần nội dung chuyển đổi và vẫn được giữ để đối chiếu. File Word gốc được giữ nguyên để kiểm tra bố cục khi cần.

## Tạo lại bản Markdown

Cần Python 3 và Pandoc trên `PATH`. Tại thư mục gốc workspace:

```bash
python3 tools/convert-docx.py 'docs/Đồ án CĐT.docx' docs/do-an-cdt.md
```

Có thể chỉ định bản Pandoc cài riêng bằng `--pandoc /duong/dan/pandoc`. Script tạo lại bản Markdown và trích xuất toàn bộ ảnh vào `docs/assets/do-an-cdt/media/`.
