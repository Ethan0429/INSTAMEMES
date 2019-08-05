import sys
import praw #pip install praw
import time
import urllib
import random
from PIL import Image
from InstagramAPI import InstagramAPI #pip install InstagramApi
from resizeimage import resizeimage

while True:    
    '''-------------------------------------------------------- Reddit API setup -----------------------------------------------------------------------------'''

reddit_p = praw.Reddit(client_id='clienid',
						client_secret='secret',
						user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36')

sr_memes = reddit_p.subreddit('sub1')
sr_dankmemes = reddit_p.subreddit('sub2')
sr_bpt = reddit_p.subreddit('sub3')

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

meme_index = ['dankmeme', 'meme', 'bpt']
meme_and_bpt = [meme_index[1], meme_index[2]]
dankmeme_bpt = [meme_index[0], meme_index[2]]
dankmeme_meme = [meme_index[0], meme_index[1]]

'''--------------------------- Very messy but basically used to write to a .txt file the # of meme that I'm on (ie 1, 2, etc) so the script doesn't repeat post --------------------------------------------------------------------------------------'''

memenum = 1 
memenum_default = 1

with open('YOUR DIR1.jpg', 'r+b') as f:
	
	with Image.open(f) as image:
        
		cover = resizeimage.resize_cover(image, [600, 400])
       
		cover.save('YOUR DIR1.jpg', image.format)	
		with open('YOUR DIR2.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR2.jpg', image.format)	
		with open('YOUR DIR3.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR3.jpg', image.format)
		with open('YOUR DIR4.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR4.jpg', image.format)
		with open('YOUR DIR5.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR5.jpg', image.format)
		with open('YOUR DIR6.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR6.jpg', image.format)
		with open('YOUR DIR7.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR7.jpg', image.format)
		with open('YOUR DIR8.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR8.jpg', image.format)
		with open('YOUR DIR9.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR9.jpg', image.format)
		with open('YOUR DIR10.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR10.jpg', image.format)
		with open('YOUR DIR11.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR11.jpg', image.format)
		with open('YOUR DIR12.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR12.jpg', image.format)
		with open('YOUR DIR13.jpg', 'r+b') as f:
			with Image.open(f) as image:	
				cover = resizeimage.resize_cover(image, [600, 400])	
       
		cover.save('YOUR DIR13.jpg', image.format)
'''------------------------------------- Posting photo from instagram API ------------------------------------------------------------------------------------------------'''

InstagramAPI = InstagramAPI("username", "password")
InstagramAPI.login()  # login




photo_path = r'YOUR DIR1.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 1 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR2.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 2 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR3.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 3 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR4.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 4 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR5.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 5 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR6.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 6 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR7.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 7 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR8.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 8 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR9.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 9 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR10.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 10 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR11.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 11 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR12.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 12 SUBMITTED\n')

time.sleep(3)

photo_path = r'YOUR DIR13.jpg'

caption = ' #meme #memes #funny #dankmemes #dank #lol #lmao #dank #funnymemes #memesdaily #dankmeme #f #dankmemes #follow #cringe #like #lmfao #anime #hilarious #autism #comedy #offensivememes #fortnite #filthyfrank #nichememes #offensive #jokes #cancer #l #bhfyp'
InstagramAPI.uploadPhoto(photo_path, caption=caption)

print('\nPOST 13 SUBMITTED\n')

time.sleep(3)


time.sleep(1800)
