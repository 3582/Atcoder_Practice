#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
# acc s --skip-filename -- --guess-python-interpreter pypy
import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(0,20):
    print(random.sample(l,20)[i])