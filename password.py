import random

print(" ____    ____  ____       ____   ____  _____ _____")
print("|    \  /    ||    \     |    \ /    |/ ___// ___/")
print("|  D  )|  o  ||  _  |    |  o  )  o  (   \(   \ ")
print("|    / |     ||  |  |    |   /|     |\_  |\__  |")
print("|    \ |  _  ||  |  |    |  |  |  _  |/  \ |/  \ |")
print("|  .  \|  |  ||  |  |    |  |  |  |  |\    |\    |")
print("||\|||||||    ||  ||| \| \_|")
print("--------------------------------------------------")
print("Hello! Let's generate a password")

### Define a list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

### Prompt the user
passwordLength = int(input("password length="))

### Generate a random password
newPassword = []
for x in range(passwordLength):
    ### Append a random character to the password string
    newPassword.append(random.choice(characters))

### Join the whole list back into a string
finalPassword = ''.join(map(str, newPassword))

### Let the user know their new password
print("\n This is your new password: ", finalPassword)