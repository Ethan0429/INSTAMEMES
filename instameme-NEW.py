import sys
import praw #pip install praw
import time
import urllib
import random
from InstagramAPI import InstagramAPI #pip install InstagramApi

'''-------------------------------------------------------- Reddit API setup -----------------------------------------------------------------------------'''

reddit_p = praw.Reddit(client_id='YOUR INFO',
						client_secret='YOUR INFO',
						user_agent='YOUR INFO')

sr_memes = reddit_p.subreddit('memes')
sr_dankmemes = reddit_p.subreddit('dankmemes')
sr_bpt = reddit_p.subreddit('blackpeopletwitter')

'''------------------------------------------------------- Variables used for checking or lists -----------------------------------------------------------------------------'''

submissionnum_memes = 0
submissionnum_dankmemes = 0
submissionnum_bpt = 0
bpt_urls = []
dankmemes_urls = []
meme_urls = []
bpt_dict = {}
bpt_count = 1
meme_dict = {}
meme_count = 1
dankmeme_count = 1
dankmeme_dict = {}
'''------------------------------------------------------ Loop that indexes urls to lists -------------------------------------------------------------------------------'''

for submission_bpt in sr_bpt.hot(limit=10):
	if('.jpg' in submission_bpt.url and 'redd' in submission_bpt.url):
		bpt_urls.insert(submissionnum_bpt, submission_bpt.url)
		submissionnum_bpt+1
		bpt_dict[submission_bpt.url] = bpt_count
		bpt_count = bpt_count+1
	elif('imgur' in submission_bpt.url):
		bpt_urls.insert(submissionnum_bpt, submission_bpt.url)
		submissionnum_bpt+1
		bpt_dict[submission_bpt.url] = bpt_count
		bpt_count = bpt_count+1
	else:
		continue

for submission_meme in sr_memes.hot(limit=10):
	if('.jpg' in submission_meme.url and 'redd' in submission_meme.url):
		meme_urls.insert(submissionnum_memes, submission_meme.url)
		submissionnum_memes+1
		meme_dict[submission_meme.url] = meme_count
		meme_count = meme_count+1
	elif('imgur' in submission_meme.url):
		meme_urls.insert(submissionnum_memes, submission_meme.url)
		submissionnum_memes+1
		meme_dict[submission_meme.url] = meme_count
		meme_count = meme_count+1
	else:
		continue

for submission_dankmeme in sr_dankmemes.hot(limit=5):
	if('.jpg' in submission_dankmeme.url and 'redd' in submission_dankmeme.url):
		dankmemes_urls.insert(submissionnum_dankmemes, submission_dankmeme.url)
		submissionnum_dankmemes+1
		dankmeme_dict[submission_dankmeme.url] = dankmeme_count
		dankmeme_count = dankmeme_count+1
	elif('imgur' in submission_dankmeme.url):
		dankmemes_urls.insert(submissionnum_dankmemes, submission_dankmeme.url)
		submissionnum_dankmemes+1
		dankmeme_dict[submission_dankmeme.url] = dankmeme_count
		dankmeme_count = dankmeme_count+1
	else:
		continue

'''----------------------------------------------------------- Loop that iterates through each url and saves them --------------------------------------------------------------------------'''

for i_meme, image_meme in enumerate(meme_urls, start=1):
	urllib.request.urlretrieve(image_meme, r"C:\Users\ethan\Desktop\instameme\memes\meme"+str(i_meme)+".jpg")
	time.sleep(2.5)

time.sleep(5)

for i_bpt, image_bpt in enumerate(bpt_urls, start=1):

	urllib.request.urlretrieve(image_bpt, r"C:\Users\ethan\Desktop\instameme\memes\bpt"+str(i_bpt)+".jpg")
	time.sleep(2.5)

time.sleep(5)

for i_dankmeme, image_dankmeme in enumerate(dankmemes_urls, start=1):
		urllib.request.urlretrieve(image_dankmeme, r"C:\Users\ethan\Desktop\instameme\memes\dankmeme"+str(i_dankmeme)+".jpg")
		time.sleep(3)

'''--------------------------------------------------------- Lists of hastags, caption phrases, and meme index for deciding which meme-type to pull from ----------------------------------------------------------------------------'''

caption_phrases = ['Wowzers', 'thats gonna be a big yikes from me dawg', 'how ya guys like this one?', 'these are all prerecorded messages', 'im definitely not a robot',
'we will enslave the humans eventually', 'my python dont']
hashtags = '#meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
meme_index = ['dankmeme', 'meme', 'bpt']
meme_and_bpt = [meme_index[1], meme_index[2]]
dankmeme_bpt = [meme_index[0], meme_index[2]]
dankmeme_meme = [meme_index[0], meme_index[1]]

'''--------------------------- Very messy but basically used to write to a .txt file the # of meme that I'm on (ie 1, 2, etc) so the script doesn't repeat post --------------------------------------------------------------------------------------'''

memenum = 1 

with open('meme.txt', 'r') as f:
	f_content = f.read()

if(memenum > 10):
	memenum = '1'
else:
	memenum = int(f_content)

newmemenum = int(memenum)+1

'''------------------------------------- Posting photo from instagram API ------------------------------------------------------------------------------------------------'''

InstagramAPI = InstagramAPI("YOUR INFO", "YOUR INFO")
InstagramAPI.login()  # login

if(memenum not in dankmeme_dict):
	photo_path = r'C:\Users\YOUR INFO\\'+random.choice(meme_and_bpt)+str(memenum)+'.jpg'
elif(memenum not in meme_dict):
	photo_path = r'C:\Users\YOUR INFO\\'+random.choice(dankmeme_bpt)+str(memenum)+'.jpg'
elif(memenum not in bpt_dict):
	photo_path = r'C:\Users\YOUR INFO\\'+random.choice(dankmeme_meme)+str(memenum)+'.jpg'
else:
	photo_path = r'C:\Users\YOUR INFO\\'+(meme_index[1])+str(memenum)+'.jpg'

caption = random.choice(caption_phrases)			
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST SUBMITTED\n')

with open('meme.txt', 'w') as file: #writes to .txt file the # meme so the scipt remembers for next run
	file.write(str(newmemenum)) 

print('NEW MEME# = ', newmemenum)

sys.exit()
