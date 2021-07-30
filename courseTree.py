'''
Takes the course connection storage and sorts data into tree form for display on site.

Could just use the hashmap but this allows us to easily search the tree and store the data in a format that works
easier for us.
'''

import courseInfoStorage as CIS
import courseConnectionStorage as CCS

class node():
    '''
    Nodes for the trees. Ambiguous amount of nodes due to unknown amount of prereqs for any course
    '''
    def __init__(self, course, key):
        self.course = course
        self.courseKey = key
        self.nodes = []

    #Return a nodes course
    def getCourse(self):
        return self.course

    #After creating a new node. Add it to the prereq list for this current one
    def addNode(self, node):
        self.nodes

class coursesToTree():
    '''
    Turn the courses into a tree
    '''

    def __init__(self):


def main():



    return 0

if __name__ == '__main__':
    main()
