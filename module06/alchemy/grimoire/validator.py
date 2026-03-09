def validate_ingredients(ingredients: str) -> str:

    ingredients_array = ["fire", "water", "earth", "air"]

    for i in ingredients.split():
        if i not in ingredients_array:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
