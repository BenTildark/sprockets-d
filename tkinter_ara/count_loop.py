from retrying import retry


@retry
def count_to_ten():

    """count to ten if you can"""

    for i in range(1, 11):
        print(i)
        if i == 7:
            raise Exception

# count_to_ten()
