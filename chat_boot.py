
def get_response(user_input):
    # Convert input to lowercase and remove extra spaces
    message = user_input.lower().strip()

    # Check the user's message and return a suitable response
    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message in ["i am fine", "i'm fine", "good"]:
        return "That's great to hear!"

    elif message in ["what is your name", "your name"]:
        return "I'm PyBot, your Python chatbot!"

    elif message in ["what can you do", "help"]:
        return "I can respond to greetings and simple questions."

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Try saying 'hello' or 'help'."


def start_chatbot():
    print("=" * 40)
    print("       Welcome to PyBot!")
    print("   Your Simple Python Chatbot")
    print("=" * 40)
    print("Type 'help' for assistance.")
    print("Type 'bye' to end the conversation.")
    print()

    while True:
        user_input = input("You: ").strip()

        # Handle empty input
        if not user_input:
            print("PyBot: Please enter a message.")
            continue

        response = get_response(user_input)
        print("PyBot:", response)

        # Stop the chatbot when the user exits
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    start_chatbot()
