def is_palindromic(value):
    """function checks if value passed is palindromic"""
    val = str(value).lower()
    if val == val[::-1]:  # Reverse order
        return True
    else:
        return False
