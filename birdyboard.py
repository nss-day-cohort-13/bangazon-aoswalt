class Birdy(object):

    def __init__(self):
        self.users = [None]
        self.chirps = [None]
        User.next_user_id = 1
        Chirp.next_chirp_id = 1


    def create_user(self, full_name, screen_name):
        user =  User(full_name, screen_name)
        self.users.append(user)
        return user


    def create_chirp(self, author, message, parent=0, to=0, private=False):
        if parent > 0:
            # set to to parent's author
            to = self.chirps[parent].id
        chirp = Chirp(author, message, parent, to, private)
        self.chirps.append(chirp)
        return chirp


    def get_public_chirps(self):
        return [c for c in self.chirps if c and
            c.parent == 0 and
            c.private == False]


    def get_private_chirps(self, user_id):
        return [c for c in self.chirps if c and
            c.parent == 0 and
            (c.to == user_id or c.author == user_id) and
            c.private == True]


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
