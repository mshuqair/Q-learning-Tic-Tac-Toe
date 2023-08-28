import tkinter as tk
import pickle
from Tic_Tac_Toe_Q_Learning import Game, QPlayer     # Classes used for Tic Tac Toe

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X", epsilon=epsilon)
player2 = QPlayer(mark="O", epsilon=epsilon)
game = Game(root, player1, player2)

N_episodes = 250000
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "Tic_Tac_Toe_Trained/Q_epsilon_09_Nepisodes_{}.p".format(N_episodes)
pickle.dump(Q, open(filename, "wb"))
