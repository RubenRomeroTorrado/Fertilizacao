from project import classe_fertilidade_magnesio

def test_classe_fertilidade_magnesio():
    assert classe_fertilidade_magnesio(29) == "MB"
    assert classe_fertilidade_magnesio(0) == "MB"
    assert classe_fertilidade_magnesio(30) == "B"
    assert classe_fertilidade_magnesio(59) == "B"
    assert classe_fertilidade_magnesio(60) == "M"
    assert classe_fertilidade_magnesio(89) == "M"
    assert classe_fertilidade_magnesio(90) == "A"
    assert classe_fertilidade_magnesio(124) == "A"
    assert classe_fertilidade_magnesio(125) == "MA"
    assert classe_fertilidade_magnesio(200) == "MA"
