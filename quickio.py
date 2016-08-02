import pickle

def serialize(filename, obj):
    """
    Write an object to a file

    Arguments:
        filename    the filename to write to
        obj         the object to be written
    """

    with open(filename, 'wb+') as write_file:
        pickle.dump(obj, write_file)


def deserialize(filename, fallback=None):
    """
    Load the data from a file

    Arguments:
        filename    the filename to read
        fallback    the object to return if the loading fails

    Returns:
        the data from the file
    """

    try:
        with open(filename, 'rb') as read_file:
            return pickle.load(read_file)
    except (FileNotFoundError, EOFError):
        return fallback
