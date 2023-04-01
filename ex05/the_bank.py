# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 18:58:06 by archid-           #+#    #+#              #
#    Updated: 2023/04/01 14:10:02 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_account(acc):
    if len(acc.__dict__) % 2 == 0:
        raise AttributeError()
    if any([attr[0] == 'b' for attr in acc.__dict__]):
        raise AttributeError()
    if not any([attr[:3] == 'zip' for attr in acc.__dict__]):
        raise AttributeError()
    if not any([attr[:4] == 'addr' for attr in acc.__dict__]):
        raise AttributeError()
    if not hasattr(acc, 'name') or not hasattr(acc, 'id') or not hasattr(acc, 'value'):
        raise AttributeError()
    if not type(acc.name) != str:
        raise AttributeError()
    if type(acc.id) != int:
        raise AttributeError()
    if type(acc.value) != int and type(acc.value) != float:
        raise AttributeError()
    if not any([acc.name == acc.name for acc in acc.accounts]):
        raise ValueError()

class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
        check_account(self)
    
    def transfer(self, amount):
        self.value += amount
        
# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        assert type(new_account) == Account
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        
        check_account(origin)
        check_account(dest)
        if type(amount) != int or type(amount) != float:
            raise TypeError()
        if amount < 0 or origin.value < amount:
            raise ValueError()
        
        
        
        
        
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if
        """
