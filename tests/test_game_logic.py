from logic_utils import check_guess, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression test for the reported bug:
# secret = 98, guessing 100 then 99 must BOTH advise going lower.
# The original bug paired a too-high guess with a "Go HIGHER" message,
# so guessing 99 (still above 98) wrongly told the player to go higher.

def test_too_high_hint_says_go_lower():
    outcome, message = check_guess(99, 98)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_consecutive_high_guesses_give_consistent_hints():
    # Both 100 and 99 are above the secret 98; both should say "go lower".
    _, msg_100 = check_guess(100, 98)
    _, msg_99 = check_guess(99, 98)
    assert "LOWER" in msg_100.upper()
    assert "LOWER" in msg_99.upper()


# Regression test for the "dead submit button" bug:
# After a win, clicking "New Game" left status == "won", so the app's guard
# called st.stop() before ever processing a guess. Starting a new game must
# reset status back to "playing" (and clear per-game state).

def test_new_game_resets_status_to_playing_after_win():
    # Simulate the session state left behind by a completed (won) game.
    state = {"secret": 42, "attempts": 5, "status": "won", "history": [10, 42]}

    state.update(new_game_state(77))

    assert state["status"] == "playing"  # the bug: this stayed "won"
    assert state["secret"] == 77
    assert state["attempts"] == 0
    assert state["history"] == []
