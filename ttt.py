import os

a = [[[1, 2], 3], [[3, 4], 3], [[5, 6], 3], [[7, 8], 3]]

x = [[1, 2] in route for route in a].count(True) > 0

print(os.listdir(os.getcwd()))