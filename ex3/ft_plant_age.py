
def ft_plant_age() -> None:
    """Check if a plant is ready for harvest based on its age."""
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
