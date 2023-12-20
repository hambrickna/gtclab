# Compute mixed strategy Nash equilibrium for a 2-player zero-sum normal form game using linear programming techniques. 
import numpy as np
import cvxpy as cp
from ..models.normalgame import NormalGame

class MSNE_LP:
    
    def __init__(self,normal_game):
        # This works only for Two Player Zero Sum Normal game representation.
        if (isinstance(normal_game, NormalGame) and normal_game.is_two_player_zero_sum()):
            self.game = normal_game
        else:
            raise RuntimeError("MSNE_LP can only be computed for Two Player Zero Sum Normal games.")
        self.msne_lp = None
        self.calc_msne_lp() # Compute MSNE_LP in the game
    
    def calc_msne_lp(self):
        # TODO: Implement Mixed Strategy Nash Equilibrium using LP Solvers (i.e. from the definition)
        # Save the mixed strategy Nash equilibrium in the following format:
        self.msne_lp = np.array([[0.5, 0.2, 0.3], [0.1, 0.45, 0.45]])



        constraints1 = []
        constraints2 = []

        t1 = cp.Variable()
        t2 = cp.Variable()

        objective1 = cp.Minimize(t1)
        objective2 = cp.Minimize(t2)


        return self.msne_lp
        
        
    
    def __repr__(self): 
        return f"""MSNE LP : {self.msne_lp}\
        \n"""