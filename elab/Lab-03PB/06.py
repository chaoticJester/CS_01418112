ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

User_input = str(input("Username: "))
Pass_input = str(input("Password: "))

if User_input == ADMIN_USERNAME and  Pass_input == ADMIN_PASSWORD:
    print("Welcome, admin.")
else : 
    print("You are not admin.")