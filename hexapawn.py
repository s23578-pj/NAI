"""
The link to Hexapawn rules:
https://en.wikipedia.org/wiki/Hexapawn#External_links

Authors:
Alicja Szczypior
Krzysztof Szczypior

Instruction to prepare environment:
to install easyAI for python3:
  pip3 install easyAI==2.0.12
"""
from easyAI import TwoPlayerGame, AI_Player, Human_Player, Negamax


def convert_to_move(move):
    """
        Converts a move in the format (row, column) to the standard format with a row letter and column number.

        Parameters:
            move (list of tuples): List of moves in the format (row, column).

        Returns:
            str: A string representing the converted move.

        Example:
            move = [(0, 1), (1, 2)]
            converted_move = convert_to_move(move)
            # Result: "A2 B3"
        """
    row_labels = "ABCD"
    col_offset = 1

    converted_moves = []

    for m in move:
        row_index, col_index = m
        row_label = row_labels[row_index]
        col_number = col_index + col_offset
        converted_move = f"{row_label}{col_number}"
        converted_moves.append(converted_move)

    return " ".join(converted_moves)


# Convert (0, 3) to A4
def convert_to_tuple(move):
    """
        Converts a move in the standard format with a row letter and column number to the format (row, column).

        Parameters:
            move (str): A string representing a move in the format "A1", "B2".

        Returns:
            tuple: A tuple representing the converted move in the format (row, column).

        Example:
            move = "A2"
            converted_move = convert_to_tuple(move)
            # Result: (0, 1)
        """
    index = "ABCD".index(move[0])
    number = int(move[1]) - 1
    return index, number


def create_initial_matrix(row, col, matrix):
    """
        Creates an initial matrix with specified dimensions (rows and columns) filled with coordinate tuples.
        The initial matrix is considering only opponents pawns.

        Parameters:
            row (int): The number of rows in the matrix.
            col (int): The number of columns in the matrix.
            matrix (list): The matrix to be populated with coordinate tuples.

        Returns:
            list of lists: The populated matrix with coordinate tuples.

        Example:
            row = 4
            col = 4
            matrix = []
            created_matrix = create_initial_matrix(row, col, matrix)
            # Result: created_matrix is a 4x4 matrix filled with coordinate tuples.
        """
    for i in [0, row - 1]:
        row_table = []
        for j in range(col):
            row_table.append((i, j))
        matrix.append(row_table)
    return matrix


def get_field(tuple, players):
    """
       Returns the field value at a specified coordinate tuple on the game board.

       Parameters:
           tuple (tuple): A coordinate tuple (row, column).
           players (list): A list of player objects, each with a list of their pawns.

       Returns:
           str: The field value at the specified coordinate - "1" for player 1, "2" for player 2, or "." for field
           without player's pawns.

       Example:
           tuple = (1, 2)
           players = [Player(pawns=[(0, 1), (1, 2)]), Player(pawns=[(2, 3), (3, 4)])]
           field_value = get_field(tuple, players)
           # Result: field_value is "1" as (1, 2) is a pawn of player 1.
       """
    if tuple in players[0].pawns:
        return "1"
    elif tuple in players[1].pawns:
        return "2"
    else:
        return "."


def scoring(game):
    """
        Assigns a score to a game state.

        Parameters:
            game: The game state to be scored.

        Returns:
            int: A score for the game state. Returns 0 if the game is lost; otherwise, returns 100,
            so the AI bot knows which moves should he play to win.

        Example:
            game = game()
            score = scoring(game_state)
            # Result: score is 100 if the game is won, when is lost score equals 0.
        """
    if game.lose():
        return -1
    else:
        return 0


def choose_player():
    """
    The function allows the player to choose the board side - with a player 1 or 2.

     Returns:
         list: A list containing player objects (AI_Player as Player 2 and Human_Player 1) or
         (AI_Player as Player 1 and Human_Player as Player 2).
    """
    isValid = False
    players_list = []
    while not isValid:
        player_choice = input()
        if player_choice == '1':
            players_list = [Human_Player(), AI_Player(ai)]
            isValid = True
        elif player_choice == '2':
            isValid = True
            players_list = [AI_Player(ai), Human_Player()]
        else:
            print("Wrong answer.\nInsert correct number 1 or 2.")

    return players_list


class Hexapawn(TwoPlayerGame):
    """
    Hexapawn game class.

      Attributes:
          size (tuple): The size of the game board (number of rows, number of columns).
          players (list): List of players.
          current_player (int): Current play number (0 or 1).
    """

    def __init__(self, players):
        """
        Initializes a Hexapawn game instance.

        This method initializes a new Hexapawn game with the provided players. It sets the size of the game board,
        creates an initial board matrix, and configures the player objects with their respective attributes,
        including direction, goal line, and pawns. It also initializes the current player to Player 1.

        Parameters:
            players (list): A list containing player objects for the game.

        Returns:
            None.
        """
        self.size = R, C = (3, 3)
        matrix = []
        create_initial_matrix(R, C, matrix)

        for player, direct, goal, pawns in [(0, 1, R - 1, matrix[0]), (1, -1, 0, matrix[1])]:
            players[player].direction = direct
            players[player].goal_line = goal
            players[player].pawns = pawns

        self.players = players
        self.current_player = 1

    def possible_moves(self):
        """
         Returns a list of possible moves for the current player.

         Returns:
             list: List of possible moves.
         """
        moves = []
        opponent_pawns = self.opponent.pawns
        direct = self.player.direction
        for row, col in self.player.pawns:
            if (row + direct, col) not in opponent_pawns:
                moves.append(((row, col), (row + direct, col)))
            if (row + direct, col + 1) in opponent_pawns:
                moves.append(((row, col), (row + direct, col + 1)))
            if (row + direct, col - 1) in opponent_pawns:
                moves.append(((row, col), (row + direct, col - 1)))
        return [convert_to_move((i, j)) for i, j in moves]

    def make_move(self, move):
        """
         Makes a move on the board.
         It transfers the string to a tuple,
         finds which index on the pawn list is the pawn used by user to play,
         replaces tuple with found index with new tuple,
         checks if in new coordinates exist opponent's pawn and remove opponent's pawn

         Parameters:
             move (str): Move as a string.

         Returns:
             None
         """
        moves = move.split(" ")
        converted_moves = [convert_to_tuple(moves[0]), convert_to_tuple(moves[1])]

        pawn_index = self.player.pawns.index(converted_moves[0])
        self.player.pawns[pawn_index] = converted_moves[1]

        if converted_moves[1] in self.opponent.pawns:
            self.opponent.pawns.remove(converted_moves[1])

    def lose(self):
        """
        This method checks whether the current player has lost the game. It examines if any of the opponent's pawns have
        reached their goal line.
        Additionally, it checks if the current player has no possible moves left, which also results in a loss.

        Returns:
            bool: True if the current player has lost, False otherwise.
        """
        for i, j in self.opponent.pawns:
            if i == self.opponent.goal_line:
                return True
        if not self.possible_moves():
            return True
        return False

    def is_over(self):
        """
        Checks if the Hexapawn game is over.

        This method checks if the game has reached a conclusion by calling the 'lose' method.
        If the 'lose' method returns True, the game is considered over; otherwise, it continues.

        Parameters:
            None.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.lose()

    def show(self):
        """
        Displays the current state of the Hexapawn board.

        The method is printing the board with rows separated by newlines.

        Parameters:
            None.

        Returns:
            None.
        """
        size_R = self.size[0]
        size_C = self.size[1]

        board = []
        for i in range(size_R):
            row = []
            for j in range(size_C):
                field = get_field((i, j), self.players)
                row.append(field)
            row_to_print = " ".join(row)
            board.append(row_to_print)

        print("\n".join(board))


if __name__ == "__main__":
    """
    Main part of the Hexapawn program.

    1. Initializes the AI player using the Negamax algorithm.
    2. Displays a welcome message and prompts the user to choose player 1 or 2.
    3. Depending on the player's choice, initializes the respective players and the Hexapawn game.
    4. Starts the gameplay.
    5. After the game ends, displays the result, indicating which player won and how many rounds the game lasted.

    Parameters:
        None.

    Returns:
        None
    """
    ai = Negamax(10, scoring)
    while True:
        print("Welcome to Hexapawn! You are going to lose with AI :)\n\nChoose player 1 or 2: ")
        players = choose_player()
        game = Hexapawn(players)
        game.play()

        print("\nGreat! Player %d has won this battle in %d rounds :]!" % (game.opponent_index, game.nmove))

        continue_playing = input("Do you want to play another game? (insert yes or any character to end): ")
        if continue_playing.lower() != "yes":
            break


