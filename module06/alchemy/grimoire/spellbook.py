def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell if its ingredients are valid; reject it otherwise."""
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
