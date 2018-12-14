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
        #self.add_to_board(2)
        self.board[0][1] = 2 # temp test
        self.board[0][2] = 2
        self.shift_left()
        print(self.board)

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
        for row_iterator in range(0, len(self.board)):
            # Add values if iterated is same as next value
            for value_iterator in range(0, len(self.board[row_iterator]) - 1):
                # THIS SORTIG WORKS. SOMETHING ELSE IS BROKEN (in theory)
                n = len(self.board[row_iterator])
                self.board[row_iterator][:] = filter(None, self.board[row_iterator])
                self.board[row_iterator].extend([0] * (n - len(self.board[row_iterator])))
                # End of sort
                if self.board[value_iterator] == self.board[value_iterator+1]:
                    # Add equal value adjacent tiles
                    self.board[row_iterator][value_iterator] = self.board[value_iterator] * 2
                    # Zero out added tile
                    self.board[row_iterator][value_iterator+1] = 0
                    # Resort to account for added zero
                    n = len(self.board[row_iterator])
                    self.board[row_iterator][:] = filter(None, self.board[row_iterator])
                    self.board[row_iterator].extend([0] * (n - len(self.board[row_iterator])))
                    # End of sort
