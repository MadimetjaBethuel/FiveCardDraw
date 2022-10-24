# FiveCardDraw

The application provide the following functionality:
● Simulate shuffling a standard deck of 52 cards.
● Deal a single hand of 5 cards to the player.
● Evaluate the player’s hand, informing them of the highest ranked poker hand that
matches their hand of 5 cards

The Hand ranks are as follows (https://www.wsop.com/poker-hands/):
1. Straight Flush
2. Four of a Kind
3. Full House
4. Flush
5. Straight
6. Three of a Kind
7. Two Pair
8. One Pair
9. High Cards


The game is developed in python and use flask.
This application uses flask api connecting with the front vue application which displays your cards and hand rank.

To run the game run:
  Pip install -r requirements.txt
  
  this will install all the requirements of the project.
  the project is developed on pyhton 3.10 (craete development env)
  
  After installation run the app.py file to start the server.
  in the terminal 
    run npm run dev to start the vue server
  
  the app should work from browser.
  
  to run the unit test on the game:
    run python -m unittest
    
 Note that requirements may different as this ws developed on mac.
  
  
