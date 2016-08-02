from birdyboard import *
from prompt import *

class Menu(object):     # pragma: no cover


    def __init__(self):
        self.birdy = Birdy()


    def main(self):
        while True:
            main_menu = {
                '1. New User Account': self.new_user_prompt,
                '2. Select User': self.select_user_prompt,
                '3. View Chirps': self.view_chirps_prompt,
                '4. Public Chirp': self.public_chirp_prompt,
                '5. Private Chirp': self.private_chirp_prompt,
                '6. Exit': exit}

            main_menu[show_menu('Birdyboard', sorted(main_menu.keys()))]()


    def new_user_prompt(self):
        print('prompt for new user')


    def select_user_prompt(self):
        print('prompt for select user')


    def view_chirps_prompt(self):
        print('prompt for view chirps')


    def public_chirp_prompt(self):
        print('prompt for public chirp')


    def private_chirp_prompt(self):
        print('prompt for private chirp')


if __name__ == '__main__':
    Menu().main()
