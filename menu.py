def do_menu(heading, menu):     # pragama: no cover
    """
    Show a menu and prompt for valid response

    Arguments:
        heading     the heading for the menu
        menu        the list of menu options

    Returns:
        the chosen option
    """

    opt_strings = [str(opt) for opt in menu]

    matches = []
    while len(matches) != 1:
        print(heading)
        [print(opt) for opt in opt_strings]
        choice = input('\n> ')
        matches = [opt for opt in opt_strings if choice in opt]

        if len(matches) == 0: print('No matches found.\n')
        if len(matches) > 1: print('Multiple matches found.\n')

    # use the index of the matched choice to get the actual value from the menu
    return menu[opt_strings.index(matches[0])]


if __name__ == '__main__':
    print(do_menu('title', [['a', 'b'], 1, 'c', 'a']))
