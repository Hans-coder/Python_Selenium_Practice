from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
 
chrome = webdriver.Chrome()
chrome.get("https://www.dcard.tw/f")
# zoom up the window
chrome.maximize_window()

time.sleep(2)

# # click login button
# python_button = chrome.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[1]/a/button/div')
# python_button.click()

# time.sleep(3)

# # click the FB login button
# FB_button = chrome.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/a[1]/div[2]')
# FB_button.click()

# # Type in the account/password
# mail = chrome.find_element(By.XPATH,'//*[@id="email"]')
# mail.send_keys('')
# pwd = chrome.find_element(By.XPATH,'//*[@id="pass"]')
# pwd.send_keys('')
# login = chrome.find_element(By.XPATH,'//*[@id="u_0_0_Pn"]')
# login.click()

search_bar = chrome.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div/form/input')
search_bar.send_keys('攝影')

time.sleep(2)

search_button = chrome.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]')
search_button.click()

time.sleep(2)

#check the post
for i in range(2,10):
    if i == 4:
        continue
    post = chrome.find_element(By.XPATH,f'//*[@id="__next"]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[{i}]/article/h2/a')
    post.click()

    time.sleep(2)

    emoji = chrome.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]')
    emoji_amount = int(emoji.text)
    print("本篇文章emoji數量為"+str(emoji_amount))
    if emoji_amount > 60:
        print('It is a good post!')
    else:
        print('It is a bad post!')

    #將文章關閉
    ActionChains(chrome).send_keys(Keys.ESCAPE).perform()

    #滾動頁面高度
    lenOfPage = chrome.execute_script('window.scrollTo(0, 150)')

    time.sleep(2)


print("the program is done!")

#close the browser
chrome.close()
