# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/23 22:13:53 by archid-           #+#    #+#              #
#    Updated: 2023/02/28 20:53:11 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Recipe, Book

class RecipeUnitTest():
    def test_valid_ctor():
        Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'],
               'A warm meal high in protein', 'starter')

    def test_invalid_ctor():
        try:
            Recipe(1, '', 1.0, {}, (), [])
        except TypeError:
            assert True, "either combination with valid argument should fail for any argument"
    
    def test_invalid_recipe_type_throw_policy():
        try:
            Recipe.is_valid_recipe_type('')
        except ValueError:
            assert True, "by default it throws ValueError"
        except:
            assert False
        policy = Recipe.RecipeTypeThrowPolicy
        Recipe.RecipeTypeThrowPolicy = False
        try:
            assert Recipe.is_valid_recipe_type('') == False
        except:
            assert False
        Recipe.RecipeTypeThrowPolicy = policy

    def test_str():
        name = 'salad'
        recipe_type = 'starter'
        ingredients = ['tomato', 'spinach', 'sweet chili', 'beans',
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
                      'A warm meal high in protein', 'starter')

class BookUnitTest():
    def test_valid_ctor():
        name = 'Fruit Salad'
        recipe_type = 'dessert'
        ingredients = ['Apples', 'Pears', 'Peach', 'Strawberries', 'Sugar', 'Almande Oil']
        descr = "A dessert rich of vitamines"
        cooking_time = 10
        cooking_lvl = 1

        salad = Recipe(name, cooking_lvl, cooking_time, ingredients, descr, recipe_type)
        beacon = Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'],
                   'A warm meal high in protein', 'starter')
        recipes = {salad.recipe_type: [salad], beacon.recipe_type: [beacon]}
        Book("Beginner Recipes", recipes)

    def test_invalid_ctor():
        try:
            Book(1, {})
        except:
            assert True, "either combination with valid argument should fail for any argument"

    def get_cookbook_instance():
        return Book("Beginner Recipes", {
           'starter': [
                Recipe("Beacon and Eggs", 1, 15, ['beacon', 'eggs', 'butter', 'salt', 'peper'],
                       'A warm meal high in protein', 'starter'),
                Recipe('Tomato Salad', 1,  10, ['tomato', 'spinach', 'chili', 'beans',
                        'mushroms', 'salt', 'oil', 'peper'], 
                        "A starter dish, high viber & rich of vitamines", 'starter')
            ]})

    def get_empty_cookbook_instance():
        return Book("empty book", {})

    def test_get_recipe_by_empty_name():
        assert BookUnitTest.get_cookbook_instance().get_recipe_by_name('') is None
        assert BookUnitTest.get_empty_cookbook_instance().get_recipe_by_name('') is None

    def test_get_recipe_by_existing_name():
        assert BookUnitTest.get_cookbook_instance().get_recipe_by_name('Tomato Salad') is not None

    def test_get_recipe_by_inexisting_name():
        assert BookUnitTest.get_empty_cookbook_instance().get_recipe_by_name("Salad") is None

    def test_get_recipes_by_empty_types():
        assert BookUnitTest.get_cookbook_instance().get_recipes_by_types('') is None
        assert BookUnitTest.get_empty_cookbook_instance().get_recipes_by_types('') is None

    def test_get_recipes_by_existing_types():
        assert BookUnitTest.get_cookbook_instance().get_recipes_by_types('starter') is not None

    def test_get_recipes_by_inexisting_types():
        assert BookUnitTest.get_empty_cookbook_instance().get_recipes_by_types('') is None

    def test_add_existing_recipe():
        assert not BookUnitTest.get_cookbook_instance().add_recipe(RecipeUnitTest.get_sample_recipe())

    def test_add_inexisting_recipe():
        assert BookUnitTest.get_empty_cookbook_instance().add_recipe(RecipeUnitTest.get_sample_recipe())

if __name__ == '__main__':
    # Recipe Unit Testing
    RecipeUnitTest.test_valid_ctor()
    RecipeUnitTest.test_invalid_ctor()
    RecipeUnitTest.test_invalid_recipe_type_throw_policy()
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
    
    print(">>> All Test Passed")