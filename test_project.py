import pytest
from project import Tile, ready_input, user_input_word, is_valid, longest_words, generate_letters_tiles, generate_letters_random, calculate_word_score, highest_point_word, all_words_list


def test_ready_input():
    # Dom - I'll take care of this one
    pass


def test_user_input_word():
    # Dom - I'll take care of this one
    pass


def test_is_valid():
    assert is_valid("corn", "tnoarec") == True
    assert is_valid("cron", "tnoaecs") == False
    # Add more tests, especially corner cases


def test_longest_words():
   assert longest_words("act") == ["act", "cat"]
   assert longest_words("abcd") != [] and isinstance(longest_words("abcd"), list)
   assert longest_words("xyz") == "No valid word found."
   # Add more tests, especially corner cases


def test_generate_letters_random():
    assert len(generate_letters_random()) == 7 and isinstance(generate_letters_random(), str)
    assert generate_letters_random(0) == ""
    with pytest.raises(ValueError):
        generate_letters_random(-1)
    # Add more tests, especially other corner cases


def test_generate_letters_tiles():
    tile_a = Tile('a', 5, 2)
    tile_b = Tile('b', 20, 0)
    tile_c = Tile('c', 10, 3)
    tile_iterable = [tile_a]
    with pytest.raises(ValueError):
        generate_letters_tiles(tile_iterable)


def test_calculate_word_score():
    tile_a = Tile('a', 10, 10)
    tile_b = Tile('b', 10, 5)
    tile_iterable = [tile_a, tile_b]
    assert calculate_word_score("aaaaaa", tile_iterable) == 60
    assert calculate_word_score("cdccd", tile_iterable) == 0
    with pytest.raises(TypeError):
            calculate_word_score(123, tile_iterable) == 0


def test_highest_point_word():
    pass


def test_all_words_list():
    pass
