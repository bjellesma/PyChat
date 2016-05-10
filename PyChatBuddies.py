



class PyChatBuddies:
    __name = ""
    __height = 0
    __weight = 0
    __greetings = []
    __catch_phrase = ""
    __html_tag = ""

    def __init__(self, name, greetings, catch_phrase, chat_color, chat_font, html_tag):
        self.__name = name
        self.__greetings = greetings
        self.__catch_phrase = catch_phrase
        self.__chat_color = chat_color
        self.__html_tag = html_tag
        self.__chat_font = chat_font

    def set_name(self, name):
        #TODO validate input
        self.__name = name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        #TODO validate input
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_height(self, height):
        #TODO validate input
        self.__height = height

    def get_height(self):
        return self.__height

    def set_greetings(self, greetings):
        #TODO validate input
        self.__greetings = greetings

    def get_greetings(self):
        return self.__greetings

    def set_catch_phrase(self, catch_phrase):
        #TODO validate input
        self.__catch_phrase = catch_phrase

    def get_catch_phrase(self):
        return self.__catch_phrase

    def set_chat_color(self, chat_color):
        #TODO validate input
        self.__chat_color = chat_color

    def get_chat_color(self):
        return self.__chat_color

    def set_chat_font(self, chat_font):
        #TODO validate input
        self.__chat_font = chat_font

    def get_chat_font(self):
        return self.__chat_font

    #since the tag will not change, it makes sense to keep this read only
    def get_html_tag(self):
        return self.__html_tag

bill_the_conqueror = PyChatBuddies('Bill', ["Hi\n", "What\'d you say to me?\n", "Do I look like I drive cabs in Baton Rouge for fun?\n"], "Whats Cookin Good Lookin", 'blue', ("Georgia", "12", "bold"), 'bill_the_conqueror_tag')
matt_the_unstable = PyChatBuddies('Matt', ["Lemonade for sale\n", "You think you are better than me\n", "My dad could so beat your dad in a race\n"], "Yup Yup Yup", 'red', ("Georgia", "12", "bold"), 'matt_the_unstable_tag')
jeff_the_grand = PyChatBuddies('Jeff', ["Yo\n", "Dude, that's so funny I forgot to laugh\n", "You know, you would get along well with my grandmother, she is really annoying too\n"], "Whats Crackalackin", 'green', ("Georgia", "12", "bold"), 'jeff_the_grand_tag')
