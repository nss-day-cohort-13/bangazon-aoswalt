class Birdy(object):
    """
    Manage users and chirps for the system

    Methods:
        create_user                 create a new user
        select_user                 select a user from a user_id
        create_chirp                create a new chirp
        get_public_chirps           get a list of head chirps of public threads
        get_private_chirps          get a list of head chirps of private threads
        get_chirps_with_replies     get a full thread from any chirp in thread
    """

    def __init__(self):
        """Initialize user and chirp storage"""

        self.users = [None]
        self.chirps = [None]
        User.next_user_id = 1
        Chirp.next_chirp_id = 1


    def create_user(self, full_name, screen_name):
        """
        Create a new user

        Arguments:
            full_name       full name of user
            screen_name     screen name for user

        Returns:
            the newly created user
        """

        user =  User(full_name, screen_name)
        self.users.append(user)
        return user


    def select_user(self, user_id):
        """
        Select a user

        Arguments:
            user_id     the requested user's id

        Returns:
            the selected user
        """

        return self.users[user_id]


    def create_chirp(self, author, message, parent=0, child=0, to=0, private=False):
        """
        Create a new chirp

        Arguments:
            author      the user_id of the author
            message     the content of the chirp
            parent      the chirp_id of the parent chirp
            child       the chirp_id of a child chirp
            to          the user_id of the chirp's recipient
            private     a boolean for the message to be private

        Returns:
            the newly created chirp
        """

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
        """
        Get a list of the head chirps for public threads

        Returns:
            the list of head chirps for public threads
        """

        return [c for c in self.chirps if c and
            c.parent == 0 and
            c.private == False]


    def get_private_chirps(self, user_id):
        """
        Get a list of the head chirps for private threads involving the user

        Arguments:
            user_id     the user involved in the private threads

        Returns:
            the list of head chirps for private threads
        """

        return [c for c in self.chirps if c and
            c.parent == 0 and
            (c.to == user_id or c.author == user_id) and
            c.private == True]


    def get_chirps_with_replies(self, cur_chirp):
        """
        Get a list of all chirps in a thread

        Arguments:
            cur_chirp   one of the chiprs in the thread

        Returns:
            a list of chirps in the full thread
        """

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
    """
    Contains the data for an individual user

    Static attributes:
        next_user_id    the id for the next created user
    """

    next_user_id = 1

    def __init__(self, full_name, screen_name):
        """
        Initialize a user and increment User.next_user_id

        Arguments:
            full_name       full name of user
            screen_name     screen name for user

        """

        self.id = User.next_user_id
        self.full_name = full_name
        self.screen_name = screen_name
        User.next_user_id += 1


class Chirp(object):
    """
    Contains the data for an individual chirp

    Static attributes:
        next_chirp_id    the id for the next created chirp
    """

    next_chirp_id = 1

    def __init__(self, author, message, parent=0, child=0, to=0, private=False):
        """
        Initialize a chirp and increment Chirp.next_chirp_id

        Arguments:
            author      the user_id of the author
            message     the content of the chirp
            parent      the chirp_id of the parent chirp
            child       the chirp_id of a child chirp
            to          the user_id of the chirp's recipient
            private     a boolean for the message to be private
        """
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
