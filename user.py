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


    def __str__(self):
        """The screen name and full name for the user"""
        return '{} - {}'.format(self.screen_name, self.full_name)


    def __repr__(self):
        """The id, screen name, and full name for the user"""
        return '{}. {} - {}'.format(self.id, self.screen_name, self.full_name)
