# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/28 21:22:54 by archid-           #+#    #+#              #
#    Updated: 2023/03/01 02:02:21 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter(object):
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Lannister(GotCharacter):
    """A class representing the Lannister family."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "A Lannister always pays back his debt!"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        if self.is_alive:
            self.is_alive = False

# if __name__ == '__main__':
#     foo = Lannister(first_name='0x0584', is_alive=True)
#     print(foo.__dict__)
#     foo.print_house_words()
#     print(foo.is_alive)
#     foo.die()
#     print(foo.is_alive)

    