userGreeting = input("Please input your greeting: ").lower()

if userGreeting.startswith("hello"):
    print("$0")
elif userGreeting.startswith("h"):
    print("$20")
else:
    print("$100")
