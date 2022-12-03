def better_than_average(class_points, your_points):
    new_array = sum(class_points) + your_points
    if new_array / (len(class_points) + 1) < your_points:
        return True
    else:
        return False