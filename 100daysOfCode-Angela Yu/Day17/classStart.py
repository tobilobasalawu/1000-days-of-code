class User:
    def __init__(self, userId, name):
        self.id = userId



user_1 = User()
user_1.id = '001'
user_1.name = 'Tobi'

print(user_1.name)