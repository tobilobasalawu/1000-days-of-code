def points(games):
    points = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            points += 3
        elif int(i[0]) < int(i[2]):
            points += 0
        else:
            points += 1

    return points