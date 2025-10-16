

def test_project_todo(client, setup_session, rollback):
    # I cannot post the same project name twice
    response1 = client.post(f"/projects", json={"project_name": "string"}, headers=setup_session)
    response2 = client.post(f"/projects", json={"project_name": "string"}, headers=setup_session)

    assert response2.status_code == 406
