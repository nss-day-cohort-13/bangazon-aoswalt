class Birdy(object):

    def __init__(self):
        self.users = [None]
        self.chirps = [None]
        User.next_user_id = 1
        Chirp.next_chirp_id = 1


    def create_user(self, full_name, screen_name):
        return User(full_name, screen_name)


    def create_chirp(self, author, message, parent=0, to=0, private=False):
        return Chirp(author, message, parent, to, private)


class User(object):
    next_user_id = 1

    def __init__(self, full_name, screen_name):
        self.id = User.next_user_id
        self.full_name = full_name
        self.screen_name = screen_name
        User.next_user_id += 1


class Chirp(object):
    next_chirp_id = 1

    def __init__(self, author, message, parent=0, to=0, private=False):
        self.id = Chirp.next_chirp_id
        self.author = author
        self.message = message
        self.parent = parent
        self.to = to
        self.private = private
        Chirp.next_chirp_id += 1


if __name__ == '__main__':
    birdy = Birdy()
