from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'STICK_MIND_SECRET_KEY'  # Required for session

@app.route("/")
def index():
    # Initialize game state
    session['total_sticks'] = 21
    session['current_turn'] = 'A'
    session['message'] = "START GAME - PLAYER A's TURN"
    session['game_over'] = False
    return render_template("game2.html", 
                         total=session['total_sticks'], 
                         message=session['message'],
                         turn=session['current_turn'],
                         game_over=session['game_over'])

@app.route("/play", methods=['POST'])
def play():
    if 'total_sticks' not in session:
        return redirect(url_for('index'))

    if session.get('game_over'):
        return redirect(url_for('index'))

    try:
        sticks_to_take = int(request.form["sticks"])
    except ValueError:
        session['message'] = "INVALID INPUT: Please enter a number."
        return render_template("game2.html", 
                             total=session['total_sticks'], 
                             message=session['message'],
                             turn=session['current_turn'],
                             game_over=session['game_over'])

    total = session['total_sticks']
    current_player = session['current_turn']

    # Validation
    if sticks_to_take < 1 or sticks_to_take > 4:
        session['message'] = f"INVALID MOVE: Player {current_player} must pick 1-4 sticks."
    elif sticks_to_take > total:
        session['message'] = f"INVALID MOVE: Only {total} sticks remaining."
    else:
        # Valid move
        total -= sticks_to_take
        session['total_sticks'] = total
        
        if total == 0:
            session['game_over'] = True
            # The player who took the last stick loses
            winner = 'B' if current_player == 'A' else 'A'
            session['message'] = f"GAME OVER! Player {current_player} took the last stick. Player {winner} WINS!"
        else:
            # Switch turn
            next_player = 'B' if current_player == 'A' else 'A'
            session['current_turn'] = next_player
            session['message'] = f"Player {next_player}'s Turn. Sticks remaining: {total}"

    return render_template("game2.html", 
                         total=session['total_sticks'], 
                         message=session['message'],
                         turn=session['current_turn'],
                         game_over=session['game_over'])

if __name__ =="__main__":
    app.run(host="localhost", port=777, debug=True)