#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
class Node:
    def __init__(self, val):
        self.val = val
        self.nodes = []
        self.is_leaf = False
        

class Trie:
    def __init__(self):
        self.root = Node('')
        self.prefixed = False
        
    def add(self, root, word, idx):
        if idx == len(word):
            root.is_leaf = True
            return
        matches = 0
        for node in root.nodes:
            if node.val == word[idx]:
                self.add(node, word, idx + 1)
                return
        new_node = Node(word[idx])
        root.nodes.append(new_node)
        self.add(new_node, word, idx + 1)
    
    def _is_prefix(self, root, word, idx):
        if idx == len(word):
            self._flag = True
            return
        if root.is_leaf == True:
            self._flag = True
            return
        for node in root.nodes:
            if node.val == word[idx]:
                self._is_prefix(node, word, idx + 1)
                return

    def is_prefix(self, word):
        self._flag = False
        self._is_prefix(self.root, word, 0)
        return self._flag
        
    def show(self, root, w):
        if root.is_leaf:
            self.words.append(w)
        for node in root.nodes:
            self.show(node, w + node.val)
    
    def display(self):
        self.words = []
        self.show(self.root, '')
        return self.words
    
    def insert(self, word):
        self.add(self.root, word, 0)
        
def noPrefix(words):
    # Write your code here
    trie = Trie()
    for word in words:
        if trie.is_prefix(word):
            print('BAD SET', word, sep='\n')
            return
        trie.insert(word)
    # print(trie.display())
    print('GOOD SET')
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
