from display import DisplayBoard


class Interact:
    playing = True
    players = ""  # input stored as string, source of many issues!
    player_1_choice = ""
    player_2_choice = ""
    current_player = 1
    winning_player = 0
    cpu_position = ''

    def __init__(self):
        self.playing = Interact.playing
        self.players = Interact.players
        self.player_1_choice = Interact.player_1_choice
        self.player_2_choice = Interact.player_2_choice
        self.current_player = Interact.current_player
        self.winning_player = Interact.winning_player
        self.cpu_position = Interact.cpu_position

    def get_input(self):
        positions = DisplayBoard.positions
        player = self.current_player
        if player == 1:
            choice = self.player_1_choice
        elif player == 2:
            choice = self.player_2_choice

        # print(choice)
        if self.players == "2" or self.players == "1" and player == 1:
            print(f"Player {player} [{choice.upper()}], please enter a number corresponding to the square:")
            if len(positions) > 0:
                options = [n for n in range(1, 10) if positions[n] == '']
                if '' in positions.values():
                    selection = input(f"{options}: ")
                    if selection.isdigit():
                        if not positions[int(selection)]:
                            positions[int(selection)] = choice
                            if player == 1:
                                self.current_player = 2
                            elif player == 2:
                                self.current_player = 1
                        else:
                            print("That position is taken, please choose another.")
                            self.get_input()
                    else:
                        print("That is not a valid choice, please try again.")
                        self.get_input()
                else:
                    self.playing = False
            else:
                print("something has gone wrong!")
        elif self.players == "1" and player == 2:
            if player == 2:
                self.cpu_position = self.cpu_move()
                print(f"CPU, [{self.player_2_choice.upper()}] has moved to: {self.cpu_position}")
                positions[int(self.cpu_position)] = self.player_2_choice
                self.current_player = 1

    def player_count(self):
        number_of_players = input("Please select 1 or 2 players: ")
        if number_of_players == '1' or number_of_players == '2':
            print(f"You have selected {number_of_players} Player{'' if number_of_players != '2' else 's'}")
            self.players = number_of_players
            self.choose_piece(int(number_of_players))
        else:
            print("Sorry that was an incorrect choice.")
            self.player_count()

    def choose_piece(self, player_count: int):
        if player_count == 1:
            choice = input("Please choose X or O: ").upper()
            self.set_choice(choice, player_count)
        elif player_count == 2:
            choice = input("Player 1 please choose X or O: ").upper()
            self.set_choice(choice, player_count)

    def set_choice(self, choice: str, player_count: int):
        if choice == 'X':
            self.player_1_choice = 'x'
            self.player_2_choice = 'o'
            print(f"Player 1 is {self.player_1_choice.upper()}, {'Player 2' if player_count == 2 else 'CPU'}"
                  f" is {self.player_2_choice.upper()}")
        elif choice == 'O':
            self.player_1_choice = 'o'
            self.player_2_choice = 'x'
            print(f"Player 1 is {self.player_1_choice.upper()}, {'Player 2' if player_count == 2 else 'CPU'}"
                  f" is {self.player_2_choice.upper()}")
        else:
            print("Sorry, your selection was not valid.")
            self.choose_piece(player_count)

    def cpu_move(self):
        positions = DisplayBoard.positions
        piece = ''
        play_row = []
        play_empty = []
        player_count = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
        }
        cpu_count = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
        }
        priority = [5, 1, 3, 7, 9, 2, 4, 6, 8]
        winning_patterns = {
            0: {1: piece, 2: piece, 3: piece},
            1: {4: piece, 5: piece, 6: piece},
            2: {7: piece, 8: piece, 9: piece},
            3: {1: piece, 4: piece, 7: piece},
            4: {2: piece, 5: piece, 8: piece},
            5: {3: piece, 6: piece, 9: piece},
            6: {1: piece, 5: piece, 9: piece},
            7: {3: piece, 5: piece, 7: piece},
        }
        mark_position = ''

        for entry in winning_patterns:
            for n in winning_patterns[entry]:
                for m in positions:
                    if positions[m] != '' and n == m:
                        winning_patterns[entry][n] = positions[m]

        for entry in winning_patterns:
            # count = sum(value == self.player_1_choice for value in winning_patterns[entry].values())
            if self.player_1_choice in winning_patterns[entry].values() and '' in winning_patterns[entry].values():
                # print(count)
                # print(winning_patterns[entry])
                play_row.append(winning_patterns[entry])
            if winning_patterns[entry] not in play_row and '' in winning_patterns[entry].values():
                play_empty.append(winning_patterns[entry])

        # print(play_row)
        # print(play_empty)

        #       Find positions where this is true first, iterate over whole dict beforehand
        #
        #       check to see if P2 can win first, then check to see if P1 can win next move (i.e. has 2 in a row)
        #       then place piece accordingly (P2 winning move or P1 blocking move)
        #       otherwise play in the centre, corners or sides if no other useful moves available, in that priority
        #
        for n in play_row:
            for entry in winning_patterns:
                if winning_patterns[entry] == n:
                    player_count[entry] = sum(value == self.player_1_choice for value in n.values())
        for n in play_empty:
            for entry in winning_patterns:
                if winning_patterns[entry] == n:
                    cpu_count[entry] = sum(value == self.player_2_choice for value in n.values())

        # print(player_count)
        # print(cpu_count)

        for entry in player_count:
            if cpu_count[entry] == 2:
                for n in winning_patterns[entry]:
                    if winning_patterns[entry][n] == '':
                        return n
            elif player_count[entry] == 2:
                for n in winning_patterns[entry]:
                    if winning_patterns[entry][n] == '':
                        return n
        else:
            for n in priority:
                if positions[n] == '':
                    return n


class PlayGame:
    def __init__(self, inter):
        self.player_1_choice = inter.player_1_choice
        self.player_2_choice = inter.player_2_choice
        self.players = inter.players
        self.winning_player = inter.winning_player
        self.playing = inter.playing

    def game_over(self, inter):
        winning_piece = self.check_winner()
        if winning_piece == 'x' or winning_piece == 'o':
            inter.playing = False
            print("Game Over!")

        if winning_piece == self.player_1_choice:
            self.winning_player = 1
            self.win_message(winning_piece)
        elif winning_piece == self.player_2_choice:
            if self.players == "2":
                self.winning_player = 2
                self.win_message(winning_piece)
            else:
                self.winning_player = 'CPU'
                self.win_message(winning_piece)
        else:
            if self.check_board_is_full():
                self.winning_player = 'Draw'
                print("Game Over!")
                print("No one wins, it's a Draw!")
                inter.playing = False

    def win_message(self, winning_piece):
        self.playing = False
        print(f"{'Player' if not self.winning_player == 'CPU' else 'CPU'}"
              f"{'' if self.winning_player == 'CPU' else self.winning_player} [{winning_piece.upper()}] wins!")

    def check_board_is_full(self):
        for n in DisplayBoard.positions:
            if DisplayBoard.positions[n] == '':
                return False
        return True

    def check_winner(self):
        pieces = {0: "x", 1: "o"}
        winning_piece = ""
        for n in range(2):
            if self.check_board(pieces[n]):
                winning_piece = pieces[n]
        return winning_piece

    def check_board(self, piece: str) -> bool:
        piece = piece
        winning_patterns = {
            0: {1: piece, 2: piece, 3: piece},
            1: {4: piece, 5: piece, 6: piece},
            2: {7: piece, 8: piece, 9: piece},
            3: {1: piece, 4: piece, 7: piece},
            4: {2: piece, 5: piece, 8: piece},
            5: {3: piece, 6: piece, 9: piece},
            6: {1: piece, 5: piece, 9: piece},
            7: {3: piece, 5: piece, 7: piece},
        }
        for n in range(len(winning_patterns)):
            won = []
            for m in winning_patterns[n]:
                won.append(DisplayBoard.positions[m] == piece)
            if False not in won:
                return True
        return False
