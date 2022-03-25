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
driver = webdriver.Chrome(ChromeDriverManager().install() ,chrome_options=opt)
driver.get('https://www.tiktok.com/foryou?lang=en')

#Set Number of Video urls you want to get:
num_scrapes = 10

#click video on for you page
time.sleep(1)
vid_link = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/video')
vid_link.click()

#write the urls to file
url_file = open("urls.txt", "w")

#give page a seconds to load
time.sleep(3)

for i in range(num_scrapes):
    #write the url to file
    url = driver.current_url
    url_file.write(url.replace("?is_copy_url=1&is_from_webapp=v1&lang=en", "") + "\n")

    #go to next video
    next_but = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/button[3]')
    next_but.click()
    time.sleep(1)
    
#get last off by one     
url = driver.current_url
url_file.write(url.replace("?is_copy_url=1&is_from_webapp=v1&lang=en", "") + "\n")
url_file.close()

