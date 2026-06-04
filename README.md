This repository contains chatbot.py, a lightweight, dictionary-based conversational assistant written in Python.
It was built specifically as a learning project to demonstrate the core mechanics of text-based chatbots without relying on complex machine learning libraries.
Features:
Pre-Programmed Responses: The bot relies on a hardcoded dictionary to map specific user inputs to predefined answers.
Input Processing: It automatically converts user text to lowercase and strips extra whitespace, ensuring that inputs like " HELLO " are successfully recognized as "hello".
Graceful Fallbacks: If a user types an unfamiliar phrase, the bot catches it and prompts the user to type 'help' for a list of valid commands.
Empty Input Handling: If the user presses enter without typing anything, the bot politely asks them to type something rather than crashing.
Continuous Chat Loop: The interaction runs in an infinite while loop, allowing for an ongoing conversation until the user decides to leave.
Getting Started:
To run the chatbot, simply execute the script in your terminal:
python chatbot.py
Once launched, the bot will greet you and wait for your input.
Supported Commands
The bot is programmed to understand and respond to the following exact phrases:
Command                                                      Action
hello or hi                                                  Returns a friendly greeting.
how are you                                                  The bot gives a quick status update.
what is your name                                            The bot introduces itself as ChatBot 1.0.
who made you                                                 Explains the project's educational purpose.
help                                                         Displays the list of recognizable commands.
exit                                                         Breaks the loop and quits the application.
