import unittest

def mat_to_list(adj_mat):
    adj_list = []
    for _ in range(len(adj_mat)):
        adj_list.append([])
    
    for i in range(len(adj_mat)):
        for j in range(len(adj_mat)):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)
                
    return adj_list

class TestMat(unittest.TestCase):
    def test_basic(self):
        adj_matrix = [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]]
       
        expected = [[1, 3], [2], [0], [4], [5], []]
        self.assertEqual(mat_to_list(adj_matrix),expected)

    def test_noEdge(self):
        adj_matrix = [[0]]
        expected = [[]]
        self.assertEqual(mat_to_list(adj_matrix),expected)


    def test_selfLoop(self):
        adj_matrix = [[1]]
        expected = [[0]]
        self.assertEqual(mat_to_list(adj_matrix),expected)

if __name__ == '__main__':
    unittest.main()