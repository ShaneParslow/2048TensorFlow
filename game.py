import numpy as np
import pdb

class Twenty48():
    """Simple 2048 game played on a matrix."""

    def __init__(self, dimensions=4):
        """Create game board matrix and create 2 random numbers on the board.

        dimensions -- length and width of game board (4 by default)
        """
        self.size = dimensions

        # Create empty board filled with zeroes of size provided
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.add_to_board(2)
        print(np.matrix(self.board))
        self.shift_left()

    def add_to_board(self, num):
        """Add 2 or 4 to game board. 90% chance of 2, 10% chance of 4.

        num -- number of random numbers to place on board
        """
        for i in range(num):
            # Check if board is full (game over)
            if not any(0 in subl for subl in self.board):
                return False
            value = 4 if np.random.rand() > 0.9 else 2  # Select value of tile
            # Keep repeating until coordinate is selected that is empty
            while True:
                x_coord = np.random.randint(self.size)
                y_coord = np.random.randint(self.size)
                # Add value to board at coordinate if the coordinate is empty
                if self.board[y_coord][x_coord] == 0:
                    self.board[y_coord][x_coord] = value
                    break
        return True

    def shift_up(self):
        pass

    def shift_right(self):
        pass

    def shift_down(self):
        pass

    def shift_left(self):
        row_iterator = 0  # Temp row to test
        for row_iterator in range(0,len(self.board)-1):
            # Sort values to end of list
            self.board[row_iterator] = sorted(self.board[row_iterator], key=lambda x: x == 0)
            for value_iterator in range(0,len(self.board[row_iterator])-1):
                current_value = self.board[row_iterator][value_iterator]
                next_value = self.board[row_iterator][value_iterator+1]
                
                if current_value == next_value:
                    self.board[row_iterator][value_iterator] = current_value*2
                    self.board[row_iterator][value_iterator+1] = 0
                    # Sort again
                    self.board[row_iterator] = sorted(self.board[row_iterator], key=lambda x: x == 0)
