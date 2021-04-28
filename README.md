# ML-Game-Playing-Project
Explanation:

  -pit.py is used for playing the game.

  -main.py is used for training the ai.

  -./squares/ contains the actual squares game code.

  -This implementation of alpha go is based on Surag Nair's https://github.com/suragnair/alpha-zero-general .
  

Requirements:

  To play against: Python 3 is needed. 

  Python libraries numpy and pygame are needed as well. python3 pit.py

To train:

  A pytorch docker image needs to be run first. There are also a lot of python libraries involved.

  Getting this running on my desktop computer was a big ordeal. If you can run setup_env.sh then you should be OK, though. 


Project Description:
Implement a game playing algorithm for an AI to play against a human in a game of squares against a human (the game seems to go by multiple names). The game “board” starts with a grid of dots, for example, an 11-row by 11-column matrix of dots. On a player’s turn, they must connect a pair of adjacent dots. At the end of the game, each pair of adjacent dots will have been connected forming a grid of squares, a 10x10 grid in the previous example. When a player’s line segment completes one or two small squares connecting adjacent dots, they capture the squares, enter their initial(s) inside the completed squares, and get to go again (get to draw another line segment). Otherwise, the next player goes, drawing a line to connect two adjacent dots.
This AI project will involve the minimax search algorithm with alpha-beta pruning, which we will likely implement in class. You will combine that algorithm with an existing open source implementation of AlphaGo Zero which utilizes deep reinforcement learning.

Useful Links:
From Akansha Goel to Everyone:  10:31 AM
I have collected a few common links, it might help :
  https://deepmind.com/research/case-studies/alphago-the-story-so-far#muzero

  https://www.youtube.com/watch?v=MPXGiowUr0o

  https://github.com/topics/alphago

  https://github.com/maxpumperla/deep_learning_and_the_game_of_go

  https://github.com/suragnair/alpha-zero-general

  https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go

  https://web.stanford.edu/~surag/posts/alphazero.html

  https://github.com/deepmind?page=2

  https://github.com/topics/alphago-zero

  https://github.com/YuriCat/MuZeroJupyterExample?utm_source=catalyzex.com

  https://github.com/pmuens/alphago

  https://medium.com/dataseries/deepminds-muzero-is-one-of-the-most-important-deep-learning-systems-ever-created-347442a6793

Chat is on 
  https://web.groupme.com/
