import pathlib
from src.DataJson import DataJson
dj = DataJson()

project_path = pathlib.Path(__file__).parent.parent
p = pathlib.Path(project_path, 'tests', 'gh.json')

def test_get_data():
    assert dj.get_data(p) == ''

def test_add_data():
    dj.add_data('', p)
    assert dj.get_data(p) == ''

def test_delete_data():
    dj.delete_data(p)
    assert dj.get_data(p) == ''
