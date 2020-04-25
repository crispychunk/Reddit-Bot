import praw
import config
from datetime import date
from datetime import timedelta
from datetime import datetime

def login():
    
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "SFU RemindMe Bot v0.1")
    return r
    
keyword = '!remindme'
def run_bot(r):
    subreddit = r.subreddit("testingforbots123")
    for comment in subreddit.stream.comments():
        if keyword in comment.body:
            analyze_bot(comment)
    

def analyze_bot(comment):
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
    if ' hour ' in text:
        date = date.partition(' ')
        time = datetime.now()
        print(time)
        
        #reply_bot(,message,comment)
    #if ' Months ' in text:
    #if ' Week ' in text:
    #if 'Day' in text:
    #if 'hour' in text:
       # print(text)
    #if 'Minute'in text:
    #if 'EOY' in text:
    #if 'EOM' in text:
    #if 'EOD' in text:



    

#def reply_bot(time,reply_message,comment):
        
    
        
# main functions
r = login()
run_bot(r)
