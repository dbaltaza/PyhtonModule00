
def ft_count_harvest_iterative(i: int = 1) -> None:
    """Count down to harvest using iteration."""
    days = int(input("Days until harvest: "))
    while i < days + 1:
        print("Day", i)
        i = i + 1
    print("Harvest time!")
