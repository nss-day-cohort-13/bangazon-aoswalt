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


    def __str__(self):
        """Show only the id and message of the chirp"""

        return '{}. {}'.format(self.id, self.message)


    def __repr__(self):
        """Show full detail for a chirp"""

        rep = '\nid:      {}\n'.format(self.id)
        rep += 'msg:     {}\n'.format(self.message)
        rep += 'from:    {}\n'.format(self.author)
        rep += 'to:      {}\n'.format(self.to)
        rep += 'parent:  {}\n'.format(self.parent)
        rep += 'child:   {}\n'.format(self.child)
        rep += 'private: {}\n'.format(self.private)
        return rep
