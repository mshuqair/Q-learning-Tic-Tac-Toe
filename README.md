# Q-learning-Tic-Tac-Toe
Reinforcement learning of the game of Tic Tac Toe in Python.

This is a fork of the original work.

## Updates
I'll be listing the updates here...

![](images/image_1.png) ![](images/image_2.png)


## Basic usage
To play Tic Tac Toe against a computer player trained by playing 250,000 games against itself, enter

`python Tic_Tac_Toe_Human_vs_QPlayer.py` 

at the command line. (You'll need to have Python installed with the Numpy package). This will bring up a simple GUI in which clicking on any of the buttons causes the mark "X" to appear, and the computer immediately responds with a countermove (Image 2).

![](images/image_3.png)  
**Figure 1.** A Tic Tac Toe game that resulted in a tie (cat's game).

I could not beat the `QPlayer,` I would like to hear if you can!

Alternatively, the user can also play against the "T-hand" player by setting `player2 = THandPlayer(mark="O")` at the bottom of the code. The "T-hand" player makes winning moves if they are available and blocks those of opponents (cf. [Boyan (1992)](http://www.cs.cmu.edu/~jab/cv/pubs/boyan.backgammon-thesis.pdf)), otherwise choosing moves at random. Unlike the QPlayer, it can frequently be beaten with the right strategy.

## Background
The implementation of Q-learning follows the pseudo-code given by Meeden [[CS63 Lab 6](https://www.cs.swarthmore.edu/~meeden/cs63/f11/lab6.php)]. A general introduction to Q-learning can be obtained from [Chapter 13](https://www.cs.swarthmore.edu/~meeden/cs63/f11/ml-ch13.pdf) of [Mitchell (1997)](http://www.cs.cmu.edu/~tom/mlbook.html), [Sutton & Barto (2012)](http://people.inf.elte.hu/lorincz/Files/RL_2006/SuttonBook.pdf), or [Watkins & Dayan (1992)](http://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf), for example.

In the game of Tic Tac Toe, at each discrete time step <a href="https://www.codecogs.com/eqnedit.php?latex=t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t" title="t" /></a>, the state <a href="https://www.codecogs.com/eqnedit.php?latex=s&space;\in&space;S" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s&space;\in&space;S" title="s \in S" /></a> of the system is defined by the marks on the board and which player's turn it is, and the available actions <a href="https://www.codecogs.com/eqnedit.php?latex=a&space;\in&space;A" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;\in&space;A" title="a \in A" /></a> by the empty squares on the board. We are looking for a policy <a href="https://www.codecogs.com/eqnedit.php?latex=\pi&space;:&space;S&space;\rightarrow&space;A" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pi&space;:&space;S&space;\rightarrow&space;A" title="\pi : S \rightarrow A" /></a> which tells us which action to take in which state to maximize our chance of winning.

Given a policy <a href="https://www.codecogs.com/eqnedit.php?latex=\pi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /></a>, at any given time each state has a certain _value_ <a href="https://www.codecogs.com/eqnedit.php?latex=V^\pi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V^\pi" title="V^\pi" /></a>, which is the expected discounted reward from following that policy for all future time:

<a href="https://www.codecogs.com/eqnedit.php?latex=V^\pi\left(s_t&space;\right&space;)\equiv&space;r_t&plus;\gamma&space;r_{t&plus;1}&plus;\gamma^2&space;r_{t&plus;2}&plus;...=\sum_{i=0}^\infty&space;\gamma^i&space;r_{t&plus;i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V^\pi\left(s_t&space;\right&space;)\equiv&space;r_t&plus;\gamma&space;r_{t&plus;1}&plus;\gamma^2&space;r_{t&plus;2}&plus;...=\sum_{i=0}^\infty&space;\gamma^i&space;r_{t&plus;i}" title="V^\pi\left(s_t \right )\equiv r_t+\gamma r_{t+1}+\gamma^2 r_{t+2}+...=\sum_{i=0}^\infty \gamma^i r_{t+i}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=r_t&space;=&space;r_t\left(s_t,&space;a_t&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_t&space;=&space;r_t\left(s_t,&space;a_t&space;\right&space;)" title="r_t = r_t\left(s_t, a_t \right )" /></a> is the _reward_ at time step <a href="https://www.codecogs.com/eqnedit.php?latex=t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t" title="t" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\gamma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\gamma" title="\gamma" /></a> represents the _discount factor_. 

In our implementation of Tic Tac Toe, we adopt the 'sign convention' that reward is positive for player "X" -- specifically, a reinforcement of `1.0` is awarded when player "X" wins, `-1.0` when player "O" wins, and `0.5` in the case of a tie. Hence, player "X" seeks to maximize value, whereas player "O" seeks to minimize it. The discount factor <a href="https://www.codecogs.com/eqnedit.php?latex=\gamma" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\gamma" title="\gamma" /></a> is given a value of `0.9`. (Its value is not so important in Tic Tac Toe as the game is deterministic with a finite time horizon).

We seek to find the optimum policy <a href="https://www.codecogs.com/eqnedit.php?latex=\pi^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pi^*" title="\pi^*" /></a> such that the value achieves a unique optimum value <a href="https://www.codecogs.com/eqnedit.php?latex=V^{\pi^*}=V^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V^{\pi^*}=V^*" title="V^{\pi^*}=V^*" /></a>. To this end, we define the evaluation function <a href="https://www.codecogs.com/eqnedit.php?latex=Q(s,a)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q(s,a)" title="Q(s,a)" /></a> as the maximum discounted cumulative reward that can be obtained by starting from state <a href="https://www.codecogs.com/eqnedit.php?latex=s" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s" title="s" /></a> and applying <a href="https://www.codecogs.com/eqnedit.php?latex=a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a" title="a" /></a> as first action:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q(s,a)\equiv&space;r(s,a)&space;&plus;&space;\gamma&space;V^*(s')" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q(s,a)\equiv&space;r(s,a)&space;&plus;&space;\gamma&space;V^*(s')" title="Q(s,a)\equiv r(s,a) + \gamma V^*(s')" /></a>,

where <a href="https://www.codecogs.com/eqnedit.php?latex=s'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s'" title="s'" /></a> is the state that results from applying action <a href="https://www.codecogs.com/eqnedit.php?latex=a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a" title="a" /></a> in state <a href="https://www.codecogs.com/eqnedit.php?latex=s" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s" title="s" /></a>.

However, to optimize the total future discounted reward, the action <a href="https://www.codecogs.com/eqnedit.php?latex=a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a" title="a" /></a> must be the one which maximizes <a href="https://www.codecogs.com/eqnedit.php?latex=Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q" title="Q" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=V^*\left(s&space;\right&space;)=\max_{a'}Q(s,a')" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V^*\left(s&space;\right&space;)=\max_{a'}Q(s,a')" title="V^*\left(s \right )=\max_{a'}Q(s,a')" /></a>

which, upon inserting into the above equation, leads to _Bellman's equation_:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q(s,a)=r(s,a)&plus;\gamma\max_{a'}Q(s,a')" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q(s,a)=r(s,a)&plus;\gamma\max_{a'}Q(s,a')" title="Q(s,a)=r(s,a)+\gamma\max_{a'}Q(s,a')" /></a>

This recursive definition of <a href="https://www.codecogs.com/eqnedit.php?latex=Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q" title="Q" /></a> provides the basis for Q-learning. Suppose we start with some initial estimate <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Q}(s,a)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Q}(s,a)" title="\hat{Q}(s,a)" /></a> of <a href="https://www.codecogs.com/eqnedit.php?latex=Q(s,a)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q(s,a)" title="Q(s,a)" /></a> and choose an action <a href="https://www.codecogs.com/eqnedit.php?latex=a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a" title="a" /></a>, thereby obtaining an immediate reward <a href="https://www.codecogs.com/eqnedit.php?latex=r" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r" title="r" /></a> and arriving at a new state <a href="https://www.codecogs.com/eqnedit.php?latex=s'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s'" title="s'" /></a>. If our estimate <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Q}" title="\hat{Q}" /></a> is correct, we would expect the difference

<a href="https://www.codecogs.com/eqnedit.php?latex=r&plus;\gamma&space;\max_{a'}\hat{Q}(s',a')-\hat{Q}(s,a)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&plus;\gamma&space;\max_{a'}\hat{Q}(s',a')-\hat{Q}(s,a)" title="r+\gamma \max_{a'}\hat{Q}(s',a')-\hat{Q}(s,a)" /></a>

to be zero. If it is not zero, but slightly positive (negative), then the action and resulting reward can be viewed as 'evidence' that our estimate was too low (high).

The way this 'discrepancy' is handled is by simply adding this difference, weighted by a _learning factor_ <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>, to our previous estimate <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Q}_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Q}_n" title="\hat{Q}_n" /></a> to obtain a revised estimate <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Q}_{n&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Q}_{n&plus;1}" title="\hat{Q}_{n+1}" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{Q}_{n&plus;1}(s,a)&space;=&space;\hat{Q}_n(s,a)&space;&plus;&space;\alpha\left[&space;r&plus;\gamma&space;\max_{a'}\hat{Q}_n(s',a')-\hat{Q}_n(s,a)\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{Q}_{n&plus;1}(s,a)&space;=&space;\hat{Q}_n(s,a)&space;&plus;&space;\alpha\left[&space;r&plus;\gamma&space;\max_{a'}\hat{Q}_n(s',a')-\hat{Q}_n(s,a)\right&space;]" title="\hat{Q}_{n+1}(s,a) = \hat{Q}_n(s,a) + \alpha\left[ r+\gamma \max_{a'}\hat{Q}_n(s',a')-\hat{Q}_n(s,a)\right ]" /></a>

In this implementation of Q-learning for Tic Tac Toe, `Q` has the form of a dictionary, the keys of which are the states of the game (represented by the game's `Board` and the mark of player whose turn it is) and the values are again dictionaries containing the current estimate of the `Q` for each available move (i.e., empty square). Bellman's equation is implemented in the `learn_Q` method of the `Game` class, which is called on every move. 

The game's `Q` is shared with any instances of `QPlayer` playing the game, which uses it to make its move decisions. Following the implementation by Heisler [[q.py](https://gist.github.com/fheisler/430e70fa249ba30e707f), [slides](http://slides.com/fheisler/q-learning#/)], the `QPlayer` follows an "<a href="https://www.codecogs.com/eqnedit.php?latex=\epsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\epsilon" title="\epsilon" /></a>-greedy" policy, meaning that with probability <a href="https://www.codecogs.com/eqnedit.php?latex=\epsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\epsilon" title="\epsilon" /></a> it chooses a random move, and otherwise it follows the policy dictated by `Q` -- that is, if the player has mark "X" ("O"), choose the move with the highest (lowest) Q-value, in accordance with our 'sign convention'. During training, `epsilon` is set to a high value to encourage exploration, whereas for the actual match against a human, it is set to zero for optimal performance.

## Discussion
After 200,000 training games against itself with `epsilon=0.9`, the `QPlayer` seems practically unbeatable by a human player. It would be instructive, however, to check this by pitting it against a player following the [minimax](https://en.wikipedia.org/wiki/Minimax) algorithm for many games. It would also be interesting to check the finding by [Boyan (1992)](http://www.cs.cmu.edu/~jab/cv/pubs/boyan.backgammon-thesis.pdf) that a Q-learned player is able to beat the "T-hand" player 58% of the time and draw the remaining 42%.

