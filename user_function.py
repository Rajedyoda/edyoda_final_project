from user_register import User_Register
from list_food import List_Food
import datetime as dt

import getpass
import re

class UserFunction:
    userlist = []
    foodorderlist = []
    def user_registration(self):
        user_fullname = input("Enter User Full Name : ")
        res = re.findall(r"^[a-zA-Z]{3,15}\s[a-zA-Z]{3,15}$",user_fullname)

        if res:
           pass
        else:
            print("Format is incorrect!!! minimum 3 char to max 15 char for first name and last Name")
            user_fullname = input("Enter User Full Name correctly : ")

        user_phonenumber = input("Enter your Phone Number : ")
        res3 = re.findall("^[1-9]{1}[0-9]{9}$",user_phonenumber)
        if res3:
            pass
        else:
            print("Format is incorrect")
            user_phonenumber = int(input("Enter your 10 digit Phone Number again : "))
            
        user_email = input("Enter User Email Id: ")
        result3 = re.findall(r"^[a-zA-Z0-9._]+[@][a-z+]+[.]{1}[a-z]+$",user_email)
        if result3:
            pass
        else:
            print("Format is incorrect!!!")
            user_email = input("Enter User Email Id coorectly with name@mail.com: ")

        user_address = input("Enter User Address : ")

        user_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")
        res2 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$",user_password)

        if res2:
            print("Password is correct")
        else:
            print("Password is incorrect!!! Kindly enter Minimum 8 & Max 15 AlphaNumeric with Special Character")
            user_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")

        user_obj = User_Register(user_fullname,user_phonenumber,user_email,user_address,user_password)
        UserFunction.userlist.append(user_obj)
        print("User Application Registration Successfully registered!")

        dic2 = dict()
        for i in range (len(self.userlist)):
            dic2[i] = self.userlist[i]
        print(dic2)

        for k,v in dic2.items():
            print(v.user_phonenumber)
 

    def place_new_order(self):

        price1 = 240
        price2 = 320
        price3 = 900
        total_price1 = price1 + price2
        total_price2 = price2 + price3
        total_price3 = price1 + price3  
        while True:                                             
            print("*" * 31 + "Food Item Menu List" + "*" * 31 + "\n" 
              "\t(1) TANDOORI CHICKER (4 pieces) [INR 240]\n"
              "\t(2) Vegan Burger (1 Piece) [INR 320]\n"
              "\t(3) Truffle Cake (500gm) [INR 900]\n"
              "\t(4) EXIT\n" +
              "_" * 72)

            user_order = int(input("Enter how many no of item want to order and Enter 4 for exit order : "))
            print()
            if (user_order == 4):
                print("*" * 40 + "Thank You Order Again" + "*" * 40 + "\n")
                break

            print("*" * 40)
            current_date = dt.datetime.now()
            print("DATE: ",current_date )
            print( "_" * 40 +"\n" )
            for i in range(0, user_order):            
                orderitem1  = int(input("Please Select Your Item: "))
                if (orderitem1 == 1):                    
                    print("TANDOORI CHICKER (4 pieces) INR 240")                    

                if (orderitem1 == 2):
                    print("Vegan Burger (1 Piece) [INR 320]")

                if (orderitem1 == 3):
                    print("Truffle Cake (500gm) [INR 900]")

                UserFunction.foodorderlist.append(orderitem1)     
            print(UserFunction.foodorderlist)
            print("_" * 40 + "\n" )
            for j in range (0,user_order):
                if (j == 1):

                    print(f"TOTAL PRICES : " , total_price2)
            
                if (i == 2):
                    print(f"TOTAL PRICES : " , total_price1)

                if (i == 3):
                    print(f"TOTAL PRICES : " , total_price3)

                print("*" * 40 +"\n" )
            print("Successfully Ordered!")

        dic2 = dict()
        for i in range (len(self.foodorderlist)):
            dic2[i] = self.foodorderlist[i]
        print(dic2)
        dic3 = dict()
        for k,v in dic3.items():
            print(v.user_order)


    def update_profile(self):
        user_phonenumber = input("Enter User Phone Number To Update the User Profile : ")
        for updateprofile in self.userlist:
            if updateprofile.user_phonenumber == user_phonenumber:
                user_fullname = input("Enter User Full Name to update : ")
                res1 = re.findall(r"^[a-zA-Z]{3,15}\s[a-zA-Z]{3,15}$",user_fullname)

                if res1:
                    pass
                else:
                    print("Format is incorrect!!! minimum 3 char to max 15 char for first name and last Name")
                    user_fullname = input("Enter User Full Name correctly : ")
                user_email = input("Enter User Email Id: ")
                result1 = re.findall(r"[a-zA-Z0-9._]+[@][a-z+]+[.]{1}[a-z]+$",user_email)

                user_address = input("Enter User Address to update : ") 
                user_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")
                result = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$",user_password)

                if result:
                    print("Password is correct")
                else:
                    print("Password is incorrect!!! Kindly enter Minimum 8 & Max 16 AlphaNumeric with Special Character")
                    user_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")
                updateprofile.set_user_fullname(user_fullname)
                updateprofile.set_user_email(user_email)
                updateprofile.set_user_address(user_address)
                updateprofile.set_user_password(user_password)
            
                print("Successfully Updated the Profile")
                break
        else:
            print("No User Profile Found!")

    def order_history(self):
        for i in self.foodorderlist:
            print()
            print(i)


