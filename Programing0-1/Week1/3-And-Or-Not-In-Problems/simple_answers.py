text = input("Enter text: ")

if "hello" in text.lower():
    print("Hello there, good stranger!")
elif "how are you?" in text.lower():
    print("I am fine, thanks. How are you?")
elif "feelings" in text.lower():
    print("I am a machine. I have no feelings")
elif "age" in text.lower():
    print("I have no age. Only current timestamp")
