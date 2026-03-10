def validate_ingredients(ingredients: str) -> str:
    """Check that every word in ingredients is a known element."""
    ingredients_array: list[str] = ["fire", "water", "earth", "air"]

    for i in ingredients.split():
        if i not in ingredients_array:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
