def square(x):
    return x * x

class TestSquareSpecialCases:
    def test_square_positive_1(self):
        assert square(2) == 4
    def test_square_positive_2(self):
        assert square(-3) == 9

def test_square_positive_3():
    assert square(0) == 0

def test_square_positive_4():
    assert square(2) == 4

print("All unit tests passed!")