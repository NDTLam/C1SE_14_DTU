import pyttsx3

bot_brain = "Hello"


bot_mouth = pyttsx3.init()
bot_mouth.say(bot_brain)
bot_mouth.runAndWait()