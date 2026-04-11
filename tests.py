import calculator as c
def tests():
    assert c.divide(0, 5) == "Division by zero is not allowed"
    assert c.add(2345, 2345) == 4690
    assert c.subtract(123456787654576543, 123456787654576543) == 0
    assert c.multiply(1, 0) == 0
    