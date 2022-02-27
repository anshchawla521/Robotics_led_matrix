from typing import Text
import telebot
import time
import credentials 
import character_map

h=0
messages_list=[]
messages = ["hello" , "world"]
led_matrix = [[] , [] , [] ,[] ,[] , [] , [] ] #7*45 (7*40 be the visisble section)
s=set()
quotes = [
    '1. Celebarting 100th aniversary of PEC',
    '2. Robotics society',
    '3. Welcome President of INDIA',
    '4. Before software can be reusable it first has to be usable. – Ralph Johnson',
    '5. Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
]
# loop through the quotes


bot_token=credentials.bot_token
bot = telebot.TeleBot(bot_token)

def check_len():
    '''this function is checking the length of the message list if exceedes 1000 then delete 500 elements '''
    if(len(messages_list)>1000):# to be verified by ans we are deleting element once read by LED
        #have to be deleted in the set also
        
        while len(messages_list)>500:
           a= messages_list.pop(0)
           s.remove(a[1])
           

    pass

def get_message():
  
   # @bot.message_handler(commands=['Quote'])
    

    @bot.message_handler(commands=['Start','start'])
    def star_bot(message):
        for quote in quotes:
            bot.send_message(message.chat.id,quote)
                 
        bot.send_message(message.chat.id,"If you want to print 1st message then send /1 and same for other options.")
   
    
    
    
    @bot.message_handler(commands=['1','2','3'])
    def send_1(message):
        h=message.json['text'][1:]
        
        if(message.chat.id not in s):
            s.add(message.chat.id)
            
            bot.reply_to(message,'Your Request is accepted')
            a=[int(h),message.chat.id]
            messages_list.append(a)
        else:
            bot.reply_to(message,'Your request is already in queue')
        check_len()
        print(messages_list)
    
    
    
  

    
   
    bot.polling()
        

if __name__ == '__main__':
    #get_message() # implement a loop so that this bot checks for messages every 10 seconds or maybe multi threading

    message_mylist = list('helloworld')
    while len(message_mylist) != 0:
        if len(led_matrix[0]) >= 40 :
            for row in led_matrix:
                row.pop(0)
        if len(led_matrix[0]) < 40 :
            for col_num in range(0,5):
                #loop so that loop runs for all columns in character maps
                for row_num, row in enumerate(led_matrix):
                    # insert the col_num index element of rows of character map into the led_matrix array
                    row.append(character_map.map_of_letters[message_mylist[0].upper()][row_num][col_num])
            for row in led_matrix:
                #insert empty column / spacing between characters
                row.append(' ')
            message_mylist.pop(0)
        character_map.print_matrix(led_matrix)
    