import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(4):
            row = []
            for j in range(4):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    def check_columns(self,player):
        for col in range(4):
            win = True
            for row in range(4):
                if self.board[row][col] != player:
                    win = False
                    break
            if win:
                return True
        return False
        
    def check_rows(self,player):
        for row in self.board:
            #all() method checks if all items in the list meets the condition
            if all([item == player for item in row]):
                return True
        return False
    
    
    def check_diagnonal(self,player):
        if all([self.board[i][i] == player for i in range(4)]):
            return True
            
        if all([self.board[i][3-i] == player for i in range(4)]):
            return True
        return False
    
    def check_corners(self,player):
        if self.board[0][0] == self.board[3][0] == self.board[0][3] == self.board[3][3] == player:
            return True
        return False
    
    def check_2_x_2_square(self,player):
        for row in range(3):
            for col in range(3):
                if (self.board[row][col] == self.board[row][col+1] == self.board[row+1][col] == self.board[row+1][col+1] == player):
                    return True
        return False
    

    def check_winner(self, player):
        if self.check_columns(player) or self.check_rows(player) or self.check_diagnonal(player) or self.check_2_x_2_square(player) or self.check_corners(player):
            return True
        return False
        

    def any_moves_left(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'x' if player == 'o' else 'o'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_game_over(self,player):
        # checking whether current player has won
        if self.check_winner(player):
            print(f"Player {player} wins the game!")
            return True

        # checking whether the game is tied or not
        if self.any_moves_left():
            print("Game has been tied!")
            return True
        
        return False
            

    def play_game(self):

        self.create_board()
        player = 'x' if self.get_random_first_player() == 1 else 'o'

        while True:
            print()
            print(f"Player {player} turn")
            self.show_board()

            # user input validation
            while True:
                try:
                    row = int(input(f"Player {player}! Choose a row position from 1-4: "))
                    col = int(input(f"Player {player}! Choose a column position from 1-4: "))
                    if row not in range(1,5) or col not in range(1,5) or self.board[row-1][col-1] != '-':
                        raise ValueError
                    break
                except ValueError:
                    print("**Row and col number must be between 1-4 and the position must be empty. Please try again.**")
                    print()

            # mark the spot
            self.mark_spot(row - 1, col - 1, player)

            # checking whether game has ended
            if self.is_game_over(player):
                print("The game is over now.")
                break

            # swap to next player
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()

# starting the game
game = TicTacToe()
game.play_game()