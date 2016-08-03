from user import *
from chirp import *
from quickio import *

class Birdy(object):
    """
    Manage users and chirps for the system

    Static properties:
        users_file      the filename for user data storage
        chirps_file     the filename for chirp data storage

    Properties:
        users           all created users
        chirps          all created chirps
        current_user    the currently active user

    Methods:
        create_user                 create a new user
        select_user                 select a user from a user_id
        create_chirp                create a new chirp
        get_public_chirps           get a list of head chirps of public threads
        get_private_chirps          get a list of head chirps of private threads
        get_chirps_with_replies     get a full thread from any chirp in thread
    """

    users_file = 'users.dat'
    chirps_file = 'chirps.dat'

    def __init__(self):
        """Initialize user and chirp storage"""

        self.users = deserialize(Birdy.users_file, [None])
        self.chirps = deserialize(Birdy.chirps_file, [None])
        User.next_user_id = self.users[-1].id + 1 if self.users[-1] else 1
        Chirp.next_chirp_id = self.chirps[-1].id + 1 if self.chirps[-1] else 1

        self.current_user = None


    def create_user(self, full_name, screen_name):
        """
        Create a new user and set as current user

        Arguments:
            full_name       full name of user
            screen_name     screen name for user

        Returns:
            the newly created user
        """

        user =  User(full_name, screen_name)
        self.users.append(user)
        serialize(Birdy.users_file, self.users)
        self.current_user = user
        return self.current_user


    def select_user(self, user):
        """
        Select a user to be the current user

        Arguments:
            user    the user to be the current user

        Returns:
            the selected user
        """

        self.current_user = user
        return self.current_user


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
        serialize(Birdy.chirps_file, self.chirps)
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


if __name__ == '__main__':
    birdy = Birdy()
