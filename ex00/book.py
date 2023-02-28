# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 22:13:46 by archid-           #+#    #+#              #
#    Updated: 2023/02/28 21:19:05 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import stdout
import datetime
from time import monotonic
from typing import Dict, List

from recipe import Recipe

RecipeDict = Dict[str, List[Recipe]]

class Book(object):
    def __init__(self, name: str, recipes_list: RecipeDict):
        self.name: str = name
        self.last_update: datetime = monotonic()
        self.creation_date: datetime = monotonic()
        for recipe_type in recipes_list.keys():
            if not Recipe.is_valid_recipe_type(recipe_type):
                raise RuntimeError()
        for key, recipes in recipes_list.items():
            if any([recipe.recipe_type != key for recipe in recipes]):
                raise TypeError("mismatched typing")        
        self.recipes_list: RecipeDict = recipes_list

    def get_recipe_by_name(self, name: str, stream=stdout):
        """Prints a recipe with the name \texttt{name} and returns the instance(s)"""
        if len(name) == 0:
            return None
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name.lower() == name.lower():
                    return recipe
        return None
        #return list(filter(lambda recipe_name: recipe_name.lower() == name.lower()), )

    def get_recipes_by_types(self, recipe_type: str):
        """Get all recipe names for a given \texttt{recipe_type}"""
        if len(recipe_type) == 0:
            return None
        if not Recipe.is_valid_recipe_type(recipe_type):
            raise RuntimeError()
        return self.recipes_list[recipe_type]

        #return filter(lambda key: key.lower() == recipe_type.lower(), recipes)

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if self.get_recipe_by_name(recipe.name) is not None:
            return False
        elif recipe.recipe_type in self.recipes_list.keys():
            self.recipes_list[recipe.recipe_type].append(recipe)
        else:
            self.recipes_list.setdefault(recipe.recipe_type, [recipe])
        self.last_update = monotonic()
        return True
