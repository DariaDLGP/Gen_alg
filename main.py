import csv
import subprocess
import os
import random
from get_score6 import *
from get_score20 import *
from get import get_best_score
from sort import *

def get_20_chromos(func):
    all = func
    return all


if __name__ == "__main__":
    make_chromo(sort_by_square(parser('1.csv')), sort_by_height(parser('1.csv')))
    ch = get_chromos()
    add_chromos6(mut_gen(ch), gen_alg6(ch))
    start_layout()
    scr = get_20_chromos(get_best_score())
    add_chromos20(gen_alg_20(scr), mutation(scr), mut_gen_alg20(scr))
    start_layout()
    get_best_score()
    for i in range(120):
        scr = get_20_chromos(get_best_score())
        add_chromos20(gen_alg_20(scr), mutation(scr), mut_gen_alg20(scr))
        start_layout()
        get_best_score()

