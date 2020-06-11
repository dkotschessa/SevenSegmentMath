#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stolen from this guy -->

Created on Fri Jun 28 16:50:45 2019

@author: martandsingh
"""

import numpy as np
rows = 7
cols = 6

top_half, bottom_half_left, top_half_right, bottom_half_right, top, bottom = int(rows/2), rows - int(rows/2), int(rows/2), rows - int(rows/2), cols, cols

M = [[' ' for x in range(cols)] for x in range(rows)]

 
def get_array():
    return [[' ' for x in range(cols)] for x in range(rows)]

def show_top_left_half(M):
    for i in range(top_half):
        for j in range(1):
            M[i][j] = '*'
    

def show_bottom_left_half(M):
    for i in range(bottom_half_left, rows-1):
        for j in range(1):
            M[i][j] = '*'

def show_top_right_half(M):
    for i in range(top_half):
        for j in range(cols-1, cols):
            M[i][j] = '*'

def show_bottom_right_half(M):
     for i in range(bottom_half_left, rows-1):
        for j in range(cols-1, cols):
            M[i][j] = '*'

def show_top(M):
    for i in range(1):
        for j in range(cols):
            M[i][j] = '*'

def show_bottom(M):
    for i in range(1):
        for j in range(cols):
            M[rows-1][j] = '*'

def show_middle(M):
    for i in range(top_half, top_half+1):
        for j in range(cols):
            M[i][j] = "*"

def show_left_middle_dot(M):
    M[top_half][0] = "*"
    

def show_right_middle_dot(M):
    M[top_half][cols-1] = "*"

def print_number(val):
    M = get_array()
    if val == 1:
        show_top_right_half(M)
        show_bottom_right_half(M)
        show_right_middle_dot(M)
     
    elif val == 2:
        show_top(M)
        show_bottom(M)
        show_top_right_half(M)
        show_middle(M)
        show_bottom_left_half(M)
    elif val == 3:
        show_top(M)
        show_bottom(M)
        show_top_right_half(M)
        show_middle(M)
        show_bottom_right_half(M)
    elif val == 4:
        show_top_left_half(M)
        show_middle(M)
        show_top_right_half(M)
        show_bottom_right_half(M)
    elif val == 5:
        show_top(M)
        show_bottom(M)
        show_top_left_half(M)
        show_bottom_right_half(M)
        show_middle(M)
    elif val == 6:
        show_bottom(M)
        show_middle(M)
        show_top_left_half(M)
        show_bottom_left_half(M)
        show_bottom_right_half(M)
    elif val == 7:
        show_top(M)
        show_top_right_half(M)
        show_bottom_right_half(M)
        show_right_middle_dot(M)
    elif val == 8:
        show_top(M)
        show_middle(M)
        show_bottom(M)
        show_top_left_half(M)
        show_bottom_left_half(M)
        show_top_right_half(M)
        show_bottom_right_half(M)
    elif val == 9:
        show_top(M)
        show_middle(M)
        show_bottom(M)
        show_top_left_half(M)
        show_top_right_half(M)
        show_bottom_right_half(M)
    elif val == 0:
        show_top(M)
        show_bottom(M)
        show_top_left_half(M)
        show_bottom_left_half(M)
        show_top_right_half(M)
        show_bottom_right_half(M)
        show_left_middle_dot(M)
        show_right_middle_dot(M)   
    
    for i in range(rows):
        for j in range(cols):
            print(M[i][j], end=''*3)
        print('')

