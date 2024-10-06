class User:
    def __init__(self, userId, userName):
        self.id = userId
        self.name = userName
        self.followers = 0


user_1 = User('s45561076', 'Tobi Salawu')
print(user_1.id, user_1.name)

user_2 = User('s4610859', 'Biology')
print(user_2.id)