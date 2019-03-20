import androidhelper
import time

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def phone_reader(phone_num):
    phone_num = phone_num[2::]
    phone_num = " ".join(phone_num)
    return phone_num

def read_aloud(messages):
    for index, message in enumerate (messages):
        mess_num = ordinal(index + 1)
        droid.ttsSpeak(mess_num + " unread message.")
        droid.ttsSpeak("From " + phone_reader(message['address']))
        time.sleep(2.5)
        droid.ttsSpeak(message['body'])
        time.sleep(2.5)
    
    droid.ttsSpeak("This is the end of your unread messages. Goodbye!")
                   
droid = androidhelper.Android()

unreads = droid.smsGetMessages(unreadOnly=True)
messages = unreads[1]
messages.reverse()
num_messages = len(messages)
print(unreads)

droid.ttsSpeak("Welcome to your unread messages box! You currently have "
	+ str(num_messages) + " unread text messages.")   
	 
if num_messages == 0:
    droid.ttsSpeak("Goodbye!")
else:
    read_aloud(messages)

droid.ttsSpeak("Welcome to your unread messages box! You currently have "
	+ str(num_messages) + " unread text messages.")   
	 
if num_messages == 0:
    droid.ttsSpeak("Goodbye!")
else:
    read_aloud(messages)
