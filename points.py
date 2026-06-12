def calculate_points(destroyed) -> int:
    points = 0
    for asteroid in destroyed:
        points += asteroid.points
    return points

def get_score(line) -> int:
    score = ""
    for character in line:
        if character in "0123456789":
            score += character
    return int(score) if score != "" else int("0")