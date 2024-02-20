import start_pack
from src.ApiHh import ApiHh
api = ApiHh()
link_hh = 'https://api.hh.ru/vacancies'
link_error = 'https://api.hh.ru/vacanciess'

def test_get_vacancy():
    v = api.get_vacancy('разработчик', link_hh)
    assert len(v) == 100
    c = api.get_vacancy('разработчик', link_error)
    assert c == None
