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
                '3. View Public Chirps': self.view_public_chirps_prompt,
                '4. View Private Chirps': self.view_private_chirps_prompt,
                '5. Create Public Chirp': self.public_chirp_prompt,
                '6. Create Private Chirp': self.private_chirp_prompt,
                '7. Exit': exit}

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


    def view_public_chirps_prompt(self):
        public_chirps = self.birdy.get_public_chirps()

        # append None to use as a back option
        public_chirps.append(None)

        thread_head = show_menu('<< Public Chirps >>', public_chirps)
        print(repr(thread_head))


    def view_private_chirps_prompt(self):
        private_chirps = self.birdy.get_private_chirps(self.birdy.current_user.id)

        # append None to use as a back option
        private_chirps.append(None)

        thread_head = show_menu('<< Private Chirps >>', private_chirps)
        print(repr(thread_head))


    def public_chirp_prompt(self):
        message = prompt('Enter chirp message')

        if len(message) > 0:
            self.birdy.create_chirp(self.birdy.current_user.id, message)


    def private_chirp_prompt(self):
        user_list = [usr for usr in self.birdy.users
                        if usr and usr != self.birdy.current_user]

        # append None to use as a back option a
        user_list.append(None)

        target = show_menu('Chirp at', user_list)
        if target == None: return

        message = prompt('Enter chirp message')
        if len(message) > 0:
            self.birdy.create_chirp(
                self.birdy.current_user.id,
                message,
                to=target.id,
                private=True)


if __name__ == '__main__':
    Menu().main()
