import random
#Graphics Library
from Tkinter import *

class Application(Frame):
    #create global variables
    billArray = ["Hi", "What\'d you say to me?", "Do I look like I drive cabs in Baton Rouge for fun?"]
    billTextColor = "blue"
    jeffArray = ["Yo", "Dude, that's so funny I forgot to laugh", "You know, you would get along well with my grandmother, she is really annoying too"]
    jeffTextColor = "yellow"
    mattArray = ["Lemonade for sale", "You think you are better than me", "My dad could so beat your dad in a race"]
    mattTextColor = "red"
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
        #create buttons
        self.billButton = Button(self)
        self.billButton.grid()
        self.billButton["text"] = "Talk to Bill"
        #add event handler
        #use lambda to avoid immediable invokation
        self.billButton["command"] = lambda: self.chat("Bill", self.billArray, self.billTextColor)

        self.jeffButton = Button(self)
        self.jeffButton.grid()
        self.jeffButton["text"] = "Talk to Jeff"
        self.jeffButton["command"] = lambda: self.chat("Jeff", self.jeffArray, self.jeffTextColor)

        self.mattButton = Button(self)
        self.mattButton.grid()
        self.mattButton["text"] = "Talk to Matt"
        self.mattButton["command"] = lambda: self.chat("Matt", self.mattArray, self.mattTextColor)



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
