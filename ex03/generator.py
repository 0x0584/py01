# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 06:35:20 by archid-           #+#    #+#              #
#    Updated: 2023/04/01 12:38:00 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from numpy import unique
from numpy.random import shuffle

def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before
    it is yielded.
    '''

    for c in text:
        if not c.isprintable():
            return "ERROR"

    words = text.split(sep)
    if option == 'shuffle':
        shuffle(words)
    elif option == 'unique':
        words = list(unique(words))
    elif option == 'ordered':
        words = sorted(words)

    for word in words:
        yield word
        
if __name__ == '__main__':
    if len(argv) == 2:
        for word in generator(argv[1]):
            print(word)
    elif len(argv) == 3:
        for word in generator(argv[1], sep=argv[2]):
            print(word)
    elif len(argv) == 4:
        for word in generator(argv[1], sep=argv[2], option=argv[3]):
            print(word)