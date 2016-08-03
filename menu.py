from birdyboard import *
from prompt import *

class Menu(object):     # pragma: no cover
    """
    Manage the cli menu

    Properties:
        birdy   an instance of the Birdy program

    Methods:
        main                        show the main menu in a loop
        new_user_prompt             prompt for new user info
        select_user_prompt          prompt for selecting a user
        view_public_chirps_prompt   prompt for viewing public chirps
        view_private_chirps_prompt  prompt for viewing private chirps
        public_chirp_prompt         prompt for creating a public chirp
        private_chirp_prompt        prompt for creating a private chirp
        respond_to_chirp            respond to an individual chirp
    """


    def __init__(self):
        """Initialize an instance of Birdy"""

        self.birdy = Birdy()


    def main(self):
        """Show the main menu in a loop"""

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
        """Prompt for new user information"""

        print('\n<< New User >>')
        full_name = prompt('Enter full name')
        screen_name = prompt('Enter screen name')
        new_user = self.birdy.create_user(full_name, screen_name)
        print('\nLogged in as {}\n'.format(self.birdy.current_user.screen_name))


    def select_user_prompt(self):
        """Prompt to select a user"""

        user = show_menu('\n<< Select User >>', self.birdy.users[1:] + [None])

        if not user: return

        self.birdy.select_user(user)
        print('\nLogged in as {}\n'.format(self.birdy.current_user.screen_name))


    def view_public_chirps_prompt(self):
        """Show public chirps and prompt for response"""

        public_chirps = self.birdy.get_public_chirps()

        # append None to use as a back option
        public_chirps.append(None)

        thread_head = show_menu('<< Public Chirps >>', public_chirps)

        if not thread_head: return

        self.respond_to_chirp(thread_head)


    def view_private_chirps_prompt(self):
        """Show private chirps and prompt for response"""

        if not self.birdy.current_user:
            print('\nPlease select a user first.')
            return

        private_chirps = self.birdy.get_private_chirps(self.birdy.current_user.id)

        # append None to use as a back option
        private_chirps.append(None)

        thread_head = show_menu('<< Private Chirps >>', private_chirps)

        if not thread_head: return

        self.respond_to_chirp(thread_head)


    def public_chirp_prompt(self):
        """Prompt for a new public chirp"""

        if not self.birdy.current_user:
            print('\nPlease select a user first.')
            return

        message = prompt('Enter chirp message')

        if len(message) > 0:
            self.birdy.create_chirp(self.birdy.current_user.id, message)


    def private_chirp_prompt(self):
        """Prompt for a target and new private chirp"""

        if not self.birdy.current_user:
            print('\nPlease select a user first.')
            return

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


    def respond_to_chirp(self, thread_head):
        """
        Show thread and prompt for reply

        Arguments:
            thread_head     the head chirp of a thread
        """

        thread = self.birdy.get_chirps_with_replies(thread_head)
        options_menu = ['1. Reply', None]

        # show thread and prompt for option
        [print(chirp) for chirp in thread]
        option = show_menu('---', options_menu)

        if not option: return

        if not self.birdy.current_user:
            print('\nPlease select a user first.')
            return

        # execute option on last chirp in thread
        parent_chirp = thread[-1]

        reply_message = prompt('Reply')
        if len(reply_message) == 0: return

        # create the reply
        self.birdy.create_chirp(
            self.birdy.current_user.id,
            reply_message,
            parent=parent_chirp.id,
            private=parent_chirp.private)


if __name__ == '__main__':
    Menu().main()
