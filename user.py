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
