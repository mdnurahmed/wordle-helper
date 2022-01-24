# wordle-helper

This is a python script to help solving [wordle game](https://www.powerlanguage.co.uk/wordle/)

5-letter-word-finder.py finds all the 5 letter word from a text file "english3.txt" .

suggester.py suggests next possible word and keeps improving suggestion by processing feedbacks.

- A feedback is a 5 letter word consisting of R,G,Y.
  - R means the letter is not present .
  - Y means the letter is present but not at that position .
  - G means the letter is present and in that exact position.
