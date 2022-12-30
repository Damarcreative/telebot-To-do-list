import telebot
from telebot import types

API_TOKEN = "API_KEY_TOKEN"

bot = telebot.TeleBot(API_TOKEN)

# Create task lists
tasks = []

# Function to add tasks to the list
def add_task(task):
    tasks.append(task)

# Function to display task list
def display_tasks():
    if tasks:
        message = "Task List:\n"
        for i, task in enumerate(tasks):
            message += f"{i+1}. {task}\n"
    else:
        message = "Empty to-do list!"
    return message

# Function to remove a task from the list
def clear_tasks():
    tasks.clear()
    return "Task list deleted successfully!"

# Function to process commands received from the user
def process_command(command):
    if command.lower().startswith("add"):
        task = command[4:]
        add_task(task)
        return "Task successfully added to the list!"
    elif command.lower() == "list":
        return display_tasks()
    elif command.lower() == "/list":
        return display_tasks()
    elif command.lower() == "delete":
        return clear_tasks()
    elif command.lower() == "/delete":
        return clear_tasks()
    elif command.lower() == "/start":
        return "Ok, start adding a new task with the following command: add Task name (add Go to market)"
    else:
        return "Command not recognized. Try again with the command: add, list, or delete."

# Handle messages received from users
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    command = message.text
    response = process_command(command)
    bot.send_message(message.chat.id, response)

bot.polling()
print("Bots are running")
