def ft_plot_area() -> None:
    """Calculate and display the area of a garden plot."""
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print("Plot area:", area)
