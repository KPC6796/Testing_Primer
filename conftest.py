import pytest

@pytest.fixture()
def set_up():
    print("\nConnection to DB established")
    print("\nImport the data from the tables")
    print("\nJoin the tables")
    yield
    print("\nClose the connection")