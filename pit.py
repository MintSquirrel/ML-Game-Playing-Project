import os
import numpy as np
import Arena
from MCTS import MCTS
from utils import dotdict
from squares.SquaresGame import SquaresGame
from squares.SquaresPlayers import HumanSquaresPlayer, RandomPlayer, GreedyRandomPlayer
from squares.pytorch.NNet import NNetWrapper

print("New match starting.")
print("The AI makes the first move.")
print("See grid_guide.png to know which numbers to enter for each possible move. Good luck!")

g = SquaresGame(n=4)

hp1 = HumanSquaresPlayer(g).play
hp2 = HumanSquaresPlayer(g).play

rp1 = RandomPlayer(g).play
rp2 = RandomPlayer(g).play

grp1 = GreedyRandomPlayer(g).play
grp2 = GreedyRandomPlayer(g).play

numMCTSSims = 50
n1 = NNetWrapper(g)
n1.load_checkpoint(os.path.join('./', 'models/'), 'best.pth.tar')
args1 = dotdict({'numMCTSSims': numMCTSSims, 'cpuct': 1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

n2 = NNetWrapper(g)
n2.load_checkpoint(os.path.join('./', 'models/'), 'best.pth.tar')
args2 = dotdict({'numMCTSSims': numMCTSSims, 'cpuct': 1.0})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

# Play AlphaZero versus Human
p1 = n1p
p2 = hp1
arena = Arena.Arena(p1, p2, g, display=SquaresGame.display)
oneWon, twoWon, draws = arena.playGames(2, verbose=True)
print("oneWon: {}, twoWon: {}, draws: {}".format(oneWon, twoWon, draws))

# # Play Greedy vs Greedy
# p1 = grp1
# p2 = grp2
# arena = Arena.Arena(p1, p2, g, display=SquaresGame.display)
# oneWon, twoWon, draws = arena.playGames(100, verbose=False)
# print("oneWon: {}, twoWon: {}, draws: {}".format(oneWon, twoWon, draws))

# # Play AlphaZero vs Greedy
# p1 = n1p
# p2 = grp2
# arena = Arena.Arena(p1, p2, g, display=SquaresGame.display)
# oneWon, twoWon, draws = arena.playGames(2, verbose=False)
# print("oneWon: {}, twoWon: {}, draws: {}".format(oneWon, twoWon, draws))