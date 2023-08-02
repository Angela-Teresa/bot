from tkinter import *
import re
import random


wind = Tk()
wind.title(" BOT ")
wind.geometry("600x650")
wind.configure(bg="pink")
xi = 0
yi = 0
def send_message():
    global yi
    u = user_entry.get()
    user = Label(chat_bg,height=1,width=53,bg='#f5cbf1',fg='black',text=u,font=12,anchor='e')
    user.place(x=xi,y=yi)
    bot = Label(chat_bg,height=1,width=64,bg='#f7bbfa',fg='black',text= get_response(u),font=12,anchor='w')
    bot.place(x=xi,y=yi+25) 
    yi+=50
    user_entry.delete(0,'end')


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response = False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)    

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank You!', ['i','love','like','you'],required_words=['i','you'])

    response("I don't like eating anything because i'm a bot obviously!", ['what', 'you', 'eat'], required_words=['you','eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    def unknown():
        response=['Could you please re-phrase that?', '...', 'sounds about right', 'what does that mean?'][random.randrange(4)]
        return response

    return unknown() if highest_prob_list[best_match] < 1 else best_match
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
   
hcb_text = Label(height=1, width=30, bg='violet' ,text='Bot Buddy' ,font=('Courier',20), fg='white' )
hcb_text.place(x=55,y=15)
chat_bg = Frame(height=420, width=650, bg='#f2daf2')
chat_bg.place(x=10,y=80)

entry_bg = Frame(height=60, width=500, bg='violet')
entry_bg.place(x=10,y=520)

c= Canvas(wind,width=52, height=57)
c.pack()
c.place(x=525,y=520)

user_entry= Entry(entry_bg, width=32, bg='white', font=('normal',20),relief=FLAT, border=0 )
user_entry.place(x=10,y=13)

user_entry.delete(0,'end')
send_button = Button(height=1,width=3,bg='violet', text='▶',fg='white', font=('Roman',20),activeforeground='white', relief=FLAT,border=0,activebackground='#f7bbfa',command=send_message)
send_button.place(x=530,y=525)

wind.mainloop()


