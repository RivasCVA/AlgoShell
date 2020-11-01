import unittest
from solutions import *

class SalesPath(unittest.TestCase):
    class Node:
        def __init__(self, cost):
            self.cost = cost
            self.children = []
            self.parent = None
    
    def test_case_1(self):
        root = SalesPath.Node(0)    # Parent
        node_a = SalesPath.Node(5)
        node_b = SalesPath.Node(3)
        node_c = SalesPath.Node(6)
        node_d = SalesPath.Node(4)
        node_e = SalesPath.Node(2)
        node_f = SalesPath.Node(0)
        node_g = SalesPath.Node(1)
        node_h = SalesPath.Node(5)
        node_i = SalesPath.Node(1)
        node_j = SalesPath.Node(10)
        node_k = SalesPath.Node(1)

        root.children.append(node_a)
        root.children.append(node_b)
        root.children.append(node_c)

        node_a.parent = root
        node_a.children.append(node_d)

        node_b.parent = root
        node_b.children.append(node_e)
        node_b.children.append(node_f)

        node_c.parent = root
        node_c.children.append(node_g)
        node_c.children.append(node_h)

        node_d.parent = node_a

        node_e.parent = node_b
        node_e.children.append(node_i)

        node_f.parent = node_b
        node_f.children.append(node_j)

        node_g.parent = node_c

        node_h.parent = node_c

        node_i.parent = node_e
        node_i.children.append(node_k)

        node_j.parent = node_f

        node_k.parent = node_i

        expected = 7
        actual = get_cheapest_cost(root)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()