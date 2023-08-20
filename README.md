# TicTacToe
In this code, first i created a class called player. in this class i created multiple characteristics such as the name of the player (in this code 'X' or 'O') and a flag to determine if the player is playing or not.

 i then created methods that run the game. first, i created a method called "play". this method is what takes the input of the player and places the player's symbol ('X' or 'O') and places it in the list named "val" which has the 16 slots of the grid
 
 the method "computer" preforms the same as the method "play" but uses a random number generator instead of waiting for an input from the player.
 
 method check_Victory checks compares all the moves a player has made with all the possible win condition. if any win condition is reached then the player wins and the method returns TRUE
 check_Tie counts all the moves of both players. if their sum is equal 16 and no win has acurred then it is a tie.
 
 the function mytictactoe simply draws the current board using the list named val.

 created three objects. one for player1 player2 and computer 

 if the player wants to play against the compute the code that has the computer will run. otherwise the other code will run
