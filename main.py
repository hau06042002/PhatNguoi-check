import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import schedule

# Đường dẫn tới tesseract.exe (cập nhật đúng đường dẫn trên máy bạn)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def tra_cuu_phat_nguoi():
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=chrome_opt)
    browser.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    # Đợi trường nhập biển số xuất hiện
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.NAME, "BienKiemSoat"))
    )

    bien_so_xe = "30A54321"
    browser.find_element(By.NAME, "BienKiemSoat").send_keys(bien_so_xe)

    chon_loai_xe = Select(browser.find_element(By.NAME, "LoaiXe"))
    chon_loai_xe.select_by_value("1")  # 1: Ô tô 2: Xe máy 3: Xe đạp điện
    # Lưu ảnh captcha
    captcha_field = browser.find_element(By.NAME, "txt_captcha")
    captcha_field.screenshot("captcha.png")

    # Tiền xử lý ảnh captcha
    anh = Image.open("captcha.png").convert("L")
    anh = anh.point(lambda x: 0 if x < 140 else 255, '1')
    ma_bao_mat = pytesseract.image_to_string(anh, config='--psm 8').strip()
    print("Mã bảo mật nhận diện được:", ma_bao_mat)

    # Nhập mã bảo mật
    captcha_input = browser.find_element(By.NAME, "txt_captcha")
    captcha_input.clear()
    captcha_input.send_keys(ma_bao_mat)

    input("Kiểm tra lại mã captcha trên trình duyệt, sửa nếu cần rồi nhấn Enter để tiếp tục...")

    # Bấm nút tra cứu
    tra_cuu_btn = browser.find_element(By.XPATH, "//input[@type='button' and @value='Tra cứu']")
    tra_cuu_btn.click()

    print("Đã thực hiện tra cứu.")

# Lên lịch chạy tự động
schedule.every().day.at("06:00").do(tra_cuu_phat_nguoi)
schedule.every().day.at("12:00").do(tra_cuu_phat_nguoi)

print("Chương trình đang chờ đến giờ chạy...")

while True:
    schedule.run_pending()
    time.sleep(60)