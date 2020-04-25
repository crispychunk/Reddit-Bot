import praw
import config
from datetime import date
from datetime import timedelta
from datetime import datetime
import time as t
from multiprocessing import Pool
from threading import Thread

    
def run_bot():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Bootleg RemindMe Bot v0.1")
    keyword = '!remindme'
    subreddit = r.subreddit("testingforbots123")
    for comment in subreddit.stream.comments(skip_existing= True):
        if keyword in comment.body:
            print(comment.body)
            analyze_bot(comment,r)


    
def analyze_bot(comment,r):
    # Remove remind me
    text = comment.body
    text = text.replace('!remindme ','')
    date = text # auto think that the rest is just date
    # Now to check if  there is a message and store it
    pos1 = text.find('"')
    if pos1 != -1: # If quotations are seen
        pos2 = text.find('"', pos1+1)
        message = text[pos1+1:pos2] # get message
        date = text.replace(text[pos1:pos2+1],'') # update date to exclude message
        
    
    else: # That means no mesage was specified
        message = "No message was specified"
    #print(message)
        
    # Now analyze when to reply
    try:
        if ' hours ' in text or 'hour' in text:
            date = date.partition(' ')
            reply_time = datetime.now() + timedelta(hours = int(date[0]))
            reply_bot(reply_time,message,comment,r)
        elif 'month' in text or 'months' in text:
            date = date.partition(' ')
            reply_time = datetime.now() + timedelta(months = int(date[0]))
            reply_bot(reply_time,message,comment,r)
        elif 'week' in text or 'weeks' in text:
            date = date.partition(' ')
            reply_time = datetime.now() + timedelta(weeks = int(date[0]))
            reply_bot(reply_time,message,comment,r)
        elif 'day' in text or 'days' in text :
            date = date.partition(' ')
            reply_time = datetime.now() + timedelta(days = int(date[0]))
            reply_bot(reply_time,message,comment,r)
        elif 'minute' in text or 'minutes' in text:
            date = date.partition(' ')
            reply_time = datetime.now() + timedelta(minutes = int(date[0]))
            reply_bot(reply_time,message,comment,r)

    except:
        print("ERROR in reading time")
# reply function and write to memory
def reply_bot(time,reply_message,comment,r):
    subject = "BootlegRemindMe"
    body = 'Hello ' + str(comment.author) + ',I am RemindmeBot. You requests me to remind you on : ' + str(time) + '\n This is a reminder for the comment: \n' + comment.permalink
    print(comment.author)
    print(body)
    user = str(comment.author)
    r.redditor(user).message(subject, body)
    code = str(comment.author) + ' ::: ' + str(time) + ' ::: ' + reply_message + ' ::: ' + str(comment.permalink) + '\n' 
    f = open("remindlist.txt","a")
    f.write(code)
    
run_bot()

