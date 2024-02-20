import start_pack
from src.Vacancy import Vacancy

vc = {
    'name': "gh",
    'apply_alternate_url': 'gh',
    'salary': {
        'from': 10000,
        'to': 20000
    },
    'snippet': {
        'requirement': 'что то',
        'responsibility': 'что то'
    }
}

v = Vacancy(vc)


def test_get_top_n():
    g, h = v.get_top_n(1, start_pack)
    assert len(g) == 0
    assert len(h) == 0


def test_get_filter_vacancy():
    g = v.get_filter_vacancy([''], [v])
    assert len(g) == 1

def test_str():
    assert type(v.__str__()) == str
