userInput = input("Enter a file name: ")

if userInput.endswith(".gif"):
    print("image/gif")
elif userInput.endswith(".jpg"):
    print("image/jpg")
elif userInput.endswith(".png"):
    print("image/png")
elif userInput.endswith(".pdf"):
    print("application.pdf")
elif userInput.endswith(".txt"):
    print("text/plain")
elif userInput.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
