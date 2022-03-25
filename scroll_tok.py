from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time



#WINDOWS INSTRUCTIONS: Run these commands in command prompt
#cd C:\Program Files (x86)\Google\Chrome\Application
#chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\willi\OneDrive\Documents\Research\Media Lab-Ecig\chromeprofile"

#IMPORTANT: Have to prelog into tiktok, can't use selenium to autolog since you will be flagged as a bot
opt=Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

#Set Number of Video urls you want to get:
num_scrapes = 10

#List of video ids
video_links = []

driver = webdriver.Chrome(ChromeDriverManager().install() ,chrome_options=opt)
driver.get('https://www.tiktok.com/foryou?lang=en')

#click video on for you page
vid_link = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/video')
vid_link.click()

#give page a seconds to load
time.sleep(1)

for i in range(num_scrapes - 1):
    video_links.add(driver.current_url)
    next_but = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/button[3]')
    next_but.click()
    time.sleep(1)
#off by one error
video_links.add(driver.current_url)

for link in video_links:
    print(link)
