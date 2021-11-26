# noughts_and_crosses
Noughts and crosses in a GUI

The program runs a GUI in which games of noughts and crosses can be played.
The code was written for python (3.8.10), and tested in a Linux environment. The python module "tkinter" is required. (Tkinter is usually - but not always - included as part of the python language on most Linux distros. You can check whether this is installed by running the command "python -m tkinter" from a terminal.)

If the noughts_and_crosses.py module is made executable (e.g. with the terminal command "chmod +x noughts_and_crosses.py"), then it should be possible to launch the game by double-clicking this file and selecting the "run in terminal" option. Otherwise, running the command "python noughts_and_crosses.py" should work.

The game is relatively simple, and the in-game menus should be reasonably self-explanatory. It is possible to play a single player game against a computer opponent or for two human players to play against each other.

The pre-calculated_results.py file shows how the computer opponent's initial move was determined. The algorithm by which the computer chooses its moves is based on selecting the move that yields the highest probability of getting a favourable result. It is reasonably sound, but not perfect and the computer can be beaten. Currently, the computer always plays second (as noughts).
