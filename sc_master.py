from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

from TikTokApi import TikTokApi
import csv
import sys  
import time
import pandas as pd
import random


#WINDOWS INSTRUCTIONS: Run these commands in command prompt
#cd C:\Program Files (x86)\Google\Chrome\Application
#chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\willi\OneDrive\Documents\Research\Media Lab-Ecig\chromeprofile"

#IMPORTANT: Have to prelog into tiktok, can't use selenium to autolog since you will be flagged as a bot
opt=Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(ChromeDriverManager().install() ,chrome_options=opt)
driver.get('https://www.tiktok.com/foryou?lang=en')

api = TikTokApi()

#list of dicts w vid data
video_data = []
errors = []

#identify if video is vape related
vape_words = ["vape", "boxmods", "disposables", "e-cig", "e-cigarette", "e-juice", "e-liquid", "ends", "pod-mods", "vape-juice",
"vape-mods", "vape-pens", "vape-pods", "Eleaf", "Aspire", "eGo", "V2", "Smok", "STLTH", "Vype", "E-lites", "VIP", "88Vape", 
"KangerTech", "Vaper", "Vapers", "Vapin", "Vaped", "Evape", "Vaporing", "e-cig*a", "ecig*a", "e-pen", "epen", "e-juice", "ejuice", "e-liquid",
"eliquid", "cloud chasing", "deeming AND regulation", "deeming AND FDA", "deemed AND FDA", "Deem*a and FDA", "elfbar"]

#Fake comment list
fake_comments = ["I love vaping","vaping is so cool!",
"what flavor is that brand?", "vape nation", "yo mama",
"asdasdasd", "vapppeeeeeeee", "nicottine",
"based as fuck", "420", "vape vape vape",
"sick smoke tricks", "vape nash", "based",
"poggers", "smoke cloud", "smoking is rad",
"vaping > smoking", "vaping", "mint flavored vaping is the best",
"That ghost was smooth", "smooth ghost yo"]


# #click video on for you page
time.sleep(3)
vid_link = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/video')
vid_link.click()

#check if word is vape related
def vape_related(desc):
    hashtags = [tag.strip() for tag in desc[desc.find('#')+1:].split('#')]
    print("hashtags", hashtags)

    for word in vape_words:
        if word in desc or word in hashtags:
            print("vape_trigger:", word)
            return True
    return False

#update this count with last id, I currently don't have it programtically update from the latest id stored in file
#so you will need to update this count manually if you are running this script w the same output file multiple times.
count = 175
vape_count = 0

#SET THESE BEFORE SCRAPING
num_scrapes = random.randint(40, 50) #random num of scrapes to help dodge bot detection
file_name = "out_test.csv" #output file
url_file = open("urls.txt", "a") #url output file

vape_labels = [] 
for i in range(num_scrapes):
    try:
        url = driver.current_url

        #Use tiktok python API to get the video data
        video = api.video(url=url.strip()).info()
        time_stamp = video['video']['duration']
        desc = video['desc']
        count += 1

        #write the url to file and add video data to list
        url_file.write(url.replace("?is_copy_url=1&is_from_webapp=v1&lang=en", "") + "\n")
        video['id'] = count
        video_data.append(video)
        print("timestamp:", time_stamp)
        print(count)

        #random comment if vape video
        if vape_related(desc):
            vape_labels.append("vape_related")
            vape_count += 1

            #TODO Figure out how to get like button auto click to work
            # like_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]')
            # ActionChains(driver).move_to_element(like_button).click(like_button).perform()

            comment = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/div[4]/div/div[1]/div/div[1]/div/div/div/div/div/div/div')
            message = random.choice(fake_comments)
            comment.send_keys(message)
            comment_but = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/div[4]/div/div[2]')
            comment_but.click()

            sleep_time = int(time_stamp) *  random.uniform(0.6, 0.8)
        else:
            vape_labels.append("non_related")
            sleep_time = int(time_stamp) * random.uniform(0.1, 0.2)
        
        #sleep for part of the video
        print(sleep_time)
        time.sleep(int(sleep_time)) 

    except Exception as e:
        errors.append(driver.current_url)
        print("Whoops")
        print(e)
        pass
    
    #go to next video
    time.sleep(1)
    next_but = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/button[3]')
    next_but.click()
    time.sleep(1)

print(vape_count)
df = pd.DataFrame.from_dict(video_data)
df['vape_label'] = vape_labels
df.to_csv(file_name, mode='a')
print(len(vape_labels))
print("errors", errors)


    

    

