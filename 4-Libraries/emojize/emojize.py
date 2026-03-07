import emoji

user_input = input("Enter an emoji string:\n")
print("Output: " + emoji.emojize(user_input, language="alias"))
