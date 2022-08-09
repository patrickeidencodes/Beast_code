from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time

mail = "DasWäreJaKeinDing"
pw = "AberSoDummBinIchAuchWiederNicht:D"
driver = webdriver.Chrome(executable_path="D:\\Programming\\Python\\Web Scrawler\\chromedriver2.exe")
driver.get("https://www.youtube.com/user/MrBeast6000/videos")
buttons = driver.find_elements(By.TAG_NAME,"button")

buttons[2].click()
time.sleep(2)

#sign in
driver.find_elements(By.CSS_SELECTOR, "a[href='https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dde%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fuser%252FMrBeast6000%252Fvideos%253Fcbrd%253D1&hl=de&ec=65620']")[0].click()
driver.find_elements(By.XPATH,"//input[@type='email']")[0].send_keys(mail)
driver.find_elements(By.XPATH,"//*[@id='identifierNext']")[0].click()
time.sleep(10)
driver.find_elements(By.XPATH,"//input[@type='password']")[0].send_keys(pw)
driver.find_elements(By.XPATH,"//*[@id='passwordNext']")[0].click()
time.sleep(2)

#loop to check if the new video is up
while True:
    WebDriverWait(driver, 10).until(expect.presence_of_element_located((By.ID, "video-title")))
    videos2 = driver.find_elements(By.ID,"video-title")[2].text
    if videos2 != "100 Girls Vs 100 Boys For $500,000":
        data = driver.find_elements(By.CSS_SELECTOR,"ytd-grid-video-renderer")[0].click()
        driver.execute_script("window.scrollBy(0,300)") 
        WebDriverWait(driver, 10).until(expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))
        item = driver.find_element(By.CSS_SELECTOR,"ytd-comments ytd-comment-simplebox-renderer div#placeholder-area")
        item.click()
        item = driver.find_elements(By.XPATH,"//*[@id='contenteditable-root']")[0]                                     
        item.click()
        item.send_keys("1")
        item.send_keys(Keys.CONTROL, Keys.ENTER)
        break
    else:
        driver.refresh()
