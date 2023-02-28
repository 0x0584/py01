# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 22:13:53 by archid-           #+#    #+#              #
#    Updated: 2023/02/28 08:10:05 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Recipe, Book

class RecipeUnitTest():
    def test_valid_ctor():
        Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'], '')

    def test_invalid_ctor():
        try:
            recipe = Recipe(1, '', 1.0, {}, (), [])
        except TypeError:
            assert True, "either combination with valid argument should fail for any argument"
    
    def test_str():
        name = 'salad'
        recipe_type = 'starter'
        ingredients = ['tomato', 'spinach', 'chili', 'beans',
                        'mushroms', 'salt', 'oil', 'peper']
        descr = "A starter dish, high viber & rich of vitamines"
        cooking_time = 10
        cooking_lvl = 1
        
        pre_cond = Recipe(name, cooking_lvl, cooking_time, ingredients, descr, recipe_type)
        post_cond: str = "recipe name: {}\nrecipe type: {}\n ingredients: {}\n" \
                "cooking time: {}\ncooking level: {}".format(
                    name, recipe_type, ingredients, cooking_time, cooking_lvl)
        assert str(pre_cond) == post_cond, "recipe string formatting is incorrect"

    def get_sample_recipe():
        return Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'],
                      'A warm meal high in protein', 'Breakfast')

class BookUnitTest():
    def test_valid_ctor():
        name = 'salad'
        recipe_type = 'starter'
        ingredients = ['tomato', 'spinach', 'chili', 'beans',
                        'mushroms', 'salt', 'oil', 'peper']
        descr = "A starter dish, high viber & rich of vitamines"
        cooking_time = 10
        cooking_lvl = 1

        Book("Beginner Recipes", [
            Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'], ''),
            Recipe(name, cooking_lvl, cooking_time, ingredients, descr, recipe_type)
        ])

    def test_invalid_ctor():
        try:
            Book(1, [])
        except:
            assert True, "either combination with valid argument should fail for any argument"

    def get_cookbook_instance():
        return Book("Beginner Recipes", [
            Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'], 'A warm meal high in protein', 'Breakfast'),
            Recipe('Tomato Salad', 1,  10, ['tomato', 'spinach', 'chili', 'beans',
                    'mushroms', 'salt', 'oil', 'peper'], 
                    "A starter dish, high viber & rich of vitamines", 'starter')
        ])

    def get_empty_cookbook_instance():
        return Book("empty book", dict())

    def test_get_recipe_by_empty_name():
        assert BookUnitTest.get_cookbook_instance().get_recipe_by_name('') is None, 'this should not catch'
        assert BookUnitTest.get_empty_cookbook_instance().get_recipe_by_name('') is None, 'this should not catch'

    def test_get_recipe_by_existing_name():
        assert BookUnitTest.get_cookbook_instance().get_recipe_by_name('Salad') is not None, 'this should not catch'

    def test_get_recipe_by_inexisting_name():
        assert BookUnitTest.get_empty_cookbook_instance().get_recipe_by_name("Salad") is None, "empty book shall not have any recipies"

    def test_get_recipes_by_empty_types():
        assert BookUnitTest.get_cookbook_instance().get_recipes_by_types('') is None
        assert BookUnitTest.get_empty_cookbook_instance().get_recipes_by_types('') is None

    def test_get_recipes_by_existing_types():
        assert BookUnitTest.get_cookbook_instance().get_recipes_by_types('Breakfast') is not None, ''


    def test_get_recipes_by_inexisting_types():
        assert BookUnitTest.get_empty_cookbook_instance().get_recipes_by_types('') is not None, 'this shall not catch'

    def test_add_existing_recipe():
        assert not BookUnitTest.get_cookbook_instance().add_recipe(
            'Tomato Salad', RecipeUnitTest.get_sample_recipe()), "this shall not catch"

    def test_add_inexisting_recipe():
        assert BookUnitTest.get_empty_cookbook_instance().add_recipe(
            'Tomato Salad', RecipeUnitTest.get_sample_recipe()), "this shall not catch"

if __name__ == '__main__':
    # Recipe Unit Testing
    RecipeUnitTest.test_str()

    # Book Unit Testing
    BookUnitTest.test_valid_ctor()
    BookUnitTest.test_invalid_ctor()
    
    BookUnitTest.test_get_recipe_by_empty_name()
    BookUnitTest.test_get_recipe_by_existing_name()
    BookUnitTest.test_get_recipe_by_inexisting_name()
    
    BookUnitTest.test_get_recipes_by_empty_types()
    BookUnitTest.test_get_recipes_by_existing_types()
    BookUnitTest.test_get_recipes_by_inexisting_types()
    BookUnitTest.test_add_existing_recipe()
    BookUnitTest.test_add_inexisting_recipe()    