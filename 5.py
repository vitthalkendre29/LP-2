from chatterbot import ChatBot 
#pip install chatterbot

from chatterbot.trainers import ListTrainer  

chatbot = ChatBot("DailyLifeBot") 

conversation = [ 
    "Hello", 
    "Hi there! How's your day going?", 
    "Hi", 
    "Hey! What’s up?", 
    "Good morning", 
    "Good morning! Hope you have a great day ahead.", 
    "Good night", 
    "Good night! Sweet dreams.", 
    "How are you?", 
    "I'm doing great! Thanks for asking. How about you?", 
    "What’s the weather like?", 
    "I'm not sure, but it’s always a good idea to check your local weather app!", 
    "What’s your favorite food?", 
    "I love pizza! What's your favorite?", 
    "What are your hobbies?", 
    "I love chatting with people and learning new things!", 
    "Tell me a joke", 
    "Why don’t scientists trust atoms? Because they make up everything!", 
    "Bye", 
    "Goodbye! Talk to you later!", 
    "See you", 
    "See you soon! Take care." 
] 

# Train chatbot 
trainer = ListTrainer(chatbot) 
trainer.train(conversation) 

# Function to interact with chatbot 
def daily_life_chatbot(): 
    print("Hello! I'm DailyLifeBot. Chat with me! (Type 'exit' to leave)")
    while True:
        user_input = input("You: ") 
        if user_input.lower() == "exit": 
            print("DailyLifeBot: Bye! Have a wonderful day!") 
            break 
        response = chatbot.get_response(user_input) 
        print(f"DailyLifeBot: {response}") 

# Start chatbot interaction 
daily_life_chatbot()
