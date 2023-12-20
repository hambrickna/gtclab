

class State:
    def __init__(self, label=None):
        self.label = label # This is a user-defined label given to the state
        self.parent = None # This state is the parent to the current state. Root parent: None, Other states' parents: 1: num_states
        self.children = []
        self.player = None # This player controls this state. Player Label: 1:num_players, Nature: 0, Leaf: num_players+1
        self.utilities = {}
        self.info_set_label = None
        self.chance_prob = None
    
    def __repr__(self):
        state_str = f'State : {str(self.label)}'
        if self.player: 
            state_str += f'\n\tPlayer: {self.player}' 

        return state_str
    
    def set_player(self, player):
        #TODO: Set the player for this state
        self.player = player

    def get_player(self):
        #TODO: Return the player for this state
        return self.player
    
    def set_info_set(self, info_set_label):
        #TODO: Set the information set label for this state
        self.info_set_label = info_set_label

    def get_info_set(self):
        #TODO: Return the information set label for this state.
        return self.info_set_label

