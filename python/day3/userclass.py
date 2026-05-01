class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        

    def greet(self):
        return f"Hi {self.name} thanks for providing the email adress {self.email}"
    

User1=User('manu','abc@gmail.com')

print(User1.greet())

