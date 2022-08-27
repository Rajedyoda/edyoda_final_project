class User_Register:

    def __init__(self,user_fullname,user_phonenumber,user_email,user_address,user_password):
        self.user_fullname = user_fullname
        self.user_phonenumber = user_phonenumber
        self.user_email = user_email
        self.user_address = user_address
        self.user_password = user_password

    def __str__(self):
        return f"User FullName : {self.user_fullname} \nUser Phone Number : {self.user_phonenumber} \nUser Email : {self.user_email} \nUser Address : {self.user_address} \nUser Password : {self.user_password} \n"


    def set_user_fullname(self,user_fullname):
        self.user_fullname = user_fullname

    def get_user_fullname(self):
        return self.user_fullname

    def set_user_phonenumber(self,user_phonenumber):
        self.user_phonenumber = user_phonenumber

    def get_user_phonenumber(self):
        return self.user_phonenumber

    def set_user_email(self,user_email):
        self.user_email = user_email

    def get_user_email(self):
        return self.user_email

    def set_user_address(self,user_address):
        self.user_address = user_address

    def get_user_address(self):
        return self.user_address

    def set_user_password(self,user_password):
        self.user_address = user_password

    def get_user_password(self):
        return self.user_password




