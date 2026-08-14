def send_messages(messages, sent_messages):
    """Send each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the messages that were sent."""
    print("\nThe following messages have been sent:")
    for completed_message in sent_messages:
        print(completed_message)

messages = [
    "I love Python",
    "Java is fun!",
    "I wish to become a programmer!",
    "I am interested in linear algebra!",
    "Probability and Statistics is my cup of tea",
    "I cannot wait until I can start with NumPy",
]

sent_messages = []

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

show_sent_messages(sent_messages)
