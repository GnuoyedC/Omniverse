def remove_special_characters_and_normalize(target_string:str) -> str:
    """
    just a basic utility function that removes special chars from a string.

    Args:
        target_string (str): string to sanitize.

    Returns:
        str: lowercase, normalized string.
    """
    return str.lower("".join([char for char in target_string if char.isalnum()]))