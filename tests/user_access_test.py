
import logging

from app import db
from app.db.models import User, Song

def test_user_login(client):
    """Tests if login was successful"""
    with client:
        client.post('/login', data=dict(email='dhyey@test.com', password='dhyeytest'))
        res = client.get('/profile')
        assert res.status_code == 200
        assert b"About" in res.data

def test_user_registration(client):
    """Tests if registration was successful"""
    with client:
        res = client.post('/register', data=dict(email='dhyey@test.com', password='dhyeytest', confirm='dhyeytest'), follow_redirects=True)
        assert res.status_code == 200
        assert b"Congratulations, you are now a registered user!" in res.data


def test_dashboard_access(client):
    """Test if user is able to access dashboard"""
    with client:
        client.post('/login', data=dict(email='dhyey@test.com', password='dhyeytest'))
        res = client.get('/dashboard', follow_redirects=True)
        assert res.status_code == 200
        assert b"Welcome" in res.data

def test_deny_dashboard_access(client):
    """Test if access to dashboard was denied"""
    with client:
        res = client.get('/dashboard', follow_redirects=True)
        assert b"Please log in to access this page." in res.data
        assert res.status_code == 200

def test_deny_csv_upload(client):
    """Test if access to uploading csv was denied"""
    with client:
        res = client.get('/songs/upload', follow_redirects=True)
        assert b"Please log in to access this page." in res.data
        assert res.status_code == 200