#!/usr/bin/python3

initial_table = [
    64,17,15,33,15,83,41,70,98,50,90,17,85,94,36,73,41,89,82,37,44,52,80,66,
    19,61,86,55,21,49,53,53,55,80,26,95,25,40,74,32,85,50,96,75,81,75,61,13,
    14,18,74,93,13,7,84,
]

class FeSeisenNoKeifuRandom():
    def __init__(self):
        self.seed = initial_table
        self.rands = self.seed[:]

    def pop(self):
        if len(self.rands):
            return self.rands.pop(0)
        self.update_table()
        return self.rands.pop(0)

    def update_table(self):
        self.new_numbers(48, 17, 7)
        self.new_numbers(24, 48, 7)
        self.new_numbers(31, 0, 17)
        self.new_numbers(0, 24, 24)
        self.new_numbers(0, 48, 7, pattern="B")
        self.rands = self.seed[:]

    def new_numbers(self, a, b, n, pattern="A"):
        if pattern == "A":
            func = self.new_number
        else:
            func = self.new_numberB
        for i in range(n):
            self.seed[i+b] = func(self.seed[i+a], self.seed[i+b])

    def new_number(self, a, b):
        return (b-a)%100

    def new_numberB(self, a, b):
        return (a+b)%100

if __name__ == "__main__":
    fe = FeSeisenNoKeifuRandom()
    for i in range(300):
        print(fe.pop())
