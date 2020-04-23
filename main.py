import praw
import config
import time
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

    # Now analyze when to reply

    
    #if ' Year ' in text:
    #if ' Months ' in text:
    #if ' Week ' in text:
    #if 'Day' in text:
    if 'hour' in text:
        print(text)
    #if 'Minute'in text:
    #if 'EOY' in text:
    #if 'EOM' in text:
    #if 'EOD' in text:


    # Now find message and store it
    

def reply_bot(time,message,comment):

    
        
# main functions
r = login()
run_bot(r)
