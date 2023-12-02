def decode_draw(encoded_draw):
    encoded_draw = encoded_draw.strip()

    values = encoded_draw.split(',')
    draw = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    if len(values) < 1 or len(values) > 3:
        raise ValueError("unable to parse draw {}".format(encoded_draw))

    for value in values:
        value = value.strip()
        split_value = value.split(' ')
        if len(split_value) != 2:
            raise ValueError("unable to parse draw {}".format(encoded_draw))

        if split_value[1] not in draw.keys():
            raise ValueError("unable to parse draw {}".format(encoded_draw))

        draw[split_value[1]] = int(split_value[0])

    return draw

def decode_game(line):
    split_line = line.split(":")
    if len(split_line) != 2:
        raise ValueError("unable to parse line {}".format(line))

    game_id = split_line[0]
    if not game_id.startswith("Game "):
        raise ValueError("unable to parse line {}".format(line))

    game_id = game_id.split(" ")
    if len(game_id) != 2:
        raise ValueError("unable to parse line {}".format(line))

    game_id = int(game_id[1])

    encoded_draws = split_line[1].split(";")
    if len(encoded_draws) < 1:
        raise ValueError("unable to parse line {}".format(line))

    draws = [decode_draw(d) for d in encoded_draws]

    return {
        'id': game_id,
        'draws': draws,
    }
