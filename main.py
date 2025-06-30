from termcolor import colored
from colorama import init

init()  # Enables color support on Windows

print(colored("Welcome to Chatbot! Type 'bye' to exit.\n", "green"))

responses = {
    "hello": "Hi there! How can I assist you?",
    "hi": "Hello! Ask me anything.",
    "how are you": "I'm doing great! Thanks for asking.",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!",
    "what is your name": "I'm a simple Python chatbot.",
    "help": "You can ask me about greetings, my name, or general questions."
}

while True:
    user_input = input(colored("You: ", "cyan")).lower().strip()

    if not user_input:
        continue

    found = False
    for key in responses:
        if key in user_input:
            print(colored("Bot: " + responses[key], "yellow"))
            found = True
            if key == "bye":
                exit()
            break

    if not found:
        if "name" in user_input:
            print(colored("Bot: I'm a Python chatbot, I don't have a fancy name yet!", "yellow"))
        elif "age" in user_input:
            print(colored("Bot: I am timeless. I exist only in code!", "yellow"))
        else:
            print(colored("Bot: I'm sorry, I don't understand. Can you please rephrase?", "red"))
