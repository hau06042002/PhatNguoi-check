# HƯỚNG DẪN CÀI ĐẶT VÀ TRIỂN KHAI PROJECT

## 1. Giới thiệu

Đây là project tự động tra cứu phương tiện vi phạm trên trang CSGT Việt Nam bằng Python, Selenium và OCR. Hướng dẫn này sẽ giúp bạn cài đặt môi trường, cấu hình, chạy chương trình và đẩy mã nguồn lên GitHub một cách chi tiết.

---

## 2. Yêu cầu hệ thống

- **Hệ điều hành:** Windows 10/11 (ưu tiên), có thể dùng MacOS/Linux với điều chỉnh tương ứng
- **Python:** Phiên bản 3.7 trở lên
- **Google Chrome:** Phiên bản mới nhất
- **ChromeDriver:** Phù hợp với phiên bản Chrome đang sử dụng
- **Tesseract OCR:** Để nhận diện mã captcha

---

## 3. Cài đặt môi trường

### 3.1. Cài đặt Python

- Tải Python tại: https://www.python.org/downloads/
- Cài đặt và tick vào “Add Python to PATH” khi cài đặt.

### 3.2. Cài đặt Google Chrome

- Tải và cài đặt tại: https://www.google.com/chrome/

### 3.3. Cài đặt ChromeDriver

- Mở Chrome, truy cập `chrome://settings/help` để xem phiên bản Chrome.
- Truy cập https://chromedriver.chromium.org/downloads, chọn đúng phiên bản ChromeDriver tương ứng.
- Giải nén file vừa tải về.
- Thêm đường dẫn chứa file `chromedriver.exe` vào biến môi trường `PATH`:
  - Chuột phải **This PC** → **Properties** → **Advanced system settings** → **Environment Variables** → Chỉnh sửa biến `Path` và thêm đường dẫn tới thư mục chứa `chromedriver.exe`.
  - Hoặc đặt file `chromedriver.exe` cùng thư mục với project.

### 3.4. Cài đặt Tesseract OCR

- Tải tại: https://github.com/UB-Mannheim/tesseract/wiki (chọn bản dành cho Windows)
- Cài đặt và ghi nhớ đường dẫn, ví dụ:  
  `C:\Program Files\Tesseract-OCR\tesseract.exe`

### 3.5. Cài đặt các thư viện Python

Mở terminal/cmd tại thư mục project và chạy:

```sh
pip install selenium pillow pytesseract schedule
```

---

## 4. Cấu hình, đẩy lên GitHub và lưu ý

### 4.1. Cấu hình đường dẫn Tesseract trong mã nguồn

- Mở file main.py
- Tìm dòng:

```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

- Đảm bảo đường dẫn đúng với nơi bạn đã cài đặt Tesseract.

### 4.2. Khởi tạo và đẩy project lên GitHub

- Đăng ký tài khoản GitHub tại https://github.com/ nếu chưa có.
- Tạo repository mới trên GitHub.
- Mở terminal/cmd tại thư mục project, chạy lần lượt:

```sh
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/hau06042002/TraCuuPhatNguoi.git
git branch -M main
git push -u origin main

```

### 4.3. Lưu ý

- Nếu chương trình không tự động nhận diện captcha, bạn cần nhập thủ công trên trình duyệt.
- Đảm bảo ChromeDriver và Chrome cùng phiên bản.
- Nếu gặp lỗi, kiểm tra lại các bước cài đặt hoặc tạo Issue trên GitHub để được hỗ trợ.
