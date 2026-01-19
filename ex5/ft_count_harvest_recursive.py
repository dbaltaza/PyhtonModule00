
from typing import Optional


def ft_count_harvest_recursive(i: int = 1, days: Optional[int] = None) -> None:
    """Count down to harvest using recursion."""
    if days is None:
        days = int(input("Days until harvest: "))
    if i < days + 1:
        print("Day", i)
        ft_count_harvest_recursive(i + 1, days)
    elif i == days + 1:
        print("Harvest time!")
