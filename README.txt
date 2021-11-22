To run the program run
python3 game1.py [computer/human] [computer/human] [depth]
I reccomend a depth of 3 for this program

heuristic should be a list of lists
the number is a constant
letter is variable
sign is a sign
for example:
[["*",-3, "x" ], ['+',6,"y"] ]
In this case the heuristic will be
-3x + 6y where x and y are defined in the program.
[["-",3, "x" ], ['*',-6,"y"] ]
in this case th heuristic would be
3x * (-6y)
you can change the heuristic in game1.py in the main function
you can have as many sublists as you want in the same format

I wanted to make a suitable heuristic which could be easily mutable. In this case the current heuristic is checking the middle row/rows and summing the number of white vs black tiles. I multiply this by a factor of 0.015 as the max value would be -5 or 5 and this would result in a max 0.075 which would never be larger than 1 or -1 (either side winning). I also created other simple quick functions the heurisitic could do like checking a row or column. I created these (and will create some more) so that the genetic algorithm will be able to use it to make a better heuristic. 

Currently it is good to keep the centre of the board, and the middle pieces are vital to winning in connect 4 so that is why I made my heuristic this. I played around with the factor 0.015 and realised that this value is good, any higher/lower makes it easier to win against. The heuristic does not win that much but that is a good thing, lots of room for improvement
