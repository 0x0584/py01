# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 22:13:50 by archid-           #+#    #+#              #
#    Updated: 2023/02/23 23:20:07 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe(object):
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        """intialises the recipe object"""
        if type(name) != str:
            raise TypeError("recie name should be an instance of `str'")
        if len(name) == 0:
            raise ValueError("recipe name should not be empty")
        self.name = name
        if type(cooking_lvl) != int:
            raise TypeError("cooking level should be an instance of `int'")
        if 1 > cooking_lvl or cooking_lvl > 5:
            raise ValueError( "cooking level should be in range of 1 to 5")
        self.cooking_lvl = cooking_lvl
        if type(cooking_time) != int:
            raise TypeError("cooking time should be an instance of `int'")
        if cooking_time == 0:
            raise ValueError("cooking time should be non zero")
        self.cooking_time = cooking_time
        if type(ingredients) != list: 
            raise TypeError("ingredients should be an instance of `list'")
        for e in ingredients:
            if type(e) != str:
                raise TypeError("an ingredient should be an instance of `str'")
        self.ingredients = ingredients
        if type(description) != str:
            raise "a description should be an instance of `str'"
        self.description = description
        if type(recipe_type) != str:
            raise TypeError("recipe type should be an instance of `str'")
        if not (recipe_type == 'starter' or recipe_type == 'lunch' \
            or recipe_type == 'dessert'):
            raise ValueError("recipe type should be either a starter dish, " \
                "a lunch or dessert")
        self.recipe_type = recipe_type
        
    def __str__(self):
        """Return the string to print with the recipe info"""
        return "recipe name: {}\nrecipe type: {}\n ingredients: {}\n" \
            "cooking time: {}\ncooking level: {}".format(
            self.name, self.recipe_type, self.ingredients, 
            self.cooking_time, self.cooking_lvl
        )
    
    