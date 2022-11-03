import pytest
from app import models


@pytest.fixture(scope="function")
def test_vote(test_posts, session, test_user):
    new_vote = models.Vote(post_id=test_posts[1].id, user_id=test_user['id'])
    session.add(new_vote)
    session.commit()


def test_add_vote_to_own_post(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json = {"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 201


def test_add_vote_to_other_user_post(authorized_client, test_posts):
    res = authorized_client.post("/vote/", json = {"post_id": test_posts[3].id, "dir": 1})
    assert res.status_code == 201


def test_add_vote_to_already_upvoted_own_post(authorized_client, test_posts, test_vote):
    res = authorized_client.post("/vote/", json = {"post_id": test_posts[1].id, "dir": 1})
    assert res.status_code == 409


def test_delete_vote_that_exists(authorized_client, test_posts, test_vote):
    res = authorized_client.post("/vote/", json = {"post_id": test_posts[1].id, "dir": 0})
    assert res.status_code == 201


def test_delete_vote_that_does_not_exists(authorized_client, test_posts, test_vote):
    res = authorized_client.post("/vote/", json = {"post_id": test_posts[2].id, "dir": 0})
    assert res.status_code == 404


def test_add_vote_to_post_that_does_not_exists(authorized_client):
    res = authorized_client.post("/vote/", json = {"post_id": 999999, "dir": 1})
    assert res.status_code == 404


def test_add_vote_unauthorized(client, test_posts):
    res = client.post("/vote/", json = {"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 401
