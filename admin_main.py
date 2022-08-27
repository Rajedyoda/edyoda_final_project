from admin_function import AdminFunction

class AdminMain:

    def __init__(self,adminfunction_obj):
        self.adminfunction_obj = adminfunction_obj

    def execute(self,choice):


        if choice == 1:
            print("***********Add New Food Items***********")
            self.adminfunction_obj.add_fooditems()

        elif choice == 2:
            print("***********Edit Food Items**********")
            self.adminfunction_obj.edit_fooditemlist()
        
        elif choice == 3:
            print("***********View Food Items**********")
            self.adminfunction_obj.view_fooditemlist()

        elif choice == 4:
            print("***********Remove Food Items**********")
            self.adminfunction_obj.delete_fooditems()

        elif choice == 5:
            print("***********Your are Exit from the admin Login**********")
            print("*" * 40 + "Thank You" + "*" * 40 + "\n")               
        else:
            print("Invalid Choice, Please Enter Choice from 1 to 4")



if __name__ == "__main__":
    print("***********Enter the Admin Login Details***********")
    adminfunction_obj = AdminFunction()
    adminmain = AdminMain(adminfunction_obj)
    
    adminfunction_obj.add_admin()
    
    while True:
        print(input("Enter \n1.Add New Food Items \n2.Edit Food Items \n3.View Food Items \n4.Remove Food Items \n5.Exit \n"))
        choice = int(input("Enter Your Choice : "))
        adminmain.execute(choice)