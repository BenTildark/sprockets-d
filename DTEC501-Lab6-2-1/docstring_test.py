# Test function docstring


def test_docstring():
    """func prints 'docstring' x6"""
    count = 0
    for i in range(6):
        count += 1
        print("{}: docstring".format(count))


# test_docstring()
