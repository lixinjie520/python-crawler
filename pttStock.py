# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 設定 chromedriver的執行檔路徑
options = Options()
options.chrome_executable_path = "D:/chromedriver-win64/chromedriver.exe"
options.add_experimental_option("detach", True)
# 建立 Driver 物件實體，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)
# 連線到目標網頁
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# 取得網頁原始碼
# print(driver.page_source)
titles = driver.find_elements(By.CLASS_NAME, 'title')
for title in titles:
    print(title.text)
link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click()
titles = driver.find_elements(By.CLASS_NAME, 'title')
for title in titles:
    print(title.text)
# driver.close()
