import random
from Tkinter import *

class Application(Frame):
    
    billArray = ["Hi", "What\'d you say to me?", "Do I look like I drive cabs in Baton Rouge for fun?"]
    jeffArray = ["Yo", "Dude, that's so funny I forgot to laugh", "You know, you would get along well with my grandmother, she is really annoying too"]
    mattArray = ["Lemonade for sale", "You think you are better than me", "My dad could so beat your dad in a race"]                    

    def __init__(self, master):
        #initialize frame
        Frame.__init__(self,master)
        self.grid()
        
        #init arrays
        
        self.create_widgets()

    def generateRand(self):
        
        return randNum
    
    def billArrayFunction(self):
        #Start randNum
        random.seed()
        randNum = random.randint(0, 2)
        self.billLabel = Label(self)
        self.billLabel.grid()
        self.billLabel["text"] = self.billArray[randNum]

    def jeffArrayFunction(self):
        #Start randNum
        random.seed()
        randNum = random.randint(0, 2)
        self.jeffLabel = Label(self)
        self.jeffLabel.grid()
        self.jeffLabel["text"] = self.jeffArray[randNum]

    def mattArrayFunction(self):
        #Start randNum
        random.seed()
        randNum = random.randint(0, 2)
        self.mattLabel = Label(self)
        self.mattLabel.grid()
        self.mattLabel["text"] = self.mattArray[randNum]

    def create_widgets(self):
        #create buttons
        self.billButton = Button(self)
        self.billButton.grid()
        self.billButton["text"] = "Talk to Bill"
        self.billButton["command"] = self.billArrayFunction

        self.jeffButton = Button(self)
        self.jeffButton.grid()
        self.jeffButton["text"] = "Talk to Jeff"
        self.jeffButton["command"] = self.jeffArrayFunction

        self.mattButton = Button(self)
        self.mattButton.grid()
        self.mattButton["text"] = "Talk to Matt"
        self.mattButton["command"] = self.mattArrayFunction




root = Tk()
root.title("buttons")
root.geometry("1000x800")

app = Application(root)

root.mainloop()
