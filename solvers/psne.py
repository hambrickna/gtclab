# Compute pure strategy Nash equilibrium for a given normal form game. 
import numpy as np

from ..models.normalgame import NormalGame

class PSNE:
    
    def __init__(self, normal_game):
        # This works only for normal game representation.
        if isinstance(normal_game, NormalGame):
            self.normal_game = normal_game
        else:
            raise RuntimeError("PSNE can only be computed for Normal games.")
        self.psne = None
        self.calc_psne()
    
    def calc_psne(self):
        # TODO: Calculate and return PSNE for basic principles (i.e. from the definition)
        # Save the PSNE in the following format. If there is no PSNE, return 'None' and print "This game has no PSNE"
        # self.psne = ['(Game.player[1].choice_set[1], ..., Game.player[n].choice_set[1])']

        #Calculate the PSNE for N-player normal form games
        all_best_response = {}

        for p in range(1, len(self.normal_game.players) + 1):
            utility_matrix = self.normal_game.players[p].get_utility_matrix()

            player_best_response = []
            for col in range(len(utility_matrix[0])):
                max = utility_matrix[0][col]
                pos = []
                for row in range(len(utility_matrix)):
                    if utility_matrix[row][col] == max:
                        max = utility_matrix[row][col]
                        if p == 1:
                            pos.append((row, col))
                        else:
                            pos.append((col, row))

                    elif utility_matrix[row][col] > max:
                        max = utility_matrix[row][col]
                        if p == 1:
                            pos = [(row, col)]
                        else:
                            pos = [(col, row)]

                player_best_response.extend(pos)

            all_best_response[p] = player_best_response

        #Find the intersection of all best responses
        psne = []
        for response in all_best_response[1]:
            if response in all_best_response[2]:
                psne.append(response)

        p1_choices = []
        p2_choices = []
        
        if len(psne) == 0:
            print("This game has no PSNE")
            return None
        else:
            self.psne = []
            for i in range(len(psne)):
                p1_choices.append(psne[i][0])
                p2_choices.append(psne[i][1])

            self.psne.append(p1_choices)
            self.psne.append(p2_choices)
                
        return self.psne

    def is_best_response(self):
        '''
        Given all other players' choices, check if a given choice of a given player is a best response strategy.
        '''
        raise NotImplemented('is_best_response function not implemented.')
    
    def __repr__(self): 
        return f"""PSNE : {self.psne}\
        \n"""