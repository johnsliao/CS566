# John Liao
# CS 566 - Extra Credit Assignment
# Problem #2
# jsmiao@bu.edu
# BU ID: U47-74-9883

"""
Problem statement:

A toy can make moves of 1, 2, or 3 inches. Write a dynamic programming algorithm
to print the total number of ways in which the toy can move a total of n inches. Assume
the order matters, that is, a move of 2, 1, 3 inches is different from 1, 2, 3.
"""


class Toy:

    def __init__(self):
        self.ways_to_move = [1, 2, 3]   # Move 1,2,3 inches
        self.max_distance = 12          # "n" inches
        self.how_many = 0               # How many different ways toy can move n inches

    def move(self, moved):

        if moved >= self.max_distance:
            self.how_many += 1
            return

        for m in self.ways_to_move:
            self.move(m+moved)

if __name__ == '__main__':
    toy = Toy()
    toy.move(0)                         # Start at 0 inches

    print toy.how_many
