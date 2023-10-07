#EMAIL SLICER

email = input("Enter your mail: ")

index = email.index("@")

username = email[:index]
dormain = email[index+1:]

print(f"Your username is {username} and your dormain in {dormain}")











