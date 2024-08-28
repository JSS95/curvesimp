import numpy as np
import pytest

VERT = [[0, 0], [2, 2], [4, 2], [4, 4], [2, 1], [5, 1], [7, 2]]


@pytest.fixture
def vert():
    return np.array(VERT)
