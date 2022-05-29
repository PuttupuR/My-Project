import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_pass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
 
# Define a function for
# for validating an Email
 
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("valid mail")
        f=open("rajeev.txt","a+")
        f.write(email)
        f.close
    else:
        print("enter valid email")

def validate(password):
    if(re.fullmatch(regex_pass, password)):
        print("valid password")
        f=open("rajeev.txt","a+")
        f.write(" "+password + "\n")
        f.close
    else:
        print("not valid")

def login():
    email=input()
    password=input()
    for line in open("rajeev.txt","r").readlines():
        logindetails= line.split()
        if(email== logindetails[0] and password== logindetails[1]):
           print("login succesful")
           break
        else:
            print("User name or password are incorrect Please chosse option for Register or Forget Password")
                
def Retrive():
    email=input("enter email:")
    for line in open("rajeev.txt","r").readlines():
        logindetails= line.split()
        if(email== logindetails[0]):
            return logindetails[1]
    
    
    
while(True):
    print("enter your choice")
    print("1 for registration")
    print("2 for Login")
    print("3 for Forget password")
    n=int(input())
    if(n==1):
#Registration
        email=input("enter email:")
        password=input("enter password:")
        check(email)
        validate(password)

#login
    elif(n==2):
        login()
        
#ForgetPassword
    elif(n==3):
        print("Your Password is:",Retrive())

    
