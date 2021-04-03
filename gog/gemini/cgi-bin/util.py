#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
import global_var

def check_equal(seq1, seq2):
    """True if seqs are equal, no matter the order"""
    if len(seq1) != len(seq2):
        return False
    return sorted(seq1) == sorted(seq2)

def printD(*args):
    """Print if DEBUG is True"""
    if global_var.DEBUG is True:
        print(*args)

