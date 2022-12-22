# from entities import Character
from errors import *


class Menu:
    characters={}

    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a new weapon for a existing character.")
        print("3. Create a new object for a existing character")
        print("4. Show all characters")
        print("5. Delete a character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class, main_weapon=None, add_object=None):
        self.characters[name] = {"sex": sex, "character_class": ch_class, "weapon": {"type": main_weapon, "attack": 0}, "additional object": {"type": add_object}, "durability": 100}

    def command_create_weapon(self, name, attack):
        pass

    def command_create_object(self, name, durability):
        pass

    def command_print_characters(self):
        pass

    def command_delete_characters(self):
        pass

    def run(self):
        # infinite menu loop
        while True:
            # print the menu
            self.print_menu()

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":

                    # ask the user to input the necessary command parameters

                    name = input("Enter the character name (alpha-numeric): ")
                    if choice == "1" and name[0] in self.characters:
                        raise CharacterExists("Name exist")

                    elif name.isalpha():
                        raise InvalidDataFormat("Character's name MUST be alpha-numeric.")

                    elif len(name) < 4:
                        raise InvalidDataFormat("Character's name must be at least 4 symbols long")

                    sex=input("Enter the character sex (letters only, len(4)): ")
                    if not sex.isalpha():
                        raise InvalidDataFormat("Character's sex MUST contain only letters")
                    elif len(sex) < 4:
                        raise InvalidDataFormat("Enter at least 4 symbols.")

                    ch_class=input("Enter the character class (Warrior, Mage, Priest, Rogue): ")
                    if ch_class!='Warrior' and ch_class!='Mage' and ch_class!='Priest' and ch_class!='Rogue':
                        raise InvalidDataFormat('Choose between Warrior, Mage, Priest, and Rogue')


                    # if main_weapon==None:
                    #     print('There are no weapons in your inventory')
                    # if add_object==None:
                    #     print("There are no weapons in your inventory") (представям си го така, но не мога да разбера как да изкарам променливите от функцията)

                    # char = self.command_create_character(....)

                    # ...
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()


    # Мозъкът ми гръмна, имам някаква представа горе долу как да се случат нещата, но много неща са ми неясни и стигам дотук.