from .state import State
from .player import Player

class Tree:
    def __init__(self, states={}):
        self.states = states # This is a dictionary of states. key: state_label, value: state obj
        
        self.num_players = 1

        self.players = []
        for n in range(self.num_players+2):
            player = Player(n)
            self.players.append(player)
    
    
    def __repr__(self):
        state_str = f'Tree : '
        if self.states: 
            state_str += f'\n States: {self.states}\n'
        return state_str
    

    def create_state(self, state_label):
        #TODO: Create a new state with the label "state_label". If such a state already exists, raise an error with an appropriate message.
        if state_label in self.states:
            raise ValueError('create_state - State with label ', state_label, ' already exists')
        else:
            self.states.update({state_label: State(state_label)})

    def add_state(self,state_obj):
        #TODO: Add a state "state_object" to the tree's state list "self.states". If such a state already exists in the list, raise an error with an appropriate message.
        if state_obj in self.states:
            raise ValueError('add_state - State ', state_obj.label, ' already exists in the tree')
        else:
            self.states.update({state_obj.label: state_obj})  
    
    def get_state(self, state_label):
        #TODO: Return a state with the "state_label", if present in the tree's state list "self.states". Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('get_state - State with label ', state_label, ' does not exist in the tree')
        else:
            return self.states[state_label]

    def add_player(self, player_label):
        #TODO: Add a player with label "player_label" to the tree's player list "self.players". Also, increment "self.num_players" by 1. If such a player already exists in the list, raise an error with an appropriate message.
        if player_label in self.players:
            raise ValueError('add_player - Player with label ', player_label, ' already exists in the tree\'s player list')
        else:
            self.players.append(Player(player_label))
            self.num_players += 1
        
    def check_player_exists(self, player_label):
        #TODO: Return true if a player with label "player_label" exists in the tree's player list "self.players". Else, return false.
        return player_label in self.players

    def add_player_to_state(self, player_label, state_obj):
        state_obj.set_player(player_label)

    def set_num_players(self, num_players):
        #TODO: Update num_players count and automatically create player objects
        self.num_players = num_players
        for i in range(num_players):
            self.add_player(i+1)

    
    def get_num_players(self):
        #TODO: Return the number of players
        return self.num_players

    def set_root(self, state_label):
        #TODO: If a state is present in the list with label "state_label", set it as the root of the tree. Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('set_root - State with label ', state_label, ' does not exist in the tree')
        else:
            self.states[state_label].parent = None

    def get_root(self):
        #TODO: Return the label of the tree's root 
        for state in self.states:
            if self.states[state].parent == None:
                return state
    
    def is_parent(self, parent_state_label, child_state_label):
        #TODO: Check if the state with label "parent_state_label" is a parent to the state with label "child_state_label". Otherwise, return False.
        if parent_state_label not in self.states:
            raise ValueError('is_parent - Parent state with label ', parent_state_label, ' does not exist in the tree')
        elif child_state_label not in self.states:
            raise ValueError('is_parent - Child state with label', child_state_label, ' does not exist in the tree')
        else:
            return child_state_label in self.states[parent_state_label].children

    def set_child(self, parent_state_label, child_state_label):
        #TODO: If either or both states with labels "parent_state_label" and "child_state_label" does not exist within the tree's state list, then raise an error with an appropriate message. Otherwise, set the state with label "child-state_label" as a child of state with label "parent_state_label".
        if parent_state_label not in self.states:
            raise ValueError('set_child - Parent state with label ', parent_state_label, ' does not exist in the tree')
        elif child_state_label not in self.states:
            raise ValueError('set_child - Child state with label', child_state_label, ' does not exist in the tree')
        else:
            self.states[child_state_label].parent = parent_state_label
            self.states[parent_state_label].children.append(child_state_label)

    def get_children(self, state_label):
        #TODO: If the state with label "state_label" exists in the tree's state list, then return all child nodes of that state. Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('get_children - State with label ', state_label, ' does not exist in the tree')
        else:
            return self.states[state_label].children

    def is_leaf(self, state_label):
        #TODO: If the state with "state_label" exists within the tree's state list, then return True if it is a leaf node, or False otherwise. However, if such a state does not exist in the list, then raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('is_leaf - State with label ', state_label, ' does not exist in the tree')
        else:
            if self.states[state_label].children == []:
                return True
            else:
                return False

    def set_utilities(self, state_label, utilities):
        #TODO: If the state with "state_label" exists within the tree's state list, then set the utility values to that state as long as it is a leaf node. Otherwise, raise an error with an appropriate message. 
        if state_label not in self.states:
            raise ValueError('set_utilities - State with label ', state_label, ' does not exist in the tree')
        else:
            if self.is_leaf(state_label):
                self.states[state_label].utilities[0] = utilities
            else:
                raise ValueError('set_utilities - State with label ', state_label, ' is not a leaf node')


    def get_utilities(self, state_label):
        #TODO: If the state with "state_label" exists within the tree's state list, then return the utilities at that state, if it is a leaf node. Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('get_utilities - State with label ', state_label, ' does not exist in the tree')
        else:
            if self.is_leaf(state_label):
                return self.states[state_label].utilities
            else:
                raise ValueError('get_utilities - State with label ', state_label, ' is not a leaf node')
    
    def set_chance_prob(self, state_label, chance_prob):
        #TODO: If the state with "state_label" exists within the tree's state list and if its player is nature, then set the chance probability to that state. Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('set_chance_prob - State with labelv ', state_label, ' does not exist in the tree')
        else:
            #If state player is nature
            if self.states[state_label].get_player().player_label == 0:
                self.states[state_label].chance_prob = chance_prob
            else:
                raise ValueError('set_chance_prob - State with label ', state_label, ' is not a nature node')
    
    def get_chance_prob(self,state_label):
        #TODO: If the state with "state_label" exists within the tree's state list and if its player is nature, then return the chance probability to that state. Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('get_chance_prob - State with label ', state_label, ' does not exist in the tree')
        else:
            #If state player is nature
            if self.states[state_label].get_player().player_label == 0:
                return self.states[state_label].chance_prob
            else:
                raise ValueError('get_chance_prob - State with label ', state_label, ' is not a nature node')
    
    def set_player_infoset(self, player_label, info_set_label, states):
        #TODO: Check if each state in states has the player defined as "player_label". If yes, then if the player with label "player_label" does not have an information set with label "info_set_label", append it to the list of player's information sets and set the "info_set_label" in each state in states. Otherwise, raise an error with an appropriate message.
        for state in states:
            if state.get_player().player_label == player_label:
                if info_set_label not in self.players[player_label].info_set_labels:
                    self.players[player_label].info_set_labels.append(info_set_label)
                    state.set_info_set(info_set_label)
                else:
                    raise ValueError('set_player_infoset - Player with label ', player_label, ' already has an information set with label ', info_set_label)
    
    def add_state_infoset(self, player_label, info_set_label, state_label):
        #TODO: Check if the state with label "state_label" has the player defined as "player_label". If yes, then if the player with label "player_label" does not have an information set with label "info_set_label", append it to the list of player's information sets and set the "info_set_label" in the state with label "state_label". Otherwise, raise an error with an appropriate message.
        if state_label not in self.states:
            raise ValueError('add_state_infoset - State with label ', state_label, ' does not exist in the tree')
        elif self.states[state_label].get_player().player_label != player_label:
            raise ValueError('add_state_infoset - State with label ', state_label, ' does not have player ', player_label)
        elif self.states[state_label].get_player().player_label == player_label:
            if info_set_label not in self.players[player_label].info_set_labels:
                self.players[player_label].info_set_labels.append(info_set_label)
                self.states[state_label].set_info_set(info_set_label)
            else:
                raise ValueError('add_state_infoset - Player with label ', player_label, ' already has an information set with label ', info_set_label)
    
    def get_states_in_infoset(self, info_set_label):
        #TODO: Identify all the states corresponding to a specific label "info_set_label" and return them.
        states = []
        for state in self.states:
            if info_set_label in state.info_set_label:
                states.append(state)
        return states