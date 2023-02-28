# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 18:28:07 by archid-           #+#    #+#              #
#    Updated: 2023/02/23 18:56:50 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator(object):
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        sum_ = 0
        for coef, word in zip(coefs, words):
            sum_ += coef * len(word)
        return sum_
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        _sum = 0
        for i, coef in enumerate(coefs):
            _sum += coef * len(words[i])
        return _sum

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.zip_evaluate(coefs, words))