class Chat:
    
    def __init__(self):
        self.human_dialogue = []
        self.robot_dialogue = []
        self.to_0 = 'aeiouAEIOU'
        
    def connect_robot(self, robot):
        # connects robot to the chat
        self.robot = robot
        robot.chat = self
    
    def connect_human(self, human):
        # connects human to the chat
        self.human = human
        human.chat = self
        
    def add_message(self, message, from_who):
        who = f"{from_who} said: "
        robot_message = "".join(["0" if char in self.to_0 else "1" for char in message])
        self.human_dialogue.append(who + message)
        self.robot_dialogue.append(who + robot_message)
    
        
    def show_human_dialogue(self):
        return "\n".join(self.human_dialogue)
    
    def show_robot_dialogue(self):
        return "\n".join(self.robot_dialogue)

class Human:
    
    def __init__(self, name):
        self.name = name
    
    def send(self, message):
        self.chat.add_message(message, self.name)
        self.message = message

class Robot:
    
    def __init__(self, serial_number):
        self.serial_number = serial_number
        
    def send(self, message):
        self.chat.add_message(message, self.serial_number)
        self.message = message


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_robot_dialogue())
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new? 
    R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011 
    R2D2 said: 10110111010111100111101110011101011010011011"""
    print("Coding complete? Let's try tests!")