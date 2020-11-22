from ppbtree import *

class Node:
    def __init__(self, value, left, right=None):
        self.value = value
        self.left = left
        self.right = right

# CYK algorithm with tree generation
def cyk(inputStr):

    # Variables
    length = len(inputStr)
    gen, ter = getProductionsFromGrammar()
    genLeft = [va[0] for va in gen] # Generator symbol
    genRight = [va[1] for va in gen] # Production pair

    # CYK matrix
    table = [[set() for i in range(length-j)] for j in range(length)]

    # Initialize matrix
    for i in range(length):
        for te in ter:
            if inputStr[i] == te[1]:
                table[0][i].add(Node(te[0], Node(te[1], None, None), None))

    # Dynamic programming algorithm
    for i in range(1, length): # Traverse rows
        for j in range(length - i): # Traverse columns
            for k in range(i): 
                comb = getCombinations(table[k][j], table[i-k-1][j+k+1]) # Create all possible combinations
                for c in comb:
                    if c in genRight: 
                        for e in range(len(genRight)):
                            if genRight[e] == c:
                                tmpL = table[k][j]
                                left = list({l for l in tmpL if l.value == c[0]})
                                tmpR = table[i-k-1][j+k+1]
                                right = list({r for r in tmpR if r.value == c[1]})
                                table[i][j].add(Node(genLeft[e], left[0], right[0])) # Add matching combination to cell

    # Return root node if S is in last cell
    for root in {s for s in table[len(inputStr)-1][0]}:
        if(root.value == 'S'): 
            print("\nThis is a valid arithmetic expression\n")
            return root

    # Return False otherwise
    print("\nThis is NOT a valid arithmetic expression\n")
    return False 

# Grammar builder
def getProductionsFromGrammar():
    with open("arithmeticCFG.txt") as cfg:
        prds = cfg.readlines()
        gen = []
        ter = []

        for prd in prds:
            left, right = prd.split(" -> ")
            right = right[:-1].split(" | ")
            # Iterate through multiple prds from one value
            for r in right:
                # Verify if prd results in terminal or generator
                if len(r) == 1:
                    ter.append([left, r])
                else:
                    gen.append([left, r])

        return gen, ter

# Combination builder
def getCombinations(first, second):
    res = set()
    if first == set() or second == set(): # Concatenation with empty set results in empty
        return set()
    for f in first:
        for s in second:
            res.add(f.value+s.value)
    return res

# MAIN #

print(
"""
-------------------------------------

*Arithmetic expression CFG analyzer*

Valid symbols:
  -> N , where N is a natural number
  -> Operators: + , - , * , / , ( , ) 

-------------------------------------
"""
)
inputStr = input("Input an arithmetic expression: ")
root = cyk(inputStr)
if root : print_tree(root)