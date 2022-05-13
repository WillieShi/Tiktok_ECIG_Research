# Tiktok_ECIG_Research
This script was developed to research the for you pages of test 16 year old and 24 year old accounts that have a lot of liked e-cigarette content.

For a given account, it will auto scroll through the fyp, watch each video for a specified range of time, and then store all the meta data into an outfile.

In addition, it will also comment on any vape related video based on the rule system in order to simulate interaction. I was not able to get the bot to auto-like videos
without TikTok preventing me.

#Credit
Heavily used this unofficial TikTok API:
https://github.com/davidteather/TikTok-Api

#Getting Started(Windows)
1. You need to selenium to hijack an existing chrome browser since TikTok can detect if it's a browser launched specifically for automated software.
Open a command prompt and naviagete to your chrome application installition, on my computer it's:
cd C:\Program Files (x86)\Google\Chrome\Application

Then launch a chrome browser in debugging mode with:
chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\willi\OneDrive\Documents\Research\Media Lab-Ecig\chromeprofile"

2. Next you need to open TikTok and login into the page because Tiktok can flags selenium account logins as bots.

3. Install required packages(Python 3.9)
pip install -r requirements.txt

4. Call the Script:
python sc_master.py
