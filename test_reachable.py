import unittest

def reachable(adj_list, start_node):
    stack = [start_node]
    visited = set()
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            
            for i in adj_list[node]:
                if i not in visited:
                    stack.append(i)
    
    return visited

class TestReachable(unittest.TestCase):
    def test_basic(self):
        adj_list = [[1,3],[2],[0],[4],[3],[]]
        start = 0
        expected = {0,1,2,3,4}
        self.assertEqual(reachable(adj_list,start),expected)

    def test_noEdge(self):
        adj_list = [[]]
        start = 0
        expected = {0}
        self.assertEqual(reachable(adj_list,start),expected)

    def test_selfLoop(self):
        adj_list = [[0]]
        start = 0
        expected = {0}
        self.assertEqual(reachable(adj_list,start),expected)

    def test_large(self):
        adj_list = [[1,3],[4],[1],[5],[3,6],[],[5]]
        start = 2
        expected = {1,2,3,4,5,6}
        self.assertEqual(reachable(adj_list,start),expected)

if __name__ == '__main__':
    unittest.main()