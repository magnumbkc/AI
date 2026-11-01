print("Chatbot: Hello!")

while True:
    message = input("You: ").lower()

    if "hello" in message or "hi" in message:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you?" in message:
        print("Chatbot: I am fine. Thank you!")

    elif "name" in message:
        print("Chatbot: I am a simple rule-based chatbot.")

    elif "bye" in message:
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")