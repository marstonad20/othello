class Game():
    """Used these rules: https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english"""

    def __init__(self):
        self.board = list[list[int]] # -1 is white, 1 is black, 0 is unclaimed
        self.curr_player = "black"
        self.BOARD_SIZE = 8

    def update(self, last_play: tuple) -> None:
        """Checks all possible captures that can be made by last_play"""
        to_change = {}
        play_color = self.board[last_play] # SYNTAX?
        for neighbor in self.get_neighbors(last_play):
            curr = neighbor
            potential_flips = list[tuple]
            if self.board[neighbor] * (-1) == play_color: # if this piece is of the opposite color
                while self.board[curr] == (-1) * play_color:
                    potential_flips.append(curr)
                    curr = self.get_ray_neighbor(curr, self.get_ray(neighbor, curr))
                if self.board[curr] == 0:
                    continue
                if self.oob_test(curr):
                    continue
        pass

    def oob_test(self, square: tuple) -> bool:
        pass

    def get_neighbors(self, square: tuple) -> list[tuple]:
        """Get all neighbors of the given square"""
        pass

    def get_ray(self, square1: tuple, square2: tuple) -> int:
        """gets the direction of the ray intersecting two squares
        up-left is 0, up is 1, up-right is 2, right is 3, down-right is 4, down is 5, down-left is 6, left is 7"""
        pass

    def get_ray_neighbor(self, square: tuple, direction: int):
        """up-left is 0, up is 1, up-right is 2, right is 3, down-right is 4, down is 5, down-left is 6, left is 7"""
        pass

    def make_move(self, move: tuple) -> None:
        """One of the two players has chosen a square, and now """
        pass
    
    def loop(self):
        """First black plays, then white plays, etc. until someone wins"""
        
    def terminal_test(self):
        """If no pieces of either player remain, the opposite player wins"""
        black_seen: bool = False
        white_seen: bool = False
        for i in range(0, self.BOARD_SIZE):
            for j in range(0, self.BOARD_SIZE):
                if self.board[i,j] == -1:
                    white_seen == True
                elif self.board[i,j] == 1: # SYNTAX?
                    black_seen == True
                if white_seen and black_seen:
                    return False
        if (not black_seen) and (not white_seen):
            return False
        return True