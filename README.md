# CCG-GAME
Colors Choices Game Project Helpful Notes & Steps:
In this text lecture you will have guide for helping you to complete the project!
Sometimes this project can feel difficult, like being at the end of closed way so you will learn to how to find an open way to the solution.
So to help out with this, here is some notes to help you understand how to start coding and think in solution, and your solution may look completely different than the given solution that is right if it work properly.
If these notes below isn't fully helpful for you , check out the "Project Walkthrough" for more explanation and help.
So what is the project scope and What you need in this project to happen?
Notes:
1.We need to create choices for players and choices for computer then ask the players for inputs.
2.compare their inputs with the choice of the computer.
3.Check if the game is won,tied, lost, or ongoing.
4.Repeat thess steps until the game has been won or tied.
5.Ask if players want to play again.
6.and if the players agree restart the game again.
7.and if the player say "No" end the game and say thanks for the player.
Let's break those notes down into steps?
1.importing needed modules for our project.
2.Then we will define the main while loop and put the second while loop inside it.
3.declare colors choices as variables and specify colors of the game inside the nested while loop.
4.define the game roles by using the second while loop, If Statements and the random module’s randint function to get an integer between one and five.
5.then print the outputs of this big nested loop and the If statements inside this big while loop.
6.show the scores of computer and player after each player turn.
7.use the If statements to ask the player if he want to play again.
8.if the player choose "Yes" so restart the game.
9.if the player say "No" so end the game and say "thanks for playing".
Great job and remember, this is a milestone project, so its meant to be challenging so try to learn from it.
Other things that you may want to implement:¶
1. Taking in a player input:
how to take in a players input, you have to use input() You can use it as following:
player_choice = int(input("enter valid input: ")) you should make it int(input()) to avoid coding errors.
Then you would see a pop-up message occur with a text box asking you for your input.
then you will Type in the number and press enter.
Now the program will compare between computer choice and the player input.
2. Ensure of a player valid input:
in the project solution,the program remind a player to put in a correct and a valid input again from number one to number five (1,2,3,4,5) through a message in the start of the game .
