import numpy as np
from gtclab.base.player import Player
from gtclab.base.state import State
from gtclab.base.tree import Tree

class ExtensiveGame:
    def __init__(self, tree):
        if self.is_tree_proper_extensive_game(tree):
            self.tree = tree
        else:
            raise RuntimeError("Extensive Game is not well defined.")

    def __repr__(self):
        return f"""Extensive Game :  {self.tree}"""
    
    
    def get_subgame(self, state_label):
        # TODO: Construct a game from the subtree of state.state_label.
        if state_label not in self.tree.states:
            raise RuntimeError('State label not found')
        
        #New states in the subgame
        states = {}

        #Add the root state to the subgame
        states[1] = self.tree.get_state(state_label)
        states[1].parent = None

        #List of states with children to add to the subgame
        l = []

        #If the root state has children, prepare to add them to the subgame
        if states[1].children != []:
            l.append(states[1])


        key = 1 #Key for the new subgame states dictionary
        #While the state has children, add the children to the subgame
        while l != []:
            state = l.pop(0) #Get the first state in the list

            #For every child of the state, add it to the subgame
            for child in state.children:
                key += 1
                #Add the child to the subgame
                states[key] = self.tree.get_state(child)

                #If the child has children, add it to the list of states to add to the subgame
                if self.tree.get_state(child).children != []:
                    l.append(states[key])
            
                
        


        sub_tree = Tree(states)
        sub_tree.num_players = self.tree.num_players
        sub_tree.players = self.tree.players

        #Create subgame from the states
        subgame = ExtensiveGame(sub_tree)



       
        

        return subgame

    def is_tree_proper_extensive_game(self, tree):
        #TODO: Check if the tree is a proper extensive game, based on the three criteria stated below.
        '''
        Criteras
        1. Every state should have a valid player defined.
        2. if state.player is not num_players+1, state.children cannot be empty.
        3. leaf node should have utilities defined.
        '''
        
        # for i in range(1, len(tree.states) + 1):
        #     if tree.states[i].get_player() is None:
        #         print("Player is None")
        #         return False
        #     if tree.states[i].get_player() != tree.num_players + 1 and tree.states[i].children == []:
        #         print("If state player is not leaf player, children cannot be empty")
        #         print("player: ", tree.states[i].get_player())
        #         print("children: ", tree.states[i].children)
        #         return False
        #     if tree.is_leaf(i) and tree.states[i].utilities == {}:
        #         print("Leaf node should have utilities defined")
        #         print("i: ", i)
        #         print("Current State: ", tree.get_state(i))
        #         return False
            

        for state in tree.states:

            #Every state should have a valid player defined
            if tree.states[state].get_player() is None:
                print("Failing on Player is none")
                return False
            
            #If state.player is not num_players+1, state.children cannot be empty
            if tree.states[state].get_player() != tree.num_players + 1 and tree.states[state].children == []:
                print("Failing on children is empty, but not leaf node")
                return False
            
            #Leaf node should have utilities defined
            if tree.states[state].get_player() == tree.num_players + 1 and tree.states[state].utilities == {}:
                print("num players: ", tree.num_players)
                print("Failing on utilities is empty in leaf node")
                print("state: ", state)
                print(tree.states[state])
                return False
            

            
        return True
    


