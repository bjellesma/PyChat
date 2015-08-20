import random

def conversation(member):
    random.seed()
    randNum = random.randint(0, 2)
    if member == 'Bill':
        print billArray[randNum]
    if member == 'Jeff':
        print jeffArray[randNum]
    if member == 'Matt':
        print mattArray[randNum]
    confirm = raw_input('Would you like to talk to anyone else?')
    if confirm == 'yes':
        member = raw_input('Who?')
        conversation(member)
    if confirm == 'no':
        return
    return

billArray = ["Hi", "What\'d you say to me?", "Do I look like I drive cabs in Baton Rouge for fun?"]
jeffArray = ["Yo", "Dude, that's so funny I forgot to laugh", "You know, you would get along well with my grandmother, she is really annoying too"]
mattArray = ["Lemonade for sale", "You think you are better than me", "My dad could so beat your dad in a race"]

member = raw_input('Hi, who would you like to talk to?')
conversation(member)

