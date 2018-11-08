## Crossword Solver

For this assignment, you will create a crossword-solver program. You will enter a word at the keyboard with some letters missing, and the program works out all the possible words that would fit with the known letters and spaces. So for instance if you had an incomplete word in a crossword and you knew the first letter was 'f', you did not know the second or third letters, but knew the fourth was an 's' and the fifth was 't'. i.e. you are trying to find all words that would fit with 'f??st' The solution would be
```
faust
feast
feist
first
foist
frost
```

There would be six words that fit.  In order to create this program, you will need to use a dictionary of words. This repo contains a file named [dictionary.txt](./dictionary.txt) that you should read in to your program to use for lookups. 

## Rough Sketch
1. We need to somehow input our incomplete word to let the program know what we are trying to solve.
2. We also need to be able to access a list of real words in a dictionary.
3. We will then have to compare our incomplete word with the words in the dictionary and determine if they are a potential match.
4. Finally we will need to print any words which match the criteria.
