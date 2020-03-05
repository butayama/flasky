import app.input_angles as inan

def test_get_angle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "27.1")
    assert inan.get_angle("query") == "27.1"


def test_coronal_component(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "27.1")
    assert inan.coronal_component() == "27.1"


def test_sagittal_component(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "-8.2")
    assert inan.sagittal_component() == "-8.2"


def test_torsion(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "29.7")
    assert inan.torsion_component() == "29.7"


def test_get_angles(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "25.6")
    assert inan.get_angles() == {'C': '25.6', 'S': '25.6', 'T': '25.6'}




