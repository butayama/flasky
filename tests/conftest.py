import os
import sys
from app.file_handling import write_pickle
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@pytest.fixture(scope="session")
def pickle_test_env(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('src_dir')
    pickle_dir = a_dir.mkdir('pickle')
    a_file = pickle_dir.join('already_there.pkl')
    write_pickle(dic_angles, a_file)
    return a_dir


@pytest.fixture()
def dic_angles():
    return {"C": 27.1, "S": -8.2, "T": 29.7}


