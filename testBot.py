#!/usr/bin/python
import praw
import pdb
import re
import os

#Create reddit instance
reddit = praw.Reddit('bot1')

#if this hasn't been run, create empty list
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

#if we already have a list for post id's, open it
else:
	#read file into list and split on \n, also remove empty entries
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#grab top 5 values from subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
	#print(submission.title)

	#if we haven't replied yet
	if submission.id not in posts_replied_to:

		#Do case insensitive search
		if re.search("i love python", submission.title, re.IGNORECASE):
			#reply to the post
			submission.reply("Nice")
			print("Bot replying to : ",submission.title)

		#store the current id into our replied to list
		posts_replied_to.append(submission.id)

#write updated list back to the file
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
