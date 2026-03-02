# test_seasons.py
# Andrew

import pytest
from seasons import calc


def test_seasons():
    ''' Invalid date '''
    with pytest.raises(ValueError):
        calc("moose")
