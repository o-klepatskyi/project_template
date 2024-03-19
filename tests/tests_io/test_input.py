from app.io.input import read_file, read_file_with_pandas
import pytest
import pandas as pd

def test_read_file_returns_file_content():
    filename = "data/test_file.txt"
    expected_content = "This is a test file."
    with open(filename, "w") as file:
        file.write(expected_content)
    assert read_file(filename) == expected_content

def test_read_file_returns_empty_string_for_empty_file():
    filename = "data/empty_file.txt"
    with open(filename, "w") as file:
        pass
    assert read_file(filename) == ""

def test_read_file_returns_none_for_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        filename = "data/nonexistent_file.txt"
        read_file(filename)

def test_read_file_with_pandas_returns_file_content():
    filename = "data/test_file.csv"
    content = "1,2,3\n4,5,6\n7,8,9"
    expected_content = " 1  2  3\n 4  5  6\n 7  8  9"
    with open(filename, "w") as file:
        file.write(content)
    print(expected_content)
    print(read_file_with_pandas(filename))
    assert read_file_with_pandas(filename) == expected_content

def test_read_file_with_pandas_returns_empty_string_for_empty_file():
    filename = "data/empty_file.csv"
    df = pd.DataFrame()
    df.to_csv(filename, index=False)
    with pytest.raises(pd.errors.EmptyDataError):
        read_file_with_pandas(filename)

def test_read_file_with_pandas_returns_none_for_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        filename = "data/nonexistent_file.csv"
        read_file_with_pandas(filename)
