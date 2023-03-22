# Shamrocks-Seahaven-Solitaire

Shamrocks is a solitaire card game which is played by one person with a standard 52-card deck of cards. The rules and a tutorial video are available at:
http://worldofsolitaire.com/
Click on “Choose Game” at the top of the screen and click on “Shamrocks”.
The program allows the user to play a simplified version of Shamrocks, with the program managing the game.

Game Rules
1. Start: The game is played with one standard deck of 52 cards. The deck is shuffled and becomes the initial stock (pile of cards).
All fifty-two cards are then dealt from the stock to the tableau, left to right, starting in the upper left. The tableau is filled with three-card collections (aka pile). There are three rows with five columns with a fourth row having three columns.

Each collection has three cards except for the last (lower right) which has only one card. Working left-to-right from the top left corner deal three cards to each collection, left-to-right, in the first row and then working left-to-right fill up the remaining rows. The last card dealt is the collection with only one card. The order of the initial deal is important to match tests. All cards are visible, a.k.a. face up.
Kings are special during the deal to the collections. Within one collection a king cannot have a card that is not a king to its left. For example, K-3-2 is valid, but 3-K-2 is not. Similarly, K-K-3 is valid but K-3-K is not. Finally K-K-K is valid.
The game also has a foundation, which has four piles of cards with cards face up. The foundation starts out empty and is filled during play. Each foundation pile is in order and contains only one suit starting with the ace at the bottom and ending with the king on top. Only the top card of each foundation pile is visible. The foundation is placed above the tableau.

2. Goal: The game is won when the foundation is full, i.e. all cards are in the foundation.
3. Moves: A player can move one card at a time and only cards from the tableau can be moved. Foundation cards cannot be moved (except if one is “undo-ing” a move). A tableau card can be moved to one of two places:
• To the tableau:
o A card, the source card, can be moved to a collection if the collection has one or
two cards and if the rightmost card in the collection, the destination card, differs in rank by one from the source card (larger or smaller but not equal). Suits do not matter—they may be the same or different.
• To the foundation:

o A card, the source card, can be moved to a foundation, if the destination (top)
The initial layout from the worldofsolitaire.com site:
<img width="597" alt="Screenshot 2023-03-22 at 4 15 06 AM" src="https://user-images.githubusercontent.com/102822796/226840309-701c4a41-75c6-455e-a3e8-22861da4d8b4.png">
foundation card is the same suit and has a rank one lower than the source card. An ace can only move to an empty foundation pile; no other rank card may move to an empty foundation pile.
No other moves are permitted (except undo).
