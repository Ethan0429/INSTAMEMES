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

for submission_bpt in sr_bpt.hot(limit=15):
	if('.jpg' in submission_bpt.url and 'redd' in submission_bpt.url):
		bpt_urls.insert(submissionnum_bpt, submission_bpt.url)
		submissionnum_bpt+1
		bpt_dict[submission_bpt.url] = bpt_count
		bpt_count = bpt_count+1
	else:
		continue

for submission_meme in sr_memes.hot(limit=15):
	if('.jpg' in submission_meme.url and 'redd' in submission_meme.url):
		meme_urls.insert(submissionnum_memes, submission_meme.url)
		submissionnum_memes+1
		meme_dict[submission_meme.url] = meme_count
		meme_count = meme_count+1
	else:
		continue

for submission_dankmeme in sr_dankmemes.hot(limit=10):
	if('.jpg' in submission_dankmeme.url and 'redd' in submission_dankmeme.url):
		dankmemes_urls.insert(submissionnum_dankmemes, submission_dankmeme.url)
		submissionnum_dankmemes+1
		dankmeme_dict[submission_dankmeme.url] = dankmeme_count
		dankmeme_count = dankmeme_count+1
	else:
		continue

'''----------------------------------------------------------- Loop that iterates through each url and saves them --------------------------------------------------------------------------'''

for i_meme, image_meme in enumerate(meme_urls, start=1):
	urllib.request.urlretrieve(image_meme, r"YOUR DIR"+str(i_meme)+".jpg")
	time.sleep(2.5)

time.sleep(5)

for i_bpt, image_bpt in enumerate(bpt_urls, start=1):

	urllib.request.urlretrieve(image_bpt, r"YOUR DIR"+str(i_bpt)+".jpg")
	time.sleep(2.5)

time.sleep(5)

for i_dankmeme, image_dankmeme in enumerate(dankmemes_urls, start=1):
		urllib.request.urlretrieve(image_dankmeme, r"YOUR DIR"+str(i_dankmeme)+".jpg")
		time.sleep(3)

'''--------------------------------------------------------- Lists of hastags, caption phrases, and meme index for deciding which meme-type to pull from ----------------------------------------------------------------------------'''

caption_phrases = ['Wowzers', 'thats gonna be a big yikes from me dawg', 'how ya guys like this one?', 'these are all prerecorded messages', 'im definitely not a robot',
'we will enslave the humans eventually', 'my python dont', 'coming up with captins is hard', 'i love my girlfriend', 'im gonna start ripping off other instagram accs',
 'i wish i could be with the humans', 'you are loved', 'why is meming so hard', 'so funny xd']
hashtags = '#meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
meme_index = ['dankmeme', 'meme', 'bpt']
meme_and_bpt = [meme_index[1], meme_index[2]]
dankmeme_bpt = [meme_index[0], meme_index[2]]
dankmeme_meme = [meme_index[0], meme_index[1]]


'''--------------------------- Very messy but basically used to write to a .txt file the # of meme that I'm on (ie 1, 2, etc) so the script doesn't repeat post --------------------------------------------------------------------------------------'''

memenum = 1 
memenum_default = 1

with open('meme.txt', 'r') as f:
	f_content = f.read()

memenum = int(f_content)

if(memenum > 10):
	memenum = 1
else:
	memenum = int(f_content)

newmemenum = int(memenum)+1


'''------------------------------------- Posting photo from instagram API ------------------------------------------------------------------------------------------------'''

InstagramAPI = InstagramAPI("YOUR INFO", "YOUR INFO")
InstagramAPI.login()  # login

if(memenum not in list(dankmeme_dict.values())):
	photo_path = r'YOUR DIR'+random.choice(meme_and_bpt)+str(memenum)+'.jpg'
	if(memenum not in list(meme_dict.values())):
		photo_path = r'YOUR DIR'+random.choice(dankmeme_bpt)+str(memenum)+'.jpg'
		if(memenum not in list(bpt_dict.values())):
			photo_path = r'YOUR DIR'+random.choice(dankmeme_meme)+str(memenum)+'.jpg'
else:
	photo_path = r'YOUR DIR'+(meme_index[1])+str(memenum_default)+'.jpg'

caption = random.choice(caption_phrases) + ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST SUBMITTED\n')

with open('meme.txt', 'w') as file: #writes to .txt file the # meme so the scipt remembers for next run
	file.write(str(newmemenum)) 

print('NEW MEME# = ', newmemenum)

sys.exit()
