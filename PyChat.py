import random
#Graphics Library
from Tkinter import *
from tkColorChooser import askcolor 
from ScrolledText import ScrolledText
import tkMessageBox
#variable to take on main library
root = Tk()

#title of frame
#root.title("PyChat")
#root.rowconfigure(0, weight = 1)
#root.columnconfigure(0, weight = 1)



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
    userName = ""
    userColor = ""
    """
    function to initialize frame
    """
    def __init__(self, master):
        #initialize frame
        Frame.__init__(self,master)
        self.grid(row =0, column = 0)
        #screen to ask user for input
        self.login_screen()

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
    function to validate username input 
    """
    def inputValidate(self, event):
        #TODO validate input
        self.userName = self.inputField.get()
        #make a copy to a local variable
        userName = self.userName
        tkMessageBox.showinfo('UserName', 'Your name is ' + userName)
         #create chat
        self.chat_screen()
        #create friends list
        #self.friends_screen()
    """
    function to create initial widgets
    """
    def login_screen(self):
        """
        Using a loop is infesible because the value of i will always be used and generate the phrases of the last buddies in the array
        best fix for right now is to use a finite number of buddies
        """
        root.title("Enter a username")
        self.enterLabel = Label(self, text = "Please enter a username")
        self.enterLabel.grid(row = 2, column = 2, columnspan = 2)
        #username input field
        self.inputField = Entry(self)
        self.inputField.grid(row =3, column = 3)
        self.inputField.bind('<Return>', self.inputValidate)
        
    """
    function to create initial widgets
    """
    def chat_screen(self):
        """
        Using a loop is infesible because the value of i will always be used and generate the phrases of the last buddies in the array
        best fix for right now is to use a finite number of buddies
        """
        root.title("PyChat")
        userName = self.userName
        userColor = self.userColor
        #username label
        #TODO: Make Seperate screen to enter name
        self.userNameLabel = Label(self, text = userName)
        self.userNameLabel.grid(row = 8, column = 0)
        #chatbox
        self.chatbox = ScrolledText(self, wrap = 'word', width = 50, height = 20, bg = 'beige')
        self.chatbox.grid(row = 0, column = 0, rowspan =7, columnspan =7)
        #setting colors
        self.chatbox.tag_config("userColor", foreground = userColor)
        self.chatbox.tag_config("billColor", foreground="Blue")
        self.chatbox.tag_config("jeffColor", foreground="Green")
        self.chatbox.tag_config("mattColor", foreground="Red")
        #input field
        self.inputField = Entry(self)
        self.inputField.grid(row =8, column = 6)
        self.inputField.bind('<Return>', self.chatThink)
    """
    function to create profile widgets
    """
    def profile_screen(self):
        username = self.userName
        userColor = self.userColor
        #TODO user picture
        #username 
        #self.userNameLabel = Label(self, text = "username: " + userName)
        #TODO create change button
    """
    function to create friends list
    """
    def friends_screen(self):
        root2.title("friends list")
        self.friendLabel = Label(self, text = "test")
        self.friendLabel.grid(row = 0, column = 0)
#frame size
root.geometry("")

#making the application the root
app = Application(root)
#starting the main loop
root.mainloop()

import tkMessageBox