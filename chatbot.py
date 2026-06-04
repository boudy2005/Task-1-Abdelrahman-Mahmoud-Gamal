question_answer = {
    "hello":"Hi there! How can I help you today?",
    "hi":"Hello! Nice to meet you.",
    "how are you":"I'm just a bot, but I'm running perfectly. Thanks for asking!",
    "what is your name":"I'm ChatBot 1.0, your friendly assistant.",
    "who made you":"I was built as a learning project to demonstrate dictionary-based chatbots.",
    "help":"Try: hello, how are you, what is your name, who made you. Type 'exit' to quit.",
}
unfamiliar_response = "Sorry, I don't understand that now. Type 'help' to see what I can help you with."
exit_command ="exit"
def chat_bot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("please tell me how can I help you in text message:")
        processed_input = user_input.lower().strip()
        if processed_input == "":
            print("ChatBot: Please type something.")
            continue
        if processed_input == exit_command:
            print("ChatBot: Goodbye! Thanks for chatting.")
            break
        response = question_answer.get(processed_input, unfamiliar_response)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat_bot()