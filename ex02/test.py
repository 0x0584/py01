# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 02:02:58 by archid-           #+#    #+#              #
#    Updated: 2023/03/29 19:01:50 by archid-          ###   ########.fr        #
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
        assert str(v) == "[[1.0], [2.0], [3.0], [4.0]]"
        assert v.values == [[1.], [2.], [3.], [4.]]
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

    def test_is_column_vector():
        v = Vector([[1],[2],[3]])
        assert v.is_column_vector()
        assert Vector.is_column_vector(v)
    
    def test_is_row_vector():
        v = Vector([[1, 2, 3]])
        assert v.is_row_vector()
        assert Vector.is_row_vector()
    
    def test_dot_product():
        v = Vector([[1, 2, 3]])
        w = Vector([[2, 4, 8]])
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
        assert v.__add__(w) == u
        assert v.__radd__(w) == u
    
    def test_subtraction():
        v = Vector([[1, 2, 3]])
        w = Vector([[1, 2, 3]])
        u = Vector([[0, 0, 0]])
        assert v.__sub__(w) == u
        assert v.__rsub__(w) == u

    def test_multiplication():
        v = Vector([[1, 2, 3]])
        k = 3
        assert v.__mul__(k) == Vector([[3, 6, 9]])
        assert v.__rmul__(k) == Vector([[3, 6, 9]])
    
    def test_str():
        v = Vector([[1, 2, 3]])
        assert v.__str__() == "[[1.0, 2.0, 3.0]]"
    
    def test_repr():
        v = Vector([[1, 2, 3]])
        assert v.__repr__() == "[[1.0, 2.0, 3.0]]"

if __name__ == '__main__':
    VectorUnitTest.test_valid_ctor_column()
    VectorUnitTest.test_valid_ctor_row()
    VectorUnitTest.test_invalid_ctor()
    print('>>> All tests passed')    