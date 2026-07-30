#This code shows a name and a quote. The name and quote are formatted in a message.
#Notice how the apostrophe's are used for the quote.
first_name = "richard"
last_name = "feynman"
full_name = f"{first_name.title()} {last_name.title()}"
famous_person = full_name 
famous_quote = "You can always recognize truth by its beauty and simplicity."
message = f"{famous_person} once said, \"{famous_quote}\""
print(message)
