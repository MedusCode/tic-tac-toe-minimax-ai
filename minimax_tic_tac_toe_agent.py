# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Nikita Andreev


class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        if not self.game or not state:
            return None

        if self.game.to_move(state) != self.symbol:
            print('It is not my turn')
            return None

        _, best_action = self.minimax(self.game, state)

        return best_action

    def minimax(self, game, state):
        """
        Applies the minimax algorithm to determine the best move
        """
        return self.max_value(game, state)

    def max_value(self, game, state):
        """
        Computes the best value and action for the agent's turn (MAX player).
        """
        if game.is_terminal(state):
            return self.game.utility(state, self.symbol), None

        best_value, best_action = float("-inf"), None

        for action in self.game.actions(state):
            value, _ = self.min_value(game, game.result(state, action))

            if value > best_value:
                best_value, best_action = value, action

        return best_value, best_action


    def min_value(self, game, state):
        """
        Computes the best value and action for the opponent's turn (MIN player).
        """
        if game.is_terminal(state):
            return self.game.utility(state, self.symbol), None

        best_value, best_action = float("inf"), None

        for action in self.game.actions(state):
            value, _ = self.max_value(game, game.result(state, action))

            if value < best_value:
                best_value, best_action = value, action

        return best_value, best_action
