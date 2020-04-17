#!/usr/bin/python
"""
Take 2 dictionaries, compare the values, or amounts and determine how many of each item you can make. The recipes contains what is required, the ingredients are what you have on hand.
"""

import math

def recipe_batches(recipe, ingredients):
  # Empty array to append any batches that can be made
  count = []

  if recipe.keys() == ingredients.keys():
  # print(recipe.keys())
    for i in ingredients:
    # print("Recipe", recipe[i], "Ing", ingredients[i])
      if ingredients[i] >= recipe[i]:
        count.append(ingredients[i] // recipe[i])
        return min(count)
      else:
        return 0
  else:
    return 0

# Should return 0, not enough milk.
recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 95, 'butter': 50, 'flour': 5 }

print(recipe_batches(recipe, ingredients))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))