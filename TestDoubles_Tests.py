# Example Unittest.mok
#
# Can call readFromFile
# readFromFile returns correct string
# readFromFile throws exception
#   when file does not exist.


from LineReader import readFromFile
from unittest.mock import MagicMock
import pytest

filename='file'


#def test_canCallReadFromFile():
#    FirstLine = readFromFile(filename)

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    FirstLine = readFromFile('abc')
    mock_open.assert_called_once_with('abc', "r")
    assert FirstLine == 'test line'

def test_throwExceptionIfFileDoesNotExist(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value = False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with pytest.raises(Exception):
        result = readFromFile('abc')
