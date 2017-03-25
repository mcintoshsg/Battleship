

class Player:

    name = 'PLAYER1'
    position = 1

    def get_name(self, position):
        while True:
            try:
                self.name = input("\n Player {} please enter your name : ".format(self.position))
                if self.name == '':
                    input("\nYou must enter a name!!! - press Enter to continue ")
                else:
                    break
            except ValueError:
                print("Bad input - try again")

        return self.name
