import unittest
from lowestCommonAncestor import Node, findLCA, findPath



class testLowestCommonAncestor(unittest.TestCase):

    def test_findLCA(self):
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.left.right = Node(5) 
        root.right.left = Node(6) 
        root.right.right = Node(7) 

        self.assertEqual((findLCA(root, 4, 5,)),2)
        self.assertEqual((findLCA(root, 4, 6,)),1)
        self.assertEqual((findLCA(root, 3, 4,)),1)
        self.assertEqual((findLCA(root, 2, 4,)),2)

    def test_findPath(self): 
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.left.right = Node(5) 
        root.right.left = Node(6) 
        root.right.right = Node(7)
        path = []

        self.assertEqual((findPath(root,path,1)),True)
        self.assertEqual((findPath(root.left,path,5)),True)
        self.assertEqual((findPath(root.right,path,6)),True)
        self.assertEqual((findPath(root,path,8)),False)

        