class Password:
    def __init__(self, cpassword, old_passwords):
        self.cpassword = cpassword
        self.old_passwords = old_passwords

    def getpassword(self):
        return self.cpassword

    def setpassword(self, new_password):
        self.old_passwords.append(self.cpassword)
        self.cpassword = new_password

    def ispassword(self, opassword):
        return self.cpassword == opassword

def main():
   
    cpassword = input("Enter the current password: ")
    
  
    old_passwords = input("Enter the list of old passwords separated by space: ").split()
    
    pwd = Password(cpassword, old_passwords)
    
    for opassword in old_passwords:
        if pwd.ispassword(opassword):
            print(f"Current Password: {cpassword}, Old Password: {opassword}, Match: True")
        else:
            print(f"Current Password: {cpassword}, Old Password: {opassword}, Match: False")
    
    new_password = input("Enter the new password: ")
    pwd.setpassword(new_password)
    print(f"New Password set: {pwd.getpassword()}")
    print(f"Updated list of old passwords: {pwd.old_passwords}")

main()