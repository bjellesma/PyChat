import random
#Graphics Library
from Tkinter import *

class Application(Frame):
    #create global variables
    buddies = ['billButton', 'jeffButton', 'mattButton']
    buttonNames = {'billButton': {'varName': 'buttonBill'}, 'jeffButton': {'varName': 'buttonJeff'}, 'mattButton': {'varName': 'buttonMatt'}}
    billArray = ["Hi", "What\'d you say to me?", "Do I look like I drive cabs in Baton Rouge for fun?"]
    jeffArray = ["Yo", "Dude, that's so funny I forgot to laugh", "You know, you would get along well with my grandmother, she is really annoying too"]
    mattArray = ["Lemonade for sale", "You think you are better than me", "My dad could so beat your dad in a race"]
    buttons = {'billButton': {'name': 'Bill', 'label': 'billLabel', 'text': 'Talk to Bill', 'textColor': 'blue', 'array': billArray},
               'jeffButton': {'name': 'Jeff', 'label': 'jeffLabel', 'text': 'Talk to Jeff', 'textColor': 'blue', 'array':jeffArray},
               'mattButton': {'name': 'Matt', 'label': 'mattLabel', 'text': 'Talk to Matt', 'textColor': 'red', 'array': mattArray}}
    randNum = 0
    """
    function to initialize frame
    """
    def __init__(self, master):
        #initialize frame
        Frame.__init__(self,master)
        self.grid()
        #create buttons
        self.create_widgets()
    """
    function to generate random integers
    """
    def generateRand(self, size):
        #seed the randomness
        random.seed()
        #declaration allows us to modify global variable
        global randNum
        #random number between 0 and size of list -1 (to account for zero indexing
        randNum = random.randint(0, size - 1)
        return randNum
    """
    function to generate Bill's Messages
    """
    def chat(self, buddy, arrayName, chatColor):
        #generate random int between 0 and list size
        randNum = self.generateRand(len(arrayName))
        #generate label
        self.labelName = Label(self)
        #add label to frame
        self.labelName.grid()
        #add text attribute
        self.labelName["text"] = buddy + ": " + arrayName[randNum]
        #add text color
        self.labelName["fg"] = chatColor

    """
    function to create initial widgets
    """
    def create_widgets(self):
        """
        Using a loop is infesible because the value of i will always be used and generate the phrases of the last buddies in the array
        best fix for right now is to use a finite number of buddies
        """
        #create buttons
        self.buttonNames[self.buddies[0]]['varName'] = Button(self)
        self.buttonNames[self.buddies[0]]['varName'].grid()
        self.buttonNames[self.buddies[0]]['varName']["text"] = self.buttons[self.buddies[0]]['text']
        #add event handler
        #use lambda to avoid immediable invokation
        self.buttonNames[self.buddies[0]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[0]]['name'], self.buttons[self.buddies[0]]['array'], self.buttons[self.buddies[0]]['textColor'])
        
        self.buttonNames[self.buddies[0]]['varName'] = Button(self)
        self.buttonNames[self.buddies[0]]['varName'].grid()
        self.buttonNames[self.buddies[0]]['varName']["text"] = self.buttons[self.buddies[0]]['text']
        #add event handler
        #use lambda to avoid immediable invokation
        self.buttonNames[self.buddies[0]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[0]]['name'], self.buttons[self.buddies[0]]['array'], self.buttons[self.buddies[0]]['textColor'])

        self.buttonNames[self.buddies[1]]['varName'] = Button(self)
        self.buttonNames[self.buddies[1]]['varName'].grid()
        self.buttonNames[self.buddies[1]]['varName']["text"] = self.buttons[self.buddies[1]]['text']
        self.buttonNames[self.buddies[1]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[1]]['name'], self.buttons[self.buddies[1]]['array'], self.buttons[self.buddies[1]]['textColor'])

        self.buttonNames[self.buddies[2]]['varName'] = Button(self)
        self.buttonNames[self.buddies[2]]['varName'].grid()
        self.buttonNames[self.buddies[2]]['varName']["text"] = self.buttons[self.buddies[2]]['text']
        self.buttonNames[self.buddies[2]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[2]]['name'], self.buttons[self.buddies[2]]['array'], self.buttons[self.buddies[2]]['textColor'])

#variable to take on main library
root = Tk()
#title of frame
root.title("buttons")
#frame size
root.geometry("1000x800")
#making the application the root
app = Application(root)
#starting the main loop
root.mainloop()
