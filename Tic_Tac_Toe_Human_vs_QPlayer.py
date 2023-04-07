import sys
import tkinter as tk
import pickle as pickle
from Tic_Tac_Toe_Q_Learning import Game, HumanPlayer, QPlayer


def difficulty_select(x):
    global Q
    global player2
    if x == 1:
        print("Easy difficulty selected")
        Q = pickle.load(open("Tic_Tac_Toe_Trained/Q_epsilon_09_Nepisodes_10000.p", "rb"))
        window.destroy()
    if x == 2:
        print("Normal difficulty selected")
        Q = pickle.load(open("Tic_Tac_Toe_Trained/Q_epsilon_09_Nepisodes_25000.p", "rb"))
        window.destroy()
    if x == 3:
        print("Hard difficulty selected")
        Q = pickle.load(open("Tic_Tac_Toe_Trained/Q_epsilon_09_Nepisodes_50000.p", "rb"))
        player2 = QPlayer(mark="O", epsilon=0.1)
        window.destroy()
    if x == 4:
        print("Impossible difficulty selected")
        Q = pickle.load(open("Tic_Tac_Toe_Trained/Q_epsilon_09_Nepisodes_100000.p", "rb"))
        window.destroy()
    return 0


player1 = HumanPlayer(mark="X")
player2 = QPlayer(mark="O", epsilon=0)

while True:
    Q = 0
    window = tk.Tk()
    window.geometry("280x300")
    window.resizable(width=False, height=False)
    window.title("Tic Tac Toe Game")

    Line = tk.Label(window, text="Select Difficulty:", font=('Tahoma', 12, 'bold'), fg='black', height=3, width=24)

    button_A = tk.Button(window, text="Easy", font=('Tahoma', 8, 'bold'), fg='white', height=2, width=24,
                         command=lambda: difficulty_select(1), bg='blue')
    button_B = tk.Button(window, text="Normal", font=('Tahoma', 8, 'bold'), fg='white', height=2, width=24,
                         command=lambda: difficulty_select(2), bg='green')
    button_C = tk.Button(window, text="Hard", font=('Tahoma', 8, 'bold'), fg='white', height=2, width=24,
                         command=lambda: difficulty_select(3), bg='orangered')
    button_D = tk.Button(window, text="Impossible!", font=('Tahoma', 8, 'bold'), fg='white', height=2, width=24,
                         command=lambda: difficulty_select(4), bg='crimson')
    button_E = tk.Button(window, text="Close Game", font=('Tahoma', 8, 'bold'), fg='white', height=1, width=12,
                         command=lambda: sys.exit(), bg='Black')

    Line.pack(fill=tk.BOTH, padx=2, pady=3)
    button_A.pack(padx=2, pady=3)
    button_B.pack(padx=2, pady=3)
    button_C.pack(padx=2, pady=3)
    button_D.pack(padx=2, pady=3)
    button_E.pack(padx=2, pady=3)

    window.mainloop()

    root = tk.Tk()
    if Q == 0:
        root.destroy()
    else:
        game = Game(root, player1, player2, Q=Q)
        game.reset()
        game.play()
    root.mainloop()
