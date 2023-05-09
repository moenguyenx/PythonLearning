class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0


minh = User(1908, "moenguyenx")
print(minh.username)
print(minh.id)