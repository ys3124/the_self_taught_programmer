def f(s):
    """
    Returns the value.
    :param s: str.
    :return: float.
    """
    try:
        return float(s)
    except (ValueError, TypeError):
        return "Invalid argument."

print(f("a"))
print(f([0]))
print(f("0"))
print(f("2"))