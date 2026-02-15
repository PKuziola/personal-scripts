import logging
import random


def libertalia_setup():
    characters = list(range(1, 41))
    player_colours = ['black', 'blue', 'green', 'purple', 'red', 'white']
    reputation_track = list(range(7, 13))

    selected_characters_1 = draw_character(characters)
    selected_characters_2 = draw_character(characters)
    selected_characters_3 = draw_character(characters)

    final_reputation = draw_reputation(reputation_track, player_colours)

    logging.info('Selected characters for Voyage #1: %s', selected_characters_1)
    logging.info('Selected characters for Voyage #2: %s', selected_characters_2)
    logging.info('Selected characters for Voyage #3: %s', selected_characters_3)

    logging.info('Reputation track: %s', final_reputation)

    return selected_characters_1, selected_characters_2, selected_characters_3, final_reputation


def draw_character(list_of_characters):
    output_list = sorted(random.sample(list_of_characters, 6))

    for character in output_list:
        list_of_characters.remove(character)

    return output_list


def draw_reputation(reputation_track, player_colours):
    shuffled_colours = random.sample(player_colours, len(player_colours))
    output_dict = dict(zip(reputation_track, shuffled_colours))

    return output_dict



if __name__ == "__main__":
    libertalia_setup()