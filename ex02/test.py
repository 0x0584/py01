# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 02:02:58 by archid-           #+#    #+#              #
#    Updated: 2023/04/01 12:29:06 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

class VectorUnitTest:
    def test_valid_ctor_column():
        v = Vector([[1], [2], [3]])
        assert str(v) == "[[1.0], [2.0], [3.0]]"
        assert v.values == [[1], [2], [3]]
        assert v.shape == Vector.COLUMN_SHAPE
        v = Vector(5)
        assert str(v) == "[[0.0], [1.0], [2.0], [3.0], [4.0]]"
        assert v.values == [[0.], [1.], [2.], [3.], [4.]]
        assert v.shape == Vector.COLUMN_SHAPE
        v = Vector((2, 5))
        assert str(v) == "[[2.0], [3.0], [4.0]]"
        assert v.values == [[2.0], [3.0], [4.0]]
        assert v.shape == Vector.COLUMN_SHAPE

    def test_valid_ctor_row():
        v = Vector([[1, 2, 3]])
        assert str(v) == "[[1.0, 2.0, 3.0]]"
        assert v.values == [[1, 2, 3]]
        assert v.shape == Vector.ROW_SHAPE

    def test_invalid_ctor():
        try:
            Vector([1, 2, 3])
            assert False
        except:
            assert True
        try:
            Vector((3,2))
            assert False
        except:
            assert True

    def test_is_column_shape():
        v = Vector([[1],[2],[3]])
        assert v.is_column_shape()
        assert not v.is_row_shape()

    def test_is_row_shape():
        v = Vector([[1, 2, 3]])
        assert v.is_row_shape()
        assert not v.is_column_shape()
    
    def test_dot_product():
        v = Vector([[1, 2, 3]])
        w = Vector([[2, 4, 8]])
        assert v.dot(w) == 34
        v = Vector([[1], [2], [3]])
        w = Vector([[2], [4], [8]])
        assert v.dot(w) == 34
    
    def test_transpose():
        v = Vector([[1, 2, 3]])
        w = Vector([[1], [2], [3]])
        assert v.T() == w
        assert w.T() == v
        
    def test_addition():
        v = Vector([[1, 2, 3]])
        w = Vector([[1, 2, 3]])
        u = Vector([[2, 4, 6]])
        assert v + w == u
        assert w + v == u
        v = Vector([[1], [2], [3]])
        w = Vector([[1], [2], [3]])
        u = Vector([[2], [4], [6]])
        assert v + w == u
        assert w + v == u
        # assert v.__radd__(w) == u
    
    def test_subtraction():
        v = Vector([[1, 2, 3]])
        w = Vector([[1, 2, 3]])
        u = Vector([[0, 0, 0]])
        assert v - w == u
        assert w - v == u * -1
        v = Vector([[1], [2], [3]])
        w = Vector([[1], [2], [3]])
        u = Vector([[0], [0], [0]])
        assert v - w == u
        assert w - v == u * -1
        # assert v.__rsub__(w) == u

    def test_multiplication():
        v = Vector([[1, 2, 3]])
        k = 3
        assert v * k == Vector([[3, 6, 9]])
        v = Vector([[1], [2], [3]])
        k = 3
        assert v * k == Vector([[3], [6], [9]])
        # assert v.__rmul__(k) == Vector([[3, 6, 9]])
    
    def test_valid_division():
        v = Vector([[1, 2, 6]])
        k = 2
        assert v / k == Vector([[0.5, 1, 3]])
    
    def test_invalid_division():
        try:
            Vector([[1, 2, 3]]) / 0
            assert False
        except:
            assert True
    
    def test_str():
        v = Vector([[1, 2, 3]])
        assert v.__str__() == "[[1.0, 2.0, 3.0]]"
    
    def test_repr():
        v = Vector([[1, 2, 3]])
        assert v.__repr__() == "[[1.0, 2.0, 3.0]]"

    def test_equal():
        v = Vector([[1, 2, 3]])
        u = Vector([[1, 2, 3]])
        assert v.__ne__(u)
        assert v.__eq__(u)

if __name__ == '__main__':
    VectorUnitTest.test_is_column_shape()
    VectorUnitTest.test_is_row_shape()
    VectorUnitTest.test_valid_ctor_column()
    VectorUnitTest.test_valid_ctor_row()
    VectorUnitTest.test_invalid_ctor()
    
    VectorUnitTest.test_addition()
    VectorUnitTest.test_subtraction()
    VectorUnitTest.test_multiplication()
    VectorUnitTest.test_valid_division()
    VectorUnitTest.test_invalid_division()
    
    VectorUnitTest.test_transpose()
    VectorUnitTest.test_dot_product()
    
    VectorUnitTest.test_str()
    VectorUnitTest.test_repr()
    
    print('>>> All tests passed')