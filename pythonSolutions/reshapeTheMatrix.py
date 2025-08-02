"""Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""


class Solution(object):
    def count_columns(self, mat):
        return len(mat)

    def count_rows(self, mat):
        return len(mat[0])

    def count_total_inputs(self, mat):
        return len(mat) * len(mat[0])

    def create_empty_array(self, rows, columns):
        array = []
        for i in range(0, rows):
            inside_array = []
            for j in range(0, columns):
                inside_array.append(0)
            array.append(inside_array)
        return array

    def make_1d(self, mat, true_if_row):
        array_1d = []
        for row in mat:
            for value in row:
                if true_if_row:
                    array_1d.append(value)
                else:
                    array_1d.append([value])
        return array_1d

    def populate_empty(self, array_1d, empty_array):
        current = 0
        for i in range(0, len(empty_array)):
            for j in range(0, len(empty_array[i])):
                empty_array[i][j] = array_1d[current]
                current += 1
        return empty_array

    # actual solution here
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r == 1 and c == self.count_total_inputs(mat):
            return [self.make_1d(mat, True)]
        elif r == self.count_total_inputs(mat) and c == 1:
            return self.make_1d(mat, False)
        elif len(mat[0]) * len(mat) == r * c:
            return self.populate_empty(
                self.make_1d(mat, True), self.create_empty_array(r, c)
            )
        return mat
