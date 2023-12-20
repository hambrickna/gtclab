from gtclab.base.player import Player
import numpy as np

class NormalGame:
    def __init__(self, num_players, num_choices, utility_matrices):
        #Note : utility_matrices is a dict of matrices. k: player_label and v: utility_matrix for player
        self.num_players =  num_players #int
        self.num_choices =  num_choices #dict-> k: player_label and v: num of choices for player
        self.players = {}#[0]*(self.num_players)

        for n in range(1, self.num_players+1): # Players are labeled using natural numbers(1:num_players), Nature is labeled as Player 0.
            self.players[n] = Player(n)
            self.players[n].set_choice_set(num_choices.get(n))
            self.players[n].set_utility_matrix(utility_matrices.get(n))

    # TODO add print
    def __repr__(self): 
        return f"""
            NormalGame : {self.players}\n
            num_players: {self.num_players}\n
            num_choices: {self.num_choices}\n        
        \n"""

    def is_two_player_zero_sum(self):
        '''
        Criteria
        1. Num of players should be 2.
        2. Player's utility_matrix should sum to all zero matrix
        '''
        if self.num_players != 2:
            return False
        
        A = np.array(self.players[1].get_utility_matrix())
        B = np.array(self.players[2].get_utility_matrix())
        C = np.add(A, B.T)

        for row in C:
            if not all(row[i] == 0 for i in range(len(row))):
                return False
            
        return True
                
    
    def print(self):
        print(self.__repr__())

