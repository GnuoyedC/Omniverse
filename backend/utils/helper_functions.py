def remove_special_characters_and_normalize(target_string:str) -> str:
    """
    just a basic utility function that removes special chars from a string.
    Args:
        target_string (str): string to sanitize.
    Returns:
        str: lowercase, normalized string.
    """
    return str.lower("".join([char for char in target_string if char.isalnum()]))

def uniquify_list(target_list: list) -> list:
    """
    returns a list with unique elements.
    Args:
        target_list (list): list to make unique.
    Returns:
        list: unique list.
    """
    return list(set(target_list))

def cleanse_extraneous_hyphens(target_str: str) -> str:
    """
    returns string without extraneous hyphens.
    Args:
        target_str (str): string to be cleansed.
    Returns:
        str: string without extraneous hyphens.
    """
    return target_str.strip("-")