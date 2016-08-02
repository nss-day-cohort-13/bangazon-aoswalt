from birdyboard import *
from prompt import *

class Menu(object):     # pragma: no cover


    def __init__(self):
        self.birdy = Birdy()


    def main(self):
        while True:
            heading = '#' * 24
            heading += '\n##' + 'Birdyboard~'.center(20) + '##\n'
            heading += '#' * 24
            main_menu = {
                '1. New User Account': self.new_user_prompt,
                '2. Select User': self.select_user_prompt,
                '3. View Chirps': self.view_chirps_prompt,
                '4. Public Chirp': self.public_chirp_prompt,
                '5. Private Chirp': self.private_chirp_prompt,
                '6. Exit': exit}

            choice = show_menu(heading, sorted(main_menu.keys()))
            main_menu[choice]()


    def new_user_prompt(self):
        print('\n<< New User>>')
        full_name = prompt('Enter full name')
        screen_name = prompt('Enter screen name')
        new_user = self.birdy.create_user(full_name, screen_name)
        print('\nLogged in as {}\n'.format(self.birdy.current_user.screen_name))


    def select_user_prompt(self):
        user = show_menu('\n<< Select User', self.birdy.users[1:])
        self.birdy.select_user(user)
        print('\nLogged in as {}\n'.format(self.birdy.current_user.screen_name))


    def view_chirps_prompt(self):
        print('prompt for view chirps')


    def public_chirp_prompt(self):
        print('prompt for public chirp')


    def private_chirp_prompt(self):
        print('prompt for private chirp')


if __name__ == '__main__':
    Menu().main()
