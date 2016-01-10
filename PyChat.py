import random
#Graphics Library
from Tkinter import *
from ScrolledText import ScrolledText
#variable to take on main library
root = Tk()
#title of frame
root.title("PyChat")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

class Application(Frame):
    #create global variables
    buddies = ['billButton', 'jeffButton', 'mattButton']
    buttonNames = {'billButton': {'varName': 'buttonBill'}, 'jeffButton': {'varName': 'buttonJeff'}, 'mattButton': {'varName': 'buttonMatt'}}
    billArray = ["Hi\n", "What\'d you say to me?\n", "Do I look like I drive cabs in Baton Rouge for fun?\n"]
    jeffArray = ["Yo\n", "Dude, that's so funny I forgot to laugh\n", "You know, you would get along well with my grandmother, she is really annoying too\n"]
    mattArray = ["Lemonade for sale\n", "You think you are better than me\n", "My dad could so beat your dad in a race\n"]
    buttons = {'billButton': {'name': 'Bill', 'label': 'billLabel', 'text': 'Talk to Bill', 'textColor': 'blue', 'array': billArray},
               'jeffButton': {'name': 'Jeff', 'label': 'jeffLabel', 'text': 'Talk to Jeff', 'textColor': 'green', 'array':jeffArray},
               'mattButton': {'name': 'Matt', 'label': 'mattLabel', 'text': 'Talk to Matt', 'textColor': 'red', 'array': mattArray}}
    randNum = 0
    """
    function to initialize frame
    """
    def __init__(self, master):
        #initialize frame
        Frame.__init__(self,master)
        self.grid(row =0, column = 0)
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
        self.labelName = Text(self)
        self.chatbox.insert('insert', buddy + ": " + arrayName[randNum])

    """
    function to create initial widgets
    """
    def create_widgets(self):
        """
        Using a loop is infesible because the value of i will always be used and generate the phrases of the last buddies in the array
        best fix for right now is to use a finite number of buddies
        """
        self.chatbox = ScrolledText(self, wrap = 'word', width = 25, height = 10, bg = 'beige')
        self.chatbox.grid(row = 0, column = 0, rowspan =7, columnspan =7)
        #create buttons
        self.buttonNames[self.buddies[0]]['varName'] = Button(self)
        self.buttonNames[self.buddies[0]]['varName'].grid(row = 8, column = 8, columnspan = 2)
        self.buttonNames[self.buddies[0]]['varName']["text"] = self.buttons[self.buddies[0]]['text']
        #add event handler
        #use lambda to avoid immediable invokation
        self.buttonNames[self.buddies[0]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[0]]['name'], self.buttons[self.buddies[0]]['array'], self.buttons[self.buddies[0]]['textColor'])

        self.buttonNames[self.buddies[1]]['varName'] = Button(self)
        self.buttonNames[self.buddies[1]]['varName'].grid(row = 9, column = 9)
        self.buttonNames[self.buddies[1]]['varName']["text"] = self.buttons[self.buddies[1]]['text']
        self.buttonNames[self.buddies[1]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[1]]['name'], self.buttons[self.buddies[1]]['array'], self.buttons[self.buddies[1]]['textColor'])

        self.buttonNames[self.buddies[2]]['varName'] = Button(self)
        self.buttonNames[self.buddies[2]]['varName'].grid(row = 9, column = 8)
        self.buttonNames[self.buddies[2]]['varName']["text"] = self.buttons[self.buddies[2]]['text']
        self.buttonNames[self.buddies[2]]['varName']["command"] = lambda: self.chat(self.buttons[self.buddies[2]]['name'], self.buttons[self.buddies[2]]['array'], self.buttons[self.buddies[2]]['textColor'])


#frame size
root.geometry()
#making the application the root
app = Application(root)
#starting the main loop
root.mainloop()
