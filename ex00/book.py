# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 22:13:46 by archid-           #+#    #+#              #
#    Updated: 2023/02/28 08:01:02 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from time import monotonic
from typing import Dict
from recipe import Recipe

RecipeDict = Dict[str, Recipe]

class Book(object):
    def __init__(self, name: str, recipes_list: RecipeDict):
        self.name: str = name
        self.last_update: datetime = monotonic()
        self.creation_date: datetime = monotonic()
        self.recipes_list: RecipeDict = recipes_list
        
    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name \texttt{name} and returns the instance(s)"""
        for recipe in self.recipes_list.keys():
            if recipe.name.lower() == name.lower():
               return self.recipes_list[recipe]
        return None
        #return list(filter(lambda recipe_name: recipe_name.lower() == name.lower()), )
    
    def get_recipes_by_types(self, recipe_types):
        """Get all recipe names for a given \texttt{recipe_type}"""
        if type(recipe_types) == str:
            recipe_types = [recipe_types]
        elif type(recipe_types) != list or any([type(recipe_type) != str for recipe_type in recipe_types]):
            raise TypeError("recipe type should be a string")
        return dict((lambda recipes: 
            dict((k, recipe) for k, recipe in recipes.items() 
                if any([str.__eq__(recipe.recipe_type, recipe_type)
                        for recipe_type in recipe_types])))(self.recipes_list))
        #return filter(lambda key: key.lower() == recipe_type.lower(), recipes)
                
    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if self.recipes_list.get(str(recipe), None) is None:
            self.recipes_list[str(recipe)] = recipe
            self.last_update = monotonic()
            return True
        else:
            return False