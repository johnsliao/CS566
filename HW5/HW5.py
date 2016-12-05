# John Liao
# CS 566, HW 5
# Email: jsmiao@bu.edu
# BU ID: U47-74-9883

import random

class Knapsack:

    def __init__(self):
        self.sack = []

        self.v = random.sample(range(0,15), 5)      # Values
        self.wt = random.sample(range(1,15), 5)     # Weights // For simplicity, assume all weights > 0
        self.n = len(self.v)                        # Number of distinct items
        self.W = 20                                 # Knapsack capacity

    def print_defaults(self):
        print 'INPUTS'
        print 'Values:', self.v
        print 'Weights:', self.wt
        print 'Number of distinct items:', self.n
        print 'Knapsack capacity:', self.W
        print '-'*50

    # 0-1 Knapsack - Top down approach
    # NOT Memoization -- Known values are not stored
    def zero_one_knapsack(self, W, wt, v, n):
        if n == 0 or W == 0:
            return 0

        if (wt[n - 1] > W):
            return self.zero_one_knapsack(W, wt, v, n - 1)
        else:
            return max(v[n - 1] + self.zero_one_knapsack(W - wt[n - 1], wt, v, n - 1),
                       self.zero_one_knapsack(W, wt, v, n - 1))

    # Unbounded Knapsack - Top down approach
    # zero_one_knapsack can NOT solve unbounded_knapsack because zero_one_knapsack only considers
    # an item to be taken either 0 or 1 time -- not more than 1.
    # NOT Memoization -- Known values are not stored
    def unbounded_knapsack(self, remaining_weight):
        sol = [0] * self.n
        my_sol = [0] * self.n

        if remaining_weight == 0:
            return 0

        for i in range(0,self.n):
            if remaining_weight >= self.wt[i]:
                sol[i] = self.unbounded_knapsack(remaining_weight-self.wt[i])
            else:
                return 0

        for i in range(0, self.n):
            if remaining_weight >= self.wt[i]:
                my_sol[i] = sol[i] + self.v[i]
            else:
                my_sol[i] = 0

        final_sol = my_sol[0]

        for i in range(1,self.n):
            if my_sol[i] > final_sol:
                final_sol = my_sol[i]

        return final_sol



if __name__ == '__main__':
    knapsack = Knapsack()
    knapsack.print_defaults()

    print 'OUTPUTS'
    print '0-1 Knapsack output:', knapsack.zero_one_knapsack(knapsack.W,
                                                             knapsack.wt,
                                                             knapsack.v,
                                                             knapsack.n)

    print 'Unbounded Knapsack output:', knapsack.unbounded_knapsack(knapsack.W)


