"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
from random import randint

import sys
import math

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def distance(p0, p1):
    """
    Returns the distance between two points on the Isolation board. Used to
    calculate the distance between two players in the heuristic functions.

    Parameters
    ----------
    p0 : (int, int)
         A tuple giving the current location of the active player on the Isolation board.

    p1 : (int, int)
         A tuple giving the current location of the opponent player on the Isolation board.

    Returns
    -------
    float
        The distance between the two players on the Isolation board
    """
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def aggressive_score(game, player):
    """Calculates and returns the distance between the two players in the 
    negative direction to yield higher score when players are closer.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state
    """
    opp_loc = game.get_player_location(game.get_opponent(player))
    own_loc = game.get_player_location(player)
    return -1*distance(own_loc, opp_loc)

def conservative_score(game, player):
    """Calculates and returns the distance between the two players 
     to yield higher score when players are farther.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state
    """
    opp_loc = game.get_player_location(game.get_opponent(player))
    own_loc = game.get_player_location(player)
    return distance(own_loc, opp_loc) 
    
def improved_conservative_score(game, player):
    """Calculates and returns score equal to the difference in the number 
    of moves available to the two players weighted by the distance between
    the two players.
    
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    
    Returns
    -------
    float
        The heuristic value of the current game state
    """
    opp_loc = game.get_player_location(game.get_opponent(player))
    own_loc = game.get_player_location(player)
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return distance(own_loc, opp_loc) * float(own_moves - opp_moves)


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    #Calling Improved Conservative Player and returning the score value
    return improved_conservative_score(game, player)



class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        
        #Opening move start from center
        move = (3,3) 

        if not legal_moves:
            return (-1, -1)

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.iterative == True:
                for depth in range(1,sys.maxsize):
                    _ , move = getattr(self, self.method)(game, depth)                   
            else:
                depth = self.search_depth
                _ , move = getattr(self, self.method)(game, depth)

        except Timeout: 
            pass

        # Return the best move from the last completed search iteration
        return move
        #raise NotImplementedError

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        def max_value(game, minimax_depth):

            if self.time_left() < self.TIMER_THRESHOLD:
               raise Timeout()

            #print("max_depth",minimax_depth)
            if minimax_depth >= depth:  
               max_score = self.score(game, self)
               #print("max_score", max_score)
               return max_score
            v = float("-inf")
            #print("max legal moves", game.get_legal_moves())            
            for m in game.get_legal_moves():
                #print("max move", m)
                v = max(v, min_value(game.forecast_move(m), minimax_depth+1))
            return v

        def min_value(game, minimax_depth):

            if self.time_left() < self.TIMER_THRESHOLD:
               raise Timeout()

            #print("min_depth", minimax_depth)           
            if minimax_depth >= depth:   
               min_score = self.score(game, self)
               #print("min_score", min_score)
               return min_score
            v = float("inf")
            #print("min legal moves", game.get_legal_moves())
            for m in game.get_legal_moves():
                #print("min move", m)
                v = min(v, max_value(game.forecast_move(m), minimax_depth+1))
            return v

        best_score = float("-inf")
        best_move = None
        #print("Depth legal moves", game.get_legal_moves())
        for m in game.get_legal_moves():
            #print("Depth", depth, "Move", m)
            v = min_value(game.forecast_move(m), 1)
            if v > best_score:
               best_score = v
               best_move = m

        #print("\nbest_score", best_score, "best_move", best_move)
        return best_score, best_move


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        #print("\n Alpha-Beta \n")

        def max_value(game, minimax_depth, a, b):

            if self.time_left() < self.TIMER_THRESHOLD:
               raise Timeout()

            #print("max_depth",minimax_depth)
            if minimax_depth >= depth:  
               max_score = self.score(game, self)
               #print("max_score", max_score)
               return max_score
            v = float("-inf")
            #print("max legal moves", game.get_legal_moves())            
            for m in game.get_legal_moves():
                #print("max move", m)
                v = max(v, min_value(game.forecast_move(m), minimax_depth+1, a, b))
                if v >= b:
                    return v
                a = max(a,v)
            return v

        def min_value(game, minimax_depth, a, b):

            if self.time_left() < self.TIMER_THRESHOLD:
               raise Timeout()

            #print("min_depth", minimax_depth)           
            if minimax_depth >= depth:   
               min_score = self.score(game, self)
               #print("min_score", min_score)
               return min_score
            v = float("inf")
            #print("min legal moves", game.get_legal_moves())
            for m in game.get_legal_moves():
                #print("min move", m)
                v = min(v, max_value(game.forecast_move(m), minimax_depth+1, a, b))
                if v <= a:
                    return v
                b = min(b,v)
            return v

        best_score = float("-inf")
        best_move = None
        #print("Depth legal moves", game.get_legal_moves())
        for m in game.get_legal_moves():
            #print("Depth", depth, "Move", m)
            v = min_value(game.forecast_move(m), 1, best_score, beta)
            #print("v > best_score", v, ">", best_score)
            if v > best_score:
               best_score = v
               best_move = m

        #print("\nbest_score", best_score, "best_move", best_move,"\n")
        return best_score, best_move

        #raise NotImplementedError
