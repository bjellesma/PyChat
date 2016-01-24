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
    buddies = ['Bill', 'Jeff', 'Matt']
    chatColors = ['billColor', 'jeffColor', 'mattColor']
    chatArray = [
                          #Bill
                          ["Hi\n", "What\'d you say to me?\n", "Do I look like I drive cabs in Baton Rouge for fun?\n"], 
                          #Jeff
                          ["Yo\n", "Dude, that's so funny I forgot to laugh\n", "You know, you would get along well with my grandmother, she is really annoying too\n"],
                          #Matt
                          ["Lemonade for sale\n", "You think you are better than me\n", "My dad could so beat your dad in a race\n"]
                          ]
    randNum = 0
    #TODO: These will eventually be dynamically gotten
    userName = "Tester"
    userColor = "Purple"
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
    function for user input
    """
    def userInput(self, userName):
         #get text from input field
        lastResponse = self.inputField.get()
        userIndex = self.chatbox.index("insert")
        self.chatbox.insert('insert', userName + ": " + lastResponse + "\n")
        self.chatbox.tag_add("userColor", userIndex + "", "insert")
    """
    Function for the AI to think of a response
    """
    def chatThink(self, event):
        #Make a copy of the username global variable
        userName = self.userName
        self.userInput(userName)
        #You do need to use the insert method after the delete method, as shown below
        self.inputField.delete(0, END)
        self.inputField.insert(0, "")
        self.inputField.configure(state='disabled')
        
        #choose random buddy
        randNumBuddy = self.generateRand(len(self.buddies))
        buddy = self.buddies[randNumBuddy]
        #choose chat color
        chatColorTag = self.chatColors[randNumBuddy]
        #choose random chat
        randNumChat = self.generateRand(len(self.buddies))
        chat = self.chatArray[randNumBuddy][randNumChat]
        #find the index to start the text coloring
        index = self.chatbox.index('insert')
        self.chatRespond(buddy, chat, chatColorTag, index)
        self.inputField.configure(state='normal')

    """
    function to generate Bill's Messages
    """
    def chatRespond(self, buddy, chat, chatColorTag, index):
        self.chatbox.insert('insert', buddy + ": " + chat)
        self.chatbox.tag_add(chatColorTag, index + "", "insert")
        #scroll to end
        self.chatbox.see('end')
    """
    function to create initial widgets
    """
    def create_widgets(self):
        """
        Using a loop is infesible because the value of i will always be used and generate the phrases of the last buddies in the array
        best fix for right now is to use a finite number of buddies
        """
        #username label
        #TODO: Make Seperate screen to enter name
        self.userNameLabel = Label(self, text = self.userName)
        self.userNameLabel.grid(row = 8, column = 0)
        #chatbox
        self.chatbox = ScrolledText(self, wrap = 'word', width = 50, height = 20, bg = 'beige')
        self.chatbox.grid(row = 0, column = 0, rowspan =7, columnspan =7)
        #setting colors
        self.chatbox.tag_config("userColor", foreground = self.userColor)
        self.chatbox.tag_config("billColor", foreground="Blue")
        self.chatbox.tag_config("jeffColor", foreground="Green")
        self.chatbox.tag_config("mattColor", foreground="Red")
        #input field
        self.inputField = Entry(self)
        self.inputField.grid(row =8, column = 6)
        self.inputField.bind('<Return>', self.chatThink)


#frame size
root.geometry("")
#making the application the root
app = Application(root)
#starting the main loop
root.mainloop()
