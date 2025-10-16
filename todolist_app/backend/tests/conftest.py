import pytest
from ...database.connectivity import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..dependencies import get_db
from ..main import app
from fastapi.testclient import TestClient
import json

#TODO use sqlite lite as a fixture for testing
# https://www.youtube.com/watch?v=9gC3Ot0LoUQ
# https://www.reddit.com/r/learnpython/comments/vi5mpo/fastapisqlalchemypytest_database_row_not_updating/
#TODO use fixture for entire directory 
# https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

# https://www.reddit.com/r/learnpython/comments/1lu91as/pytest_when_not_to_use_its_fixtures/
# https://docs.pytest.org/en/6.2.x/fixture.html
### all of these are fixtures, something my tests need to be prepared for them to run

#TODO maybe break this down into more parts
# it could be setting up a user which could be for session and the creation of project is specific for this module
@pytest.fixture(scope="session")
def setup_session(client):
    response = client.post(f"/users", json={"email": "myuser2@example.com", "password": "string"})
    
    response = client.post(f"/token", data={"username": "myuser2@example.com", "password": "string"})
    token = json.loads(response.content)
    headers = {"Authorization": f"Bearer {token.get("access_token")}"}
    return headers

@pytest.fixture(scope='session')
def db_engine():
    """Creates a test database and yields a database engine"""
    SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///todolist_app/backend/tests/todo_app.db"

    engine = create_engine(
        SQLALCHEMY_TEST_DATABASE_URL,
        connect_args={
            'check_same_thread': False
        }
    )

    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope='session')
def db(db_engine):
    """Creates a connection to the test database and handles cleanup"""

    test_session = sessionmaker(bind=db_engine)
    db = test_session()

    yield db
    #TODO this rollback should happen at the end of every function...
    # I probably have to turn it into its own fixture
    db.rollback() 
    db.close()

@pytest.fixture(scope='function')
def rollback(db):
    db.rollback()


@pytest.fixture(scope='session')
def client(db):
    """
    Overrides the normal database access with test database,
    and yields a configured test client
    """
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c
