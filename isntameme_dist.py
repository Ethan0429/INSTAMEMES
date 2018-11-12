import sys
import praw #pip install praw
from selenium import webdriver #pip install selenium
import time
import urllib.request
from selenium.webdriver.common.keys import Keys 
import pyautogui as controller #pip install pyautogui
import random

'''-------------------------------------------------------- Reddit API setup -----------------------------------------------------------------------------'''

reddit_p = praw.Reddit(client_id='YOURS HERE',
						client_secret='YOURS HERE',
						user_agent='YOURS HERE')

sr_memes = reddit_p.subreddit('memes')
sr_edgymemes = reddit_p.subreddit('edgymemes')
sr_bpt = reddit_p.subreddit('blackpeopletwitter')

'''------------------------------------------------------- Variables used for checking or lists -----------------------------------------------------------------------------'''

submissionnum_memes = 0
submissionnum_edgymemes = 0
submissionnum_bpt = 0
bpt_urls = []
edgymemes_urls = []
meme_urls = []

'''------------------------------------------------------ Loop that indexes urls to lists -------------------------------------------------------------------------------'''

for submission_bpt in sr_bpt.hot(limit=5):
	if('.jpg' in submission_bpt.url or '.png' in submission_bpt.url):
		bpt_urls.insert(submissionnum_bpt, submission_bpt.url)
		submissionnum_bpt+1
	else:
		continue

for submission_meme in sr_memes.hot(limit=5):
	if('.jpg' in submission_bpt.url or '.png' in submission_meme.url):
		meme_urls.insert(submissionnum_memes, submission_meme.url)
		submissionnum_memes+1
	else:
		continue

for submission_edgymeme in sr_edgymemes.hot(limit=5):
	if('.jpg' in submission_bpt.url or '.png' in submission_edgymeme.url):
		edgymemes_urls.insert(submissionnum_edgymemes, submission_edgymeme.url)
		submissionnum_edgymemes+1
	else:
		continue

'''----------------------------------------------------------- Loop that iterates through each url and saves them --------------------------------------------------------------------------'''

for i_meme, image_meme in enumerate(meme_urls, start=1):
	urllib.request.urlretrieve(image_meme, r"C:\Users\ethan\Desktop\instameme\memes\meme"+str(i_meme)+".png")
	time.sleep(2.5)

time.sleep(5)

for i_bpt, image_bpt in enumerate(bpt_urls, start=1):
	urllib.request.urlretrieve(image_bpt, r"C:\Users\ethan\Desktop\instameme\memes\bpt"+str(i_bpt)+".png")
	time.sleep(2.5)

time.sleep(5)

for i_edgymeme, image_edgymeme in enumerate(edgymemes_urls, start=1):
	urllib.request.urlretrieve(image_edgymeme, r"C:\Users\ethan\Desktop\instameme\memes\edgymeme"+str(i_edgymeme)+".png")
	time.sleep(3)

'''--------------------------------------------------------- Lists of hastags, caption phrases, and meme index for deciding which meme-type to pull from ----------------------------------------------------------------------------'''

caption_phrases = ['Wowzers', 'thats gonna be a big yikes from me dawg', 'how ya guys like this one?', 'these are all prerecorded messages', 'im definitely not a robot',
'we will enslave the humans eventually', 'my python dont']
hashtags = '#meme #memes #funny #dankmemes #dank #lol #lmao #edgy #funnymemes #memesdaily #dankmeme #f #edgymemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
meme_index = ['edgymeme', 'meme', 'bpt']

'''--------------------------- Very messy but basically used to write to a .txt file the # of meme that I'm on (ie 1, 2, etc) so the script doesn't repeat post --------------------------------------------------------------------------------------'''

memenum = 1 

with open('meme.txt', 'r') as f:
	f_content = f.read()

memenum = int(f_content)

if(memenum > 15):
	memenum = '1'
else:
	memenum = f_content

newmemenum = int(memenum)+1

'''------------------------------------- Webpage nagivation ------------------------------------------------------------------------------------------------'''

insta_driver = webdriver.Chrome()
insta_driver.set_window_size(1813,990)
insta_driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(1)
insta_driver.find_element_by_name('username').send_keys('YOURS HERE')
time.sleep(1)
insta_driver.find_element_by_name('password').send_keys('YOURS HERE'+Keys.RETURN)
time.sleep(2)

controller.moveTo(907,704)
time.sleep(.100)
controller.click()
controller.hotkey('ctrl', 'shift', 'i')
time.sleep(.5)
controller.hotkey('ctrl', 'shift', 'm')  
time.sleep(1)
controller.moveTo(104,70)
time.sleep(.5)
controller.click()
time.sleep(5) 
controller.moveTo(640,950)
time.sleep(.5)
controller.click()
controller.moveTo(314,58)
time.sleep(.5)
controller.click()
controller.typewrite(r'C:\Users\ethan\Desktop\instameme\memes')
time.sleep(.5)
controller.press('enter')
time.sleep(.5)
controller.moveTo(803,483)
time.sleep(.5)
controller.click()
time.sleep(.5)
controller.moveTo(781,521)
time.sleep(.5)
controller.click()
time.sleep(.5)
controller.moveTo(270,486)
time.sleep(.5)
controller.click()
if(memenum == '15'): #too lazy to change the list size. For some reason edgy memes only go up to 14 right now
	controller.typewrite(meme_index[1]+memenum+'.png')
else:
	controller.typewrite(random.choice(meme_index)+memenum+'.png') #randomizes the type of meme posted & controls the # meme
time.sleep(1)
controller.press('enter')
time.sleep(.5)
controller.moveTo(472,614) #resize
time.sleep(.5)
controller.click()
time.sleep(1)
controller.moveTo(808,223) #next
time.sleep(.5)
controller.click()
time.sleep(.5)
controller.moveTo(575,276)
time.sleep(.5)
controller.click()
controller.typewrite(random.choice(caption_phrases)+' '+hashtags) #random caption & hashtag list
time.sleep(3)
controller.moveTo(800,223)
time.sleep(.1)
controller.click() #share

with open('meme.txt', 'w') as file: #writes to .txt file the # meme so the scipt remembers for next run
	file.write(str(newmemenum)) 

sys.exit()
