# Compute the reduced game using iterative elimination of dominated strategies for a given normal form game. 

from ..models.normalgame import NormalGame

class IEDS:
    
    def __init__(self, normal_game):
        # This works only for normal game representation.
        if isinstance(normal_game, NormalGame):
            self.original_game = normal_game
            self.reduced_game = normal_game
        else:
            raise RuntimeError("IEDS can only be computed for Normal games.")
        self.calc_reduced_game()
    
    def calc_reduced_game(self):
        # TODO: Implement Iterative Elimination of Dominated Strategies for basic principles (i.e. from the definition)
        reduced_C = {}
        reduced_U = {}

        for i in range(1, len(self.reduced_game.players) + 1):
            
            utility_matrix = self.reduced_game.players[i].get_utility_matrix()
            choice_set = self.reduced_game.players[i].get_choice_set()
            dominated_choice = self.is_dominated(utility_matrix)

            if dominated_choice == None:
                continue

            #Remove one choice from choice set as there are now 1 less choices
            choice_set.remove(choice_set[-1])

            #Remove dominated choice from utility matrix
            count = 0 #Iterator to find what row we are removing
            for row in utility_matrix:
                if row == dominated_choice:
                    utility_matrix.remove(row)
                    break
                count += 1

            #Remove ith column from every other players utility matrix
            for p in range(1, len(self.reduced_game.players) + 1):

                #Skip if we are looking at the same player
                if self.reduced_game.players[p] == self.reduced_game.players[i]:
                    continue

                #Remove ith column from every other players utility matrix
                other_utility_matrix = self.reduced_game.players[p].get_utility_matrix()

                for j in range(len(other_utility_matrix)):
                    for k in range(len(other_utility_matrix[j])):
                        if k == count:
                            other_utility_matrix[j].remove(other_utility_matrix[j][k])

            #Update utility matrix
            self.reduced_game.players[i].set_utility_matrix(utility_matrix)
            self.reduced_game.players[i].set_choice_set(len(choice_set))
        
            #Update reduced game
            reduced_C[i] = len(choice_set)
            reduced_U[i] = utility_matrix

        # Save the reduced choice profile space and utility matrices in the following two variables:
        # reduced_C = [['a'], ['c']]
        # reduced_U = ['1', '-1']
        
        # Define the reduced normal-form game using the reduced choice profile space and the reduced utility matrices
        if not reduced_C == {} or not reduced_U == {}:
            self.reduced_game = NormalGame(self.original_game.num_players, reduced_C, reduced_U)
        else:
            return self.reduced_game
        
        # Define the stopping criterion
        if self.reduced_game == self.original_game: #TODO 
            # TODO: Stop the recursion only when the game does not reduce at all players.
            return self.reduced_game
        else:
            # TODO: Continue the recursion until the game can no longer be reduced. Make sure the recursion includes a round-robin iteration of the players.
            self.calc_reduced_game()

    def is_dominated(self, utility_matrix):
        #Compare every choice to every other choice
        for choice_1 in utility_matrix:
            for choice_2 in utility_matrix:

                #Skip if we are looking at the same choice
                if choice_1 != choice_2:
                    #Check if choice_1 dominates choice_2
                    if all(choice_1[i] >= choice_2[i] for i in range(len(choice_1))):
                        return choice_2
                    
                    #Check if choice_2 dominates choice_1
                    if all(choice_2[i] >= choice_1[i] for i in range(len(choice_2))):
                        return choice_1
        
        #No dominated choice found
        return None
            

    def __repr__(self): 
        return f"""Reduced Game due to IEDS : {self.reduced_game}\n"""