class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    def enroll(self):
        if self.is_rewards_member==True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member=True
            self.gold_card_points+=200
            return self
    def spend_points(self, amount):
        if self.gold_card_points>amount:
            self.gold_card_points-=amount
            return self
        else:
            print("You do not have enough points!")


user_brittany=User("Brittany", "Francis", "brittanyfrancis200@gmail.com", 29)
user_clinton=User("Clinton", "Butler", "clinton.butler@gmail.com", 30)
user_cobu=User("Cobu", "Francis-Butler", "cobucat@yahoo.com", 5)

user_brittany.enroll().display_info().spend_points(50).display_info()
user_clinton.enroll().display_info().spend_points(80).display_info()

user_cobu.display_info().spend_points(40)