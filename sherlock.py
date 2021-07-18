passs = ['kartik', 'kartik11', 'kartik@11', 'kartik@#11', 'Kartik@#11', 'Kartik@11']
password = "kartik@#11"
guess = ""
for char in passs:
    if char == password:
        guess = char
        print("password cracked", guess)

