from project import classe_fertilidade_potassio

def test_classe_fertilidade_potassio():
    assert classe_fertilidade_potassio(24) == "MB"
    assert classe_fertilidade_potassio(0) == "MB"
    assert classe_fertilidade_potassio(25) == "B"
    assert classe_fertilidade_potassio(49) == "B"
    assert classe_fertilidade_potassio(50) == "M"
    assert classe_fertilidade_potassio(79) == "M"
    assert classe_fertilidade_potassio(80) == "A"
    assert classe_fertilidade_potassio(119) == "A"
    assert classe_fertilidade_potassio(120) == "MA"
    assert classe_fertilidade_potassio(149) == "MA"
    assert classe_fertilidade_potassio(150) == "E"
    assert classe_fertilidade_potassio(200) == "E"