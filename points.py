def calculate_points(destroyed) -> int:
    points = 0
    for asteroid in destroyed:
        points += asteroid.points
    return points

def get_score(line) -> int:
    line_pieces = line.split(" ")
    return int(line_pieces[len(line_pieces)-1])

def update_scoring_board(destroyed):
    points = calculate_points(destroyed)
    print(f"You totalized {points} points")
    name = input("Enter your name: ")

    try:
        with open("Classifica.txt", "r") as file:
            classifica = file.read()
        classifica_lines = classifica.split("\n")
        placement = 0
        for line in classifica_lines:
            if points <= get_score(line):
                placement += 1
            else:
                break
        point_line = f"{name}: {points}"
        new_classifica_lines = classifica_lines[0:placement]
        new_classifica_lines.append(point_line)
        new_classifica_lines.extend(classifica_lines[placement:len(classifica_lines)])
        new_classifica = "\n".join(new_classifica_lines)
        with open("Classifica.txt", "w") as file:
            file.write(new_classifica)
    except:
        file = open("Classifica.txt", "w")
        file.write(f"{name}: {points}")