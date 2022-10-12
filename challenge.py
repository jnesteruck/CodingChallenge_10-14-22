'''
Weekly Coding Challenge(s)
    
a)  Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
    Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked
    list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

b)  Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the start of the loop.
    DEFINITION:
    Circular linked list: A (corrupt) linked list in which a node's next pointer points to
    an earlier node, so as to make a loop in the linked list.
    EXAMPLE
    Input: A -> B -> C -> D -> E -> C [the same C as earlier]
    Output: C

'''
from LinkedList import LinkedList

def intersection(ll1: LinkedList, ll2: LinkedList):
    '''
    intersection

    Determines if two linked lists intersect or not. If they intersect,
    returns the intersecting node. If not, returns None.

    '''
    for k in ll1:
        for j in ll2:
            if k.next == None or j.next == None:
                break
            if k.next.value == j.next.value:
                return k
    return None

def loopDetection(ll: LinkedList):
    '''
    loopDetection

    Returns the node at the start of a circular linked list loop

    '''
    list_elements = []
    for node in ll:
        if node in list_elements:
            return node
        list_elements.append(node)
    return None