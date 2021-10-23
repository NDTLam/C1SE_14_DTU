from datetime import date, datetime
 
you = "today"
if you == "":
    bot_brain = "I can't hear anything, please speak again"
elif you == "Hello":
    bot_brain = "Hello"
elif "today" in you:
        today = date.today()
        bot_brain = today.strftime("%B %d, %Y")
elif  you == "Joe Biden":
    bot_brain = "President of USA "
else:
    bot_brain = "I'm fine thank you"



print(bot_brain)