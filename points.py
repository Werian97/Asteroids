def calculate_points(destroyed):
    points = 0
    for asteroid in destroyed:
        points += asteroid.points
    return points