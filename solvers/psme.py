# Compute pure strategy minimax equilibrium for a 2-player, zero-sum normal form game. 
import numpy as np
from ..models.normalgame import NormalGame

class PSME:
    
    def __init__(self,normal_game):
        # This works only for Two Player Zero Sum Normal game representation.
        if (isinstance(normal_game, NormalGame) and normal_game.is_two_player_zero_sum()):
            self.game = normal_game
        else:
            raise RuntimeError("PSME can only be computed for Two Player Zero Sum Normal games.")
        self.psme = None
        self.calc_psme()
    
    def calc_psme(self):
        # TODO: Implement Pure Strategy Minimax Equilibrium (i.e. from the definition)

        minimum_utility = []
        maximum_utility = []
        pos = []
        
        #Player 1's utility matrix
        A = np.array(self.game.players[1].get_utility_matrix())

        for row in range(np.shape(A)[0]):
            minimum_utility.append(np.min(A[row, :]))
            pos.append((row, list(A[row, :]).index(np.min(A[row, :]))))

        for col in range(np.shape(A)[1]):
            maximum_utility.append(np.max(A[:, col]))

        psme = []
        while (min(maximum_utility) == max(minimum_utility)):
            psme.append(pos[minimum_utility.index(max(minimum_utility))])
            minimum_utility.pop(minimum_utility.index(max(minimum_utility)))
            maximum_utility.pop(maximum_utility.index(min(maximum_utility)))
            pos.pop(minimum_utility.index(max(minimum_utility)))

        self.psme = psme

        if self.psme == []:
            self.psme = "no pure strategy minimax equilibrium exists"
        
        return self.psme
    
    def __repr__(self): 
        return f"""PSME : {self.psme}\
        \n"""