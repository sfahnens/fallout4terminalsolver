# fallout4terminalsolver

Helps to hack terminals in the above-named game.
While novice-level terminals with four or five characters are quite easy to solve, the higher ones are rather inconvenient.

## Requirements

Just python (tested with python 3.5, maybe it also runs with python2).

## Usage

    python solver.py WORD[,LIKENESS] ...

## Example

0. find a terminal you want to hack
1. enter all words to get the initial guess

    ```
    python solver.py lance hatch spree lives books halls finds plays cared locks nests
    ```
    
2. the solver will tell you to try 'lives'
3. doing so in the game could yield a likeness of 1
4. rerun the solver with the new information

    ```
    python solver.py lance hatch spree lives,1 books halls finds plays cared locks nests
    ```
 
5. the solver will present another hint    
6. repeat until solved or (hopefully not) locked out
