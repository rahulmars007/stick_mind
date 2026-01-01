import pytest
import sys
import os

# Add parent directory to path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stick_mind_using_flask import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.secret_key = 'TEST_KEY'
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index_initialization(client):
    """Test that the index route initializes the game correctly."""
    response = client.get('/')
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess['total_sticks'] == 21
        assert sess['current_turn'] == 'A'
        assert not sess['game_over']

def test_valid_move(client):
    """Test a valid move by Player A."""
    client.get('/') # Initialize
    response = client.post('/play', data={'sticks': '3'})
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess['total_sticks'] == 18 # 21 - 3
        assert sess['current_turn'] == 'B'

def test_invalid_input_non_integer(client):
    """Test that non-integer input is handled gracefully."""
    client.get('/')
    response = client.post('/play', data={'sticks': 'abc'})
    assert response.status_code == 200
    # Should stay on page, check for error message in session or response text would need parsing
    with client.session_transaction() as sess:
        assert sess['total_sticks'] == 21 # No change
        assert "INVALID INPUT" in sess['message']

def test_invalid_move_out_of_range(client):
    """Test picking too many sticks (e.g. 5)."""
    client.get('/')
    response = client.post('/play', data={'sticks': '5'})
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess['total_sticks'] == 21
        assert sess['current_turn'] == 'A' # Still A's turn
        assert "must pick 1-4" in sess['message']

def test_game_over(client):
    """Test the game over condition."""
    client.get('/')
    # Simulate a game where we get close to 1 stick
    with client.session_transaction() as sess:
        sess['total_sticks'] = 1
        sess['current_turn'] = 'A'
    
    # Player A takes the last stick
    response = client.post('/play', data={'sticks': '1'})
    
    with client.session_transaction() as sess:
        assert sess['total_sticks'] == 0
        assert sess['game_over'] == True
        assert "Player B WINS" in sess['message']
