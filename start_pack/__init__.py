import pathlib
import os
from start_pack.app_operation import app_operation
from src.functions import get_top_n
from src.DataJson import DataJson
from src.ApiHh import ApiHh

api = ApiHh()
data_json = DataJson()

project_path = pathlib.Path(__file__).parent.parent
vacancy_path = pathlib.Path(project_path, 'src', 'vacancy.json')


