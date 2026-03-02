# test_add.py
# Andrew


from add import sum_numbers, random_player_name


def test_sum_numbers_positive():
    assert sum_numbers(2,2) == 4
    assert sum_numbers(2,10) == 12
    assert sum_numbers(0,0) == 0

def test_sum_numbers_negative():
    assert sum_numbers(-2,7) == 5
    assert sum_numbers(-1,-1) != 10

def test_random_player_name():
    assert random_player_name() in ['Uhhhh','Rudy','Aaron','George','Theodore','Tyler','Missy']
    assert random_player_name() != 'Trish'

