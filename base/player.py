from numpy import isin


class Player:

    def __init__(self, player_label, player_type='normal'): 
        # By default, a player is set for normal-form representation. For extensive games, player_type = 'extensive'
        if player_type.lower() not in ['normal', 'extensive']:
            raise RuntimeError("Player type should be 'normal' or 'extensive'")
        if not isinstance(player_label, int):
            raise RuntimeError("Player label should be an integer")
        self.player_label = player_label #(if player_label is num_players + 1, then leaf node; if player_label is 0, then nature)
        self.choice_set = None
        self.utility_matrix = None
        self.info_set_labels = None
        self.player_type = player_type.lower()
    
    def __repr__(self): 
        return f'Player(player_label : {self.player_label },choice_set : {self.choice_set}, utility_matrix : {self.utility_matrix}, player_type :  {self.player_type})'

    def set_choice_set(self, num_choices):
        # TODO: Construct the set of choices from "num_choices" array for every player in normal-form games.
        # NOTE: The length of "num_choices" should be equal to the number of players. If not, return an appropriate error message.
        if self.player_type == 'normal':
            self.choice_set = list(range(0, num_choices))
        else:
            raise NotImplemented('Choices not implemented for extensive games')

    def get_choice_set(self):
        # TODO: Return the set of choices for every player in normal-form games
        if self.player_type == 'normal':
            return self.choice_set
        else:
            raise NotImplemented('Choices not implemented for extensive games')

    def set_utility_matrix(self, utility_matrix):
        # TODO: Set the utility matrix for normal-form games
        if self.player_type == 'normal':
            self.utility_matrix = utility_matrix
        else:
            raise NotImplemented('Utility Matrix not implemented for extensive games')

    def get_utility_matrix(self):
        # TODO: Return the utility matrix for normal-form games
        if self.player_type == 'normal':
            return self.utility_matrix
        else:
            raise NotImplemented('Utility Matrix not implemented for extensive games')