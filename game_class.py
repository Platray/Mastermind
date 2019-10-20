from os import name as os_name, system as os_system


class Game:
    def __init__(self):
        self.color_list = ['Yellow', 'Pink', 'Red', 'Aqua', 'White', 'Black', 'Orange', 'Violet']
        self.solution = []
        self.players = []
        self.difficulty_list = {1: "Normal", 2: "Difficult"}
        self.difficulty = 1
        self.mod_list = {1: "Normal", 2: "Debug"}
        self.mod = 1
        self.color_choice_save = []
        self.color_result_save = []
        self.game_turn = 1
        self.game_continue = True
        self.another_game = True

        # Verify OS to clear shell
        if os_name == 'posix':
            self.var_os = 'clear'
        else:
            self.var_os = 'cls'

    def game_title(self):

        os_system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Welcome to Mastermind !"))
        print("║{:51}║".format(""))
        print("║{:51}║".format(" For a better experience, we recommend you"))
        print("║{:51}║".format(" to run this program in a real terminal,"))
        print("║{:51}║".format(" not in a python interpreter."))
        print("╚" + "═" * 51 + "╝")
        input("Press Enter to continue...")

        os_system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Player Name"))
        print("╚" + "═" * 51 + "╝")

    def set_players(self, p1, p2):
        self.players.append(p1)
        self.players.append(p2)

    """
    Set self.difficulty
    Difficult : add two colors into color list
    """

    def game_difficulty(self):
        res = ""

        os_system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")

        for difficulty in self.difficulty_list:
            res = res + "{:^} : {:^}  ".format(difficulty,
                                               self.difficulty_list[difficulty])

        print("║{:^51}║".format(res))
        print("╚" + "═" * 51 + "╝")

        while True:
            difficulty_choice = input(" Choose your difficulty : ")

            if len(difficulty_choice) == 1:
                if int(ord(difficulty_choice)) in (49, 50):
                    break

            print(" Enter the number before difficulty.")

        self.difficulty = int(difficulty_choice)

        if self.difficulty == 2:
            self.color_list.append('Gold')
            self.color_list.append('Silver')

        self.color_list.sort()

        print()

    """
    Set self.mod
    Normal : Solution is hidden
    Debug : Solution is visible 
    """

    def set_mod(self):
        res = ""

        os_system(self.var_os)
        print("")
        print("╔" + "═" * 51 + "╗")

        for mod in self.mod_list:
            res = res + "{:^} : {:^}  ".format(mod,
                                               self.mod_list[mod])

        print("║{:^51}║".format(res))
        print("╚" + "═" * 51 + "╝")

        while True:
            mod_choice = input(" Choose your mod : ")

            if len(mod_choice) > 0:
                if int(ord(mod_choice)) in (49, 50):
                    break

            print(" Enter 1 for Normal or 2 for Debug.")

        self.mod = int(mod_choice)

    """
    Print resume before lunch game
    """

    def game_title_resume(self, p1, p2):
        os_system(self.var_os)

        print("")
        print("╔" + "═" * 51 + "╗")
        print("║{:^51}║".format("Resume Game"))
        print("╠" + "═" * 51 + "╣")
        print("║{0:8}{1:10}{2:>24}{0:8}║".format("",
                                                 "Player 1 : ",
                                                 p1))
        print("║{0:8}{1:10}{2:>24}{0:8}║".format("",
                                                 "Player 2 : ",
                                                 p2))
        print("║{:51}║".format(""))
        print("║{0:8}{1:14}{2:>21}{0:8}║".format("",
                                                 "Difficulty : ",
                                                 self.difficulty_list[self.difficulty]))
        print("║{0:8}{1:14}{2:>21}{0:8}║".format("",
                                                 "Mod : ",
                                                 self.mod_list[self.mod]))
        print("╚" + "═" * 51 + "╝")
        input("Press Enter to continue...")

    def view_color(self):
        x = 0

        os_system(self.var_os)
        print("")
        print("╔" + "═" * 16 + "╗")

        for color in self.color_list:
            print("║ {:2} | {:9} ║".format(x,
                                           color))
            x += 1

        print("╚" + "═" * 16 + "╝")

    def game_board_view(self):
        cpt = 0
        os_system(self.var_os)
        print(" ")

        if self.difficulty == 1:
            head = "╔" + "═" * 39 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = "╠" + "═" * 39 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = "╚" + "═" * 39 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"

            print(head)

            for color_choice in self.color_choice_save:

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = '------'

                print("║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                      "║ {:^3} : {:^3} | {:^3} : {:^3} ║"
                      "║ {:2} | {:9} ║".format(self.color_list[int(color_choice[0])].upper(),
                                               self.color_list[int(color_choice[1])].upper(),
                                               self.color_list[int(color_choice[2])].upper(),
                                               self.color_list[int(color_choice[3])].upper(),
                                               list(self.color_result_save[cpt].keys())[0],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[0]
                                               ],
                                               list(self.color_result_save[cpt].keys())[1],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[1]
                                               ],
                                               cpt,
                                               color.upper()))
                print(middle)
                cpt = cpt + 1

            for i in range(0, 10 - cpt):

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = '------'

                print("║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {0:^3}   {0:^3} | {0:^3}   {0:^3} ║"
                      "║ {1:2} | {2:9} ║".format("",
                                                 cpt,
                                                 color.upper()))
                print(middle)
                cpt = cpt + 1

            if self.mod == 2:
                print(
                    "║ {:^7} | {:^7} | {:^7} | {:^7} ║"
                    "║ {:^9} | {:^9} ║"
                    "║{:^16}║".format(self.color_list[int(self.solution[0])].upper(),
                                      self.color_list[int(self.solution[1])].upper(),
                                      self.color_list[int(self.solution[2])].upper(),
                                      self.color_list[int(self.solution[3])].upper(),
                                      "PLACED",
                                      "COLOR",
                                      "COLORS"))
            else:
                print("║ {0:^7} | {0:^7} | {0:^7} | {0:^7} ║"
                      "║ {1:^9} | {2:^9} ║"
                      "║{3:^16}║".format("X",
                                         "COMPLETED",
                                         "PARTIAL",
                                         "COLORS"))

        else:
            head = "╔" + "═" * 47 + "╦" * 2 + "═" * 23 + "╦" * 2 + "═" * 16 + "╗"
            middle = "╠" + "═" * 47 + "╬" * 2 + "═" * 23 + "╬" * 2 + "═" * 16 + "╣"
            foot = "╚" + "═" * 47 + "╩" * 2 + "═" * 23 + "╩" * 2 + "═" * 16 + "╝"

            print(head)

            for color_choice in self.color_choice_save:
                if len(self.color_list) >= cpt:
                    color = self.color_list[cpt]
                else:
                    color = ' '

                print("║{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}║"
                      "║ {:^3} : {:^3} | {:^3} : {:^3} ║"
                      "║ {:2} | {:9} ║".format(color_choice[0],
                                               color_choice[1],
                                               color_choice[2],
                                               color_choice[3],
                                               color_choice[4],
                                               color_choice[5],
                                               list(self.color_result_save[cpt].keys())[0],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[0]
                                               ],
                                               list(self.color_result_save[cpt].keys())[1],
                                               self.color_result_save[cpt][
                                                   list(self.color_result_save[cpt].keys())[1]
                                               ],
                                               cpt,
                                               color.upper()))
                print(middle)
                cpt = cpt + 1

            for i in range(0, 10 - cpt):

                if len(self.color_list) > cpt:
                    color = self.color_list[cpt]
                else:
                    color = ' '

                print("║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║ {0:^3}   {0:^3} | {0:^3}   {0:^3} ║"
                      "║ {1:2} | {2:9} ║".format("",
                                                 cpt,
                                                 color.upper()))
                print(middle)

                cpt = cpt + 1

            print(middle)

            if self.mod == 2:
                print(
                    "║{:^7}|{:^7}|{:^7}|{:^7}║"
                    "║{:^15}║"
                    "║{:^16}║".format(self.color_list[self.solution[0]].upper(),
                                      self.color_list[self.solution[1]].upper(),
                                      self.color_list[self.solution[2]].upper(),
                                      self.color_list[self.solution[3]].upper(),
                                      self.color_list[self.solution[4]].upper(),
                                      self.color_list[self.solution[5]].upper(),
                                      "SOLUTION",
                                      "COLORS"))
            else:
                print("║{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}|{0:^7}║"
                      "║{1:^23}║"
                      "║{2:^16}║".format("x",
                                         "SOLUTION",
                                         "COLORS"))

        print(foot)

    def verify_choice(self):
        color_choice = self.color_choice_save[-1]
        solution_copy = self.solution[:]
        result_choice = {"X": 0, "O": 0}

        for cpt1 in range(0, len(solution_copy)):
            if solution_copy[cpt1] == int(color_choice[cpt1]):
                result_choice['X'] = result_choice['X'] + 1
                solution_copy[cpt1] = " "

        for cpt1 in range(0, len(solution_copy)):
            for cpt2 in range(0, len(solution_copy)):
                if solution_copy[cpt1] == int(color_choice[cpt2]):
                    result_choice['O'] = result_choice['O'] + 1
                    solution_copy[cpt1] = " "
                    break

        self.color_result_save.append(result_choice)

    def verify_end_game(self):

        if self.game_turn > 10:
            self.game_continue = False
        elif len(self.color_result_save) > 0:
            if self.color_result_save[-1]["X"] == 4:
                self.game_continue = False
        else:
            self.game_turn += 1

    def another_game(self):
        var = ''

        if self.color_result_save[-1]["X"] == 4:
            print("")
            print("╔" + "═" * 51 + "╗")
            print("║{:^51}║".format("Felicitation !"))
            print("║{:51}║".format(""))
            print("║{} {} {}║".format(" You win in ", len(self.color_result_save), " tries "))
            print("╚" + "═" * 51 + "╝")

        if self.color_result_save[-1]["X"] != 4:
            print("")
            print("╔" + "═" * 51 + "╗")
            print("║{:^51}║".format("You loose !"))
            print("║{:51}║".format(""))
            print("║{:51}║".format("You loose the game. Solution was :"))

            if self.difficulty == 1:
                print("║{:^7}|{:^7}|{:^7}|{:^7}║".format(self.color_list[self.solution[0]].upper(),
                                                         self.color_list[self.solution[1]].upper(),
                                                         self.color_list[self.solution[2]].upper(),
                                                         self.color_list[self.solution[3]].upper(),
                                                         ))

            print("╚" + "═" * 51 + "╝")

        while True:

            if var == 'y':
                self.solution = []
                self.color_choice_save = []
                self.color_result_save = []
                self.game_turn = 1
                return True

            elif var == 'n':
                return False

            else:
                var = str(input(" Another game ? y / n \n")).lower().strip()
