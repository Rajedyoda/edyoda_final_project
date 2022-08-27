from admin import Admin_Login

from food_items import Food_Items
import getpass
import re

class AdminFunction:
    adminlist = []
    fooditemlist = []
    def add_admin(self):
        admin_username = input("Enter Admin User Name : ")

        admin_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")
        res2 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$",admin_password)

        if res2:
            pass
        else:
            print("Password is incorrect!!! Kindly enter Minimum 8 & Max 15 AlphaNumeric with Special Character")
            admin_password = getpass.getpass(prompt = "Enter User Password minmun 8 characters and digits with special character : ")

        
        admin_first_name = input("Enter Admin First Name in Capital Letter min 3 and max 16  : ")
        res4 = re.findall(r"^(?=.*[A-Z])[A-Z]{3,16}$",admin_first_name)
        if res4:
           pass
        else:
            print("Format is incorrect!!! minimum 3 char to max 15 char for first name")
            admin_first_name = input("Enter Admin First Name in Capital Letter min 3 and max 16  : ")

        admin_last_name = input("Enter Admin Last Name in Capital Letter min 3 and max 16  : ")
        res5 = re.findall(r"^(?=.*[A-Z])[A-Z]{3,16}$",admin_last_name)
        if res5:
           pass
        else:
            print("Format is incorrect!!! minimum 3 char to max 15 char for last Name")
            admin_last_name = input("Enter Admin Last Name in Capital Letter min 3 and max 16  : ")


        admin_email = input("Enter User Email Id: ")
        result3 = re.findall(r"^[a-zA-Z0-9._]+[@][a-z+]+[.]{1}[a-z]+$",admin_email)
        if result3:
            pass
        else:
            print("Format is incorrect!!!")
            admin_email = input("Enter User Email Id coorectly with name@mail.com: ")

        admin_mobileno = input("Enter your Mobile Number : ")
        result5 = re.findall("^[1-9]{1}[0-9]{9}$",admin_mobileno)
        if result5:
            pass
        else:
            print("Format is incorrect")
            admin_mobileno = int(input("Enter your 10 digit Mobile Number again : "))

        admin_address = input("Enter Admin Address : ") 

        admin_obj = Admin_Login(admin_username,admin_password,admin_first_name,admin_last_name,admin_email,admin_mobileno,admin_address)
        AdminFunction.adminlist.append(admin_obj)
        print("Admin Login Details Successfully Added!")

        dic = dict()
        for i in range (len(self.adminlist)):
            dic[i] = self.adminlist[i]
        print(dic)

        for k,v in dic.items():
            print(v.admin_username)

    def add_fooditems(self):
        food_id = input("Enter Food Item ID : ")
        food_name = input("Enter Food Item Name : ")
        food_quantity = input("Enter Food Item Quantity For eg, 100ml, 250gm, 4pieces etc : ")
        food_price = float(input("Enter Food Item Price : "))
        food_discount = input("Enter Food Item Discount : ")
        food_stock = input("Enter Amount left in stock in the restaurant : ")

        fooditems_obj = Food_Items(food_id,food_name,food_quantity,food_price,food_discount,food_stock)
        AdminFunction.fooditemlist.append(fooditems_obj)
        print("Food Items Successfully Added!")

        dic1 = dict()
        for i in range (len(self.fooditemlist)):
            dic1[i] = self.fooditemlist[i]
        print(dic1)

        for k,v in dic1.items():
            print(v.food_id)

    def edit_fooditemlist(self):
        food_id = input("Enter Food Id of the Food Items List you want to Edit : ")
        for fooditems in self.fooditemlist:
            if fooditems.food_id == food_id:
                food_name = input("Enter Food Item Name : ")
                food_quantity = input("Enter Food Item Quantity For eg, 100ml, 250gm, 4pieces etc : ")
                food_price = float(input("Enter Food Item Price : "))
                food_discount = input("Enter Food Item Discount : ")
                food_stock = input("Enter Amount left in stock in the restaurant : ")
                
                fooditems.set_food_name(food_name)
                fooditems.set_food_quantity(food_quantity)
                fooditems.set_food_price(food_price)
                fooditems.set_food_discount(food_discount)
                fooditems.set_food_stock(food_stock)             
                print("Successfully Edited the Food Items List")
                break
        else:
            print("No Food Item List Found!")

    def view_fooditemlist(self):
        for i in self.fooditemlist:
            print()
            print(i)

    def delete_fooditems(self):
        food_id = input("Enter Food Id of the Food Item List you want to delete : ")
        for fooditems in self.fooditemlist:
            if fooditems.food_id == food_id:
                self.fooditemlist.remove(fooditems)
                print("Successfully Deleted the Food Item List")
                break
        else:
            print("No Food Item List Found!")