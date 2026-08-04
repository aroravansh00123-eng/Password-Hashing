import hashlib
import random

print("ENTER THE CHOICE 1 OR 2")
print("""1. For hash your own password
         2. To generate new password
""")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    password=input("ENTER YOUR PASSWORD FOR HASHING:")
    hashed_pass=hashlib.sha256(password.encode()).hexdigest()
    print("PASSWORD HAHSED SUCCESSFULLY!!")
    print("Your Hashed Password is: ",hashed_pass)
    print("\n")
    print("**"*62)
    print("DO YOU WANT TO VERIFY YOUR HASHED PASSWORD enter y for yes and n for no")
    choice_check=input("y/n:")
    if choice_check=="y":
        print("WE ARE VERIFIYING YOUR PASSWORD!!")
        hash_pass=input("ENTER YOUR PASSWORD FOR VERITIFICATION:")
        hashed_pass=hashlib.sha256(check_pass.encode()).hexdigest()
        if check_pass==hashed_pass:
            print("PASSWORD VERIFIED SUCCESSFULLY")
        else:
            print("WRONG PASSWORD")
    elif choice_check=="n":
        print("YOU DO NOT WANT TO VERIFY YOUR PASSWORD!!")
        print("exiting....")
