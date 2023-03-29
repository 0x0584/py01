# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 02:02:52 by archid-           #+#    #+#              #
#    Updated: 2023/03/29 09:26:01 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List

VectorType = List[List[float]]

class Vector(object):
    ROW_SHAPE = (1, 0)
    COLUMN_SHAPE = (0, 1)
    
    def __init__(self, values):
        """either takes a list that represents a row or column vector, a value or a range or values"""
        if type(values) == list:
            if Vector.is_row_vector(values):
                self.shape = Vector.ROW_SHAPE
            elif Vector.is_column_vector(values):
                self.shape = Vector.COLUMN_SHAPE
            else:
                raise ValueError("values are neither row nor column vectors")
            self.values = values
        else:
            tmp = 0
            if type(values) == int:
                pass
            elif type(values) == tuple:
                if values[0] >= values[1]:
                    raise ValueError()
                tmp = values[0]
            else:
                raise TypeError()
            self.shape = Vector.COLUMN_SHAPE
            self.values = [[i] for i in range(tmp, values)]

    def is_row_vector(values: VectorType) -> bool:
        """returns false if misshaped, throws on type error"""
        if type(values) != list or len(values) != 1 or type(values[0]) != list:
            return False
        for e in values[0]:
            if type(e) != float:
                raise TypeError("Row vector should have floats")
        return True

    def is_column_vector(values: VectorType) -> bool:
        """returns false if misshaped, throws on type error"""
        if type(values) != list:
            return False
        for e in values:
            if type(e) != list or len(e) != 1:
                return False
            if type(e[0]) != float:
                raise TypeError("Column vector has invalid typing")
        return True
    
    def is_column_vector(self) -> bool:
        return Vector.is_column_vector(self.values)
    
    def is_row_vector(self) -> bool:
        return Vector.is_row_vector(self.values)
    
    def dot(self, v: VectorType) -> float:
        assert self.shape == v.shape
        prod = 0
        for i, val in enumerate(v.values):
            if Vector.is_row_vector(self.shape):
                prod += self.values[0][i] * v.values[0][i]
            else:
                prod += self.values[i] * v.values[i]
        return prod
    
    def T(self) -> VectorType:
        if self.is_row_vector(self.values):
            self.shape = Vector.COLUMN_SHAPE
            self.values = [[val] for val in self.values[0]]
        elif self.is_column_vector(self.values):
            self.shape = Vector.ROW_SHAPE
            self.values = [[val[0] for val in self.values]]
        else:
            assert False
    
    def apply_linear_operation(self, v: VectorType, op) -> VectorType:
        if self.shape != v.shape:
            raise TypeError("misshaped")
        elif self.is_row_vector(self.values):
            if len(self.values[0]) != len(v.values[0]):
                raise TypeError("misshaped")
            return Vector([[
                op(self.values[0][i], v.values[0][i]) for i in range(v.values[0])
            ]])
        elif self.is_column_vector(self.values):
            if len(self.values) != len(v.values):
                raise TypeError("misshaped")
            return Vector([
                [op(self.values[i][0], v.values[i][0])] for i in range(v.values[0])
            ])
        else:
            assert False
    
    def __add__(self, v: VectorType) -> VectorType:
        return self.apply_linear_operation(v, lambda x, y: x + y)
    
    def __radd__(self, v) -> VectorType:
        return self.__add__(v)
    
    def __sub__(self, v: VectorType) -> VectorType:
        return self.apply_linear_operation(v, lambda x, y: x - y)
    
    def __rsub__(self, v: VectorType) -> VectorType:
        return self.__sub__(v)
    
    def __mul__(self, e) -> VectorType:
        if type(e) == int or type(e) == float:
            return [self.values[i] * e for i in range(self.values)]
        elif type(e) == VectorType:
            if self.is_row_vector():
                return sum([u * v for u, v in zip(self.values[0])])
            elif self.is_column_vector():
                return sum([u[0] * v[0] for u, v in zip(self.values)])
        else:
            assert False
        
    def __rmul__(self, e) -> VectorType:
        return self.__mul__(e)
    
    def __truediv__(self, e) -> VectorType:
        if not(type(e) == int or type(e) == float):
            raise TypeError("only scalars")
        if self.is_row_vector():
            return Vector([[v / e for v in self.values[0]]])
        elif self.is_column_vector():
            return Vector([[v[0] / e] for v in self.values])
        else:
            assert False
            
    def __str__(self) -> str:
        return "{}".format(self.values)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    