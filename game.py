class Game():
    """Used these rules: https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english"""

    def __init__(self):
        self.board = list[list[int]] # -1 is white, 1 is black, 0 is unclaimed
        self.curr_player = "black"
        self.BOARD_SIZE = 8

    def update(self, last_play: tuple) -> None:
        # for each direction from last_play, check each square in that direction. If it is the oppostie color, keep going
        # if not, then stop. If stopped on a square of the same color as last_play, flip all reached squares
        # If oob or empty, move on
        to_change = {}
        play_color = self.board[last_play]
        for ray in self.get_rays(last_play):
            ray_list = list[tuple]
            curr: tuple = self.get_ray_next()
            while self.board[curr] == (-1) * play_color:
                if self.oob_test(curr):
                    break
                ray_list.append(curr)
                curr = self.get_ray_next(curr)
            if self.board[curr] == play_color and not self.oob_test(curr):
                to_change.append(ray_list)
            else:
                continue

    def get_rays(self, square: tuple) -> list[str]:
        # TODO: get every direction from the given square that has at least one square in it
        pass

    def oob_test(self, square: tuple) -> bool:
        if square[0] < 0 or square[0] > 7 or square[1] < 0 or square[1] > 7:
            return True
        return False

    def get_ray_next(self, square: tuple, direction: str):
        # TODO: get next square in this direction
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