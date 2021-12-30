
class User:
    def __init__(self, name, password, balance, uname):
        self.name = name
        self.password = password
        self.balance = balance
        self.uname = uname


u1 = User("Hridy", "1234", "50000", "hridy")
u2 = User("Samihat", "1235", "50000", "hridy")
u3 = User("Khadem", "1236", "50000", "hridy")
u4 = User("Tanjim", "1237", "50000", "hridy")

allUser = []

allUser.append(u1)
allUser.append(u2)
allUser.append(u3)
allUser.append(u4)
