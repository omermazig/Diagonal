import pytest
from diagonal import create_diagonals_array


@pytest.fixture()
def two_way_dict(request) -> dict:
    # Return your object here
    raise NotImplementedError


expected = {
    1: [[1]],
    4: [[1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1]],
    7: [[1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1]]
}


@pytest.mark.parametrize("size", [1, 4, 7])
def test_diagonals(size):
    assert create_diagonals_array(size) == expected[size]
