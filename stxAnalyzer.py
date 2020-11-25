from ppbtree import *
from print_color import print

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
        if(root.value == '■'): 
            return root

    # Return False otherwise
    return False 

# Grammar builder
def getProductionsFromGrammar():
    with open("semverCFG.txt", "r", encoding = "UTF-8") as cfg:
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

state = ""
while (state != "3"):

    print(
    """
    -------------------------------------

    *Semantic versioning 2.0.0 analyzer*

    (1) Evaluate single version
    (2) Evaluate multiple from file
    (3) Exit

    -------------------------------------

    """,
    color="cyan"
    )

    state = input("Choose an option: ")

    if state == "1":
        inputStr = input("\nInput version: ")
        root = cyk(inputStr)
        if root :
            print("\nThis is a valid semantic version\n", color='green')
            inputStr = input("Print derivation tree? (Y/N): ")
            if inputStr in ['Y', 'y', 'yes', 'Yes'] : print_tree(root)
        else :
            print("\nThis is a NOT valid semantic version\n", color='red')
    elif state == "2":
        fileName = input("\nType file name to read from: ")
        try:
            versions = open(fileName)
        except:
            print("\nFile not found\n", color='magenta')
        else:
            print("\nEvaluating versions...\n")
            for v in versions.read().splitlines():
                if len(v) > 0 :
                    root = cyk(v)
                    if (root) : 
                        print(v, tag='✓', tag_color='green', color='white')
                    else : 
                        print(v, tag='X', tag_color='red', color='white')
    elif state == "3":
        print("\nBye!\n", color='cyan')
    else:
        print("\nThis is not a valid option!\n", color='magenta')