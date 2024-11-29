# enter some value for login and password have to Initialize
stored_login = "12345"
stored_password = "67890"
# thi loop works until the function is false
while True:
    # ask user
    user_login = input("Enter login: ")
    user_password = input("Enter password: ")

    # Check if enetered info is true or not
    if user_login == stored_login and user_password == stored_password:
        print("Login successful! Welcome to the website.")
        break
    else:
        print("Incorrect login or password. Please try again.")
