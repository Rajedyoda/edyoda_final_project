from user_function import UserFunction


class UserMain:

    def __init__(self,userfunction_obj):
        self.userfunction_obj = userfunction_obj

    def user_execute(self,choice):


        if choice == 1:
            print("*********** Place New Order***********")
            self.userfunction_obj.place_new_order()


        elif choice == 2:
            print("***********Order History**********")
            self.userfunction_obj.order_history()
      
        elif choice == 3:
            print("***********Update Profile**********")
            self.userfunction_obj.update_profile()

        elif choice == 4:
            print("***********Your are Exit from the order**********")
            print("*" * 40 + "Thank You Order Again" + "*" * 40 + "\n")           
             
        else:
            print("\n" * 3 + "ERROR: Invalid Input (" + str(choice) + "). Try again!")
    


if __name__ == "__main__":
    print("***********Register on the Appliction***********")
    userfunction_obj = UserFunction()
    usermain = UserMain(userfunction_obj)
    
    userfunction_obj.user_registration()
    print("Log in to the application!")
    while True:     
        
        print(input("Enter \n1. Place New Order \n2. Order History \n3. Update Profile \n4. Exit order \n"))
        choice = int(input("Enter Your Option: "))
        usermain.user_execute(choice)

    