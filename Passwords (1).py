users = []
users.append(['user1','password1'])
users.append(['user2','password2'])
users.append(['user3','password3'])
users.append(['user4','password4'])

loginAttempts = 0
login = False
while loginAttempts <3 and login == False:
    userEntry = input("Please enter your user name.")
    userPassword = input("Please enter your password.")
    loginAttempts +=1 #Increment login attempts
    for sub_list in users:
        if sub_list[0] == userEntry:
            if userPassword == sub_list[1]:
                print("Login Successful")
                login = True #while loop terminates
    if login == False:
        print("Unsuccessful login")
        print("You now have "+str(3-loginAttempts)+" attempts remaining")
#End While Loop
if login == True:
    print("You are now logged in")
else:
    print("3 Unsuccessful login attempts. Login over")

new_user = 'user4','password4'
users[4].extend(new_user)

print(users)
