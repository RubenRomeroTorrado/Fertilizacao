from final import azoto_deduzido_cultura_anterior

def test_azoto_deduzido_cultura_anterior():
    assert azoto_deduzido_cultura_anterior('1') == -20
    assert azoto_deduzido_cultura_anterior('2') == 20
    assert azoto_deduzido_cultura_anterior('3') == -20
    assert azoto_deduzido_cultura_anterior('4') == -20
    assert azoto_deduzido_cultura_anterior('5') == -40
    assert azoto_deduzido_cultura_anterior('6') == 0
    assert azoto_deduzido_cultura_anterior('7') == 0
    assert azoto_deduzido_cultura_anterior('banana') == 0
