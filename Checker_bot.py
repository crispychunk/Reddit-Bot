# Reply checker bot
import config
import time as t
import praw
from datetime import datetime
def run_checker(r):

    with open("remindlist.txt") as f:
        lines = f.readlines()
        for line in lines:
            code = line.split(' ::: ')
            print(line)
            
            
            try:
                
                date = datetime.strptime(code[1], '%Y-%m-%d %H:%M:%S.%f') 
                if date < datetime.now():
                    print("removing")
                    reply_bot(code,line,r)  
            except:
                None
                #print("Error reading datetime")

def reply_bot(code,lineD,r):
    
    with open("remindlist.txt", "r") as f:
        lines = f.readlines()
    with open("remindlist.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != lineD.strip('\n'):
                print("cleaning: " , line)
                f.write(line)
    reply_message = 'Hello you requested to be reminded as of today for your comment:' + code[3] + '\n Link: ' + code[3] 
    r.redditor(code[0]).message("RemindmeBot",reply_message)


###############################################
r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Bootleg RemindMe Bot v0.1")
while True:
    t.sleep(3)
    run_checker(r)
