def main():
    test_game = Game() # TODO: fix not printing anything
    test_game.print_board()

class Game():
    """Used these rules: https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english"""

    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.board[3][3] = -1
        self.board[4][4] = -1
        self.board[3][4] = 1
        self.board[4][3] = 1

    def play(self, player: int, loc: tuple[int]) -> bool:
        """Makes a play on the board by player"""
        to_change = {}
        if not self.valid_check(player, loc):
            return False
        self.board = self.flip(player, loc, self.board)[1]
        return True

    def valid_check(self, player: int, loc: tuple) -> bool:
        if loc[0] < 0 or loc[0] > 7 or loc[1] < 0 or loc[1] > 7:
            return False
        if self.board[loc] != 0:
            return False
        # determine whether this move would flip any pieces
        test_board: list[list[int]] = self.copy_board()
        if self.flip(player, loc)[0] > 0:
            return True
        return False
    
    def bounds_check(self, loc: tuple) -> bool:
        """Returns true if this location is in bounds"""
        if loc[0] < 0 or loc[0] > 7 or loc[1] < 0 or loc[1] > 7:
            return False
        return True
        
    def copy_board(self) -> list[list[int]]:
        new_board = [[0 for x in range(8)] for y in range(8)]
        for y in range(8):
            for x in range(8):
                new_board[y][x] = self.board[y][x]
        return new_board

    def flip(self, player: int, loc: tuple, board: list[list[int]]) -> tuple[int, list[list[int]]]:
        """Returns the number of flipped spaces and the modified board"""
        # check every neighbor (direction by direction) of loc.
        # If it is an opponent piece, check the next piece in that direction (and save the previous one in a list).
        # Keep checking until the next piece is either 1) out of bounds 2) empty 3) friendly piece
        # Only if it is a friendly piece do we save all tiles in that direction in a to_flip list
        ret_board = self.copy_board(board)
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        num_flipped = 0
        to_flip = []

        for direction in directions:
            next_loc = loc + direction
            flip_candidates = []
            while (self.bounds_check(next_loc)):
                if self.board[next_loc] == player:
                    # save the flip_candidates to to_flip
                    to_flip.append(flip_candidates)
                    break # end the loop
                elif self.board[next_loc] == player * (-1):
                    # keep going in this direction
                    next_loc = next_loc + direction
                elif self.board[next_loc] == 0:
                    # stop
                    break
        # flip all squares in to_flip
        for square in to_flip:
            ret_board[square] = player
            num_flipped += 1
            
        return num_flipped, ret_board
            
                

    def win_check(self) -> int:
        """Checks to see if a player has won. Returns the number of the winning player
        or 0 if neither player has won.
        If no pieces of either player remain, the opposite player wins"""
        # TODO

    def print_board(self) -> None:
        for row in range(8):
            print(self.board[row])

if __name__ == "__main__": main()