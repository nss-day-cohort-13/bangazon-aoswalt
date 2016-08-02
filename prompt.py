def show_menu(heading, menu):     # pragama: no cover
    """
    Show a menu and prompt for valid response

    Arguments:
        heading     the heading for the menu
        menu        the list of menu options

    Returns:
        the chosen option
    """

    # string representations of the options
    opt_strings = [str(opt) for opt in menu]

    # prompt until only 1 match
    matches = []
    while len(matches) != 1:
        print('\n' + heading)
        [print(opt) for opt in opt_strings]
        choice = input('\n> ')

        # get all matches where input is in the option
        matches = [opt for opt in opt_strings if choice.lower() in opt.lower()]

        if len(matches) == 0: print('No matches found.\n')
        if len(matches) > 1: print('Multiple matches found.\n')

    # use the index of the matched choice to get the actual value from the menu
    return menu[opt_strings.index(matches[0])]


def prompt(prompt_msg):     # pragma: no cover
    """
    Prompt the user for input

    Arguments:
        prompt_msg      the prompt for the input

    Returns:
        the user's input
    """

    print('\n' + prompt_msg)
    return input('> ')


if __name__ == '__main__':
    print(do_menu('title', [['a', 'b'], 1, 'c', 'a']))
