class User:
    def __init__(self, userId, userName):
        self.id = userId
        self.name = userName


user_1 = User('s45561076', 'Tobi Salawu')
print(user_1.id, user_1.name)