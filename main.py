import csv
import subprocess
import os
import random
from get_score6 import *
from get_score20 import *
from get import get_best_score

def get_20_chromos(func):
    all = func
    return all


if __name__ == "__main__":
    ''''#make()
    length_1 = 0
    while length_1 != 470:
        length_1 = len_check('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv')
        start_layout()
        add_chromos6(gen_alg6(get_chromos()),mut_gen(get_chromos()))'''
    #ch = get_chromos()
    #add_chromos6(mut_gen(ch), gen_alg6(ch))
    #start_layout()
    scr = get_20_chromos(get_best_score())
    add_chromos20(gen_alg20(scr), mutation(scr), mut_gen_alg20(scr))
    start_layout()

