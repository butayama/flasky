from os.path import join, exists
import app.file_handling as fh
from io import StringIO
import pytest


def test_verify_path(pickle_test_env):
    # is verify_path creating a directory if directory does not exist yet?
    assert not exists(join(pickle_test_env, 'not_yet_there'))
    fh.verify_path(join(pickle_test_env, 'not_yet_there'))
    assert exists(join(pickle_test_env, 'not_yet_there'))


def test_overwrite_file(pickle_test_env):
    # is verify_path returning a valid filename if filename doesn't exist?
    assert not exists(join(pickle_test_env, 'not_yet_there.pkl'))
    assert fh.overwrite_file(join(pickle_test_env, 'not_yet_there.pkl')) == \
           join(pickle_test_env, 'not_yet_there.pkl')


def test_overwrite_file_exists(pickle_test_env, monkeypatch):
    # is verify_path returning a valid filename if filename exists
    # and file should be overwritten?
    filename = 'pickle/already_there.pkl'
    assert exists(join(pickle_test_env, filename))
    monkeypatch.setattr('builtins.input', lambda overwrite: "y")
    assert fh.overwrite_file(join(pickle_test_env, filename)) == join(pickle_test_env, filename)


@pytest.mark.skip
def test_not_overwrite_file_exists(pickle_test_env, monkeypatch):
    # TODO Test wahrscheinlich unsinnig
    # is verify_path returning a valid new filename if filename exists
    # and should not be overwritten?
    pickle_dir = join(pickle_test_env, "pickle")
    filename = 'already_there.pkl'
    new_filename = 'new.pkl'
    assert exists(join(pickle_dir, filename))
    # monkeypatch.setattr('builtins.input', lambda overwrite: "n")
    # monkeypatch.setattr('builtins.input', lambda new_name: new_filename)
    assert fh.overwrite_file(join(pickle_dir, new_filename)) == join(pickle_dir, new_filename)


@pytest.mark.skip
def test_not_overwrite_file_exists_variant(pickle_test_env, monkeypatch):
    # TODO Test wahrscheinlich unsinnig
    # Variant using <from io import StringIO>
    # is verify_path returning a valid new filename if filename exists
    # and should not be overwritten?
    pickle_dir = join(pickle_test_env, "pickle")
    filename = 'already_there.pkl'
    new_filename = 'new.pkl'
    answer_n = StringIO('n\n')
    assert exists(join(pickle_dir, filename))
    monkeypatch.setattr('sys.stdin', answer_n)
    # monkeypatch.setattr('sys.stdin', new_filename)
    assert fh.overwrite_file(join(pickle_dir, new_filename)) == join(pickle_dir, new_filename)


@pytest.mark.xfail
def test_store_pickle_file(pickle_test_env, dic_angles, monkeypatch):
    # TODO Test wahrscheinlich unsinnig
    # is store_pickle_file creating a file?
    pickle_dir = join(pickle_test_env, "pickle")
    filename = 'already_there.pkl'
    new_filename = 'new.pkl'
    answer_n = StringIO('n\n')
    assert exists(join(pickle_dir, filename))
    fh.store_pickle_file(dic_angles, join(pickle_dir, filename))
    monkeypatch.setattr('sys.stdin', answer_n)
    monkeypatch.setattr('sys.stdin', new_filename)
    assert exists(join(pickle_dir, new_filename))
