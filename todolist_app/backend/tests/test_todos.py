import pytest
import json

@pytest.fixture(scope="module")
def setup_module(client, setup_session):
    post_project_response = client.post(f"/projects", json={"project_name": "string"}, headers=setup_session)


def test_post_todo(client, setup_session, rollback):

    post_todo_response = client.post(f"/todos", 
                           json={"name": "string", "description": "string", "project_id": 1},
                           headers=setup_session
    )
    assert post_todo_response.status_code == 201
    
    post_second_todo_response = client.post(f"/todos", 
                           json={"name": "string", "description": "string", "project_id": 1},
                           headers=setup_session
    )
    assert post_second_todo_response.status_code == 201

    post_todo_response_no_project_1 = client.post(f"/todos", 
                           json={"name": "string", "description": "string"},
                           headers=setup_session
    )
    post_todo_response_no_project_2 = client.post(f"/todos", 
                           json={"name": "string", "description": "string"},
                           headers=setup_session
    )
    assert post_todo_response_no_project_2.status_code == 201

    post_todo_response_no_optional = client.post(f"/todos", 
                           json={"name": "string"},
                           headers=setup_session
    )
    assert post_todo_response_no_optional.status_code == 201



def test_post_todo_project(client, setup_session, rollback):
    post_todo_response_wrong_project_id = client.post(f"/todos", 
                           json={"name": "string", "description": "string", "project_id": 10},
                           headers=setup_session
    )
    assert post_todo_response_wrong_project_id.status_code == 406


def test_delete_todo(client, setup_session, rollback):
    client.post(f"/todos", 
                           json={"name": "string", "description": "string", "project_id": 1},
                           headers=setup_session
    )
    delete_todo_response = client.delete(f"/todos/1", 
                           headers=setup_session
    )
    print(delete_todo_response.content)
    assert delete_todo_response.status_code == 200