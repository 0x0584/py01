# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/01 02:02:52 by archid-           #+#    #+#              #
#    Updated: 2023/04/01 12:27:39 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List

def apply_op(u, v, op):
    if type(v) != Vector or u.shape != v.shape:
        raise TypeError()
    elif u.is_row_shape():
        if len(u.values[0]) != len(v.values[0]):
            raise ValueError()
        return Vector([[op(p, q) for p, q in zip(u.values[0], v.values[0])]])
    else:
        assert u.is_column_shape()
        if len(u.values) != len(v.values):
            raise ValueError()
        return Vector([[op(p[0], q[0])] for p, q in zip(u.values, v.values)])

def is_row_vector(values):
    if type(values) != list or len(values) != 1 or type(values[0]) != list:
        return False
    for e in values[0]:
        if type(e) != float and type(e) != int:
            raise TypeError()
    return True

def is_column_vector(values):
    if type(values) != list:
        return False
    for e in values:
        if type(e) != list or len(e) != 1:
            return False
        if type(e[0]) != float and type(e[0]) != int:
            raise TypeError()
    return True

class Vector(object):
    ROW_SHAPE = (1, 0)
    COLUMN_SHAPE = (0, 1)
    
    def __init__(self, values):
        if type(values) == list:
            if is_row_vector(values):
                self.shape = Vector.ROW_SHAPE
                self.values = [[float(val) for val in values[0]]]
            elif is_column_vector(values):
                self.shape = Vector.COLUMN_SHAPE
                self.values = [[float(val[0])] for val in values]
            else:
                raise ValueError()
        else:
            if type(values) == int:
                if values == 0:
                    raise ValueError()
                l, r = 0, values
            elif type(values) == tuple:
                if values[0] >= values[1]:
                    raise ValueError()
                l, r = values[0], values[1]
            else:
                raise TypeError()
            self.shape = Vector.COLUMN_SHAPE
            self.values = [[float(i)] for i in range(l, r)]

    def is_column_shape(self):
        return is_column_vector(self.values)
    
    def is_row_shape(self):
        return is_row_vector(self.values)
    
    def dot(self, v):
        if type(v) != Vector or self.shape != v.shape:
            raise TypeError()
        elif self.is_row_shape():
            if len(self.values[0]) != len(v.values[0]):
                raise ValueError()
            return sum([u * v for u, v in zip(self.values[0], v.values[0])])
        else:
            assert self.is_column_shape()
            return sum([u[0] * v[0] for u, v in zip(self.values, v.values)])
    
    def T(self):
        if self.is_row_shape():
            return Vector([[val] for val in self.values[0]])
        else:
            assert self.is_column_shape()
            return Vector([[val[0] for val in self.values]])
    
    def __add__(self, v):
        return apply_op(self, v, lambda x, y: x + y)
    
    def __radd__(self, v):
        return v.__add__(self)
    
    def __sub__(self, v):
        return apply_op(self, v, lambda x, y: x - y)
    
    def __rsub__(self, v):
        return v.__sub__(self)
    
    def __mul__(self, e):
        if type(e) == int or type(e) == float:
            if self.is_row_shape():
                return Vector([[val * e for val in self.values[0]]])
            else:
                assert self.is_column_shape()
                return Vector([[val[0] * e] for val in self.values])
        else:
            raise TypeError()
        
    def __rmul__(self, v):
        return self.__mul__(v)
    
    def __truediv__(self, e):
        if not(type(e) == int or type(e) == float):
            raise TypeError()
        elif e == 0:
            raise ValueError()
        if self.is_row_shape():
            return Vector([[v / e for v in self.values[0]]])
        elif self.is_column_shape():
            return Vector([[v[0] / e] for v in self.values])
        else:
            assert False
    
    def __rtruediv__(self, e):
        return self.__truediv__(e)

    def __str__(self):
        return "{}".format(self.values)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if type(other) != Vector:
            return False
        else:
            return self.shape == other.shape and self.values == other.values
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    