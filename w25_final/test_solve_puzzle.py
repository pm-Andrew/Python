# test_solve_puzzle.py


from game import solve_puzzle


def test_solve_puzzle():
    puzzle, answer = solve_puzzle()
    assert isinstance(puzzle, str)  # Ensures puzzle is a string
    assert isinstance(answer, (int, str))  # Ensures answer is valid type
