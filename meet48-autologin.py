# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
#載入定時模

# 設定 chromedriver的執行檔路徑
options = Options()
options.chrome_executable_path = "D:/chromedriver-win64/chromedriver.exe"
options.add_experimental_option("detach", True)
# 建立 Driver 物件實體，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)
# 連線到目標網頁
driver.get("https://gipr.meet48.xyz/#/task")

clickLogIn = driver.find_element(By.CLASS_NAME, "style_borderOnly__rpIqm")
time.sleep(2)
clickLogIn.click()
time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, "[type=text]")
password = driver.find_element(By.CSS_SELECTOR, "[type=password]")
username.send_keys("amber")
password.send_keys("lxj520wangshengyan")
# 取得登錄按鈕
logInBtn = driver.find_element(By.CLASS_NAME, "style_btn__VEzut")
logInBtn.send_keys(Keys.ENTER)
time.sleep(2)
cards = driver.find_elements(By.CLASS_NAME, "style_taskBox__7QD99")
cards[1].click()
award = driver.find_element(By.CLASS_NAME, "style_btn__i7g3Y")
award.click()

# driver.close()


