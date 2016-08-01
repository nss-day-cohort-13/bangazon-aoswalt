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


    def select_user(self, user_id):
        return self.users[user_id]


    def create_chirp(self, author, message, parent=0, child=0, to=0, private=False):
        if parent > 0:
            # set to to parent's author
            to = self.chirps[parent].id
        chirp = Chirp(author, message, parent, child, to, private)
        if parent > 0:
            # update parent's child
            self.chirps[parent].child = chirp.id
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


    def get_chirps_with_replies(self, cur_chirp):
        # set current chirp to start of thread
        while cur_chirp.parent != 0:
            cur_chirp = self.chirps[cur_chirp.parent]

        # build thread starting from head
        thread = [cur_chirp]
        while cur_chirp.child != 0:
            cur_chirp = self.chirps[cur_chirp.child]
            thread.append(cur_chirp)

        return thread


class User(object):
    next_user_id = 1

    def __init__(self, full_name, screen_name):
        self.id = User.next_user_id
        self.full_name = full_name
        self.screen_name = screen_name
        User.next_user_id += 1


class Chirp(object):
    next_chirp_id = 1

    def __init__(self, author, message, parent=0, child=0, to=0, private=False):
        self.id = Chirp.next_chirp_id
        self.author = author
        self.message = message
        self.parent = parent
        self.child = child
        self.to = to
        self.private = private
        Chirp.next_chirp_id += 1


if __name__ == '__main__':
    birdy = Birdy()
