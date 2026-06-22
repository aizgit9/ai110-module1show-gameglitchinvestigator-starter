#FIX: Refactored get_range_for_difficulty from app.py into logic_utils.py; replaced the NotImplementedError stub with the real implementation.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


# FIX: Refactored this function out of app.py into logic_utils.py (filled in
# the stub) so the guess-parsing logic is importable and unit-testable.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIX: Refactored this function out of app.py into logic_utils.py (filled in
# the stub) so the comparison logic is importable and unit-testable.
# FIX: Inverted-hint bug. The hint messages were swapped -- a too-high guess
# said "Go HIGHER" and a too-low guess said "Go LOWER". Corrected so "Too High"
# -> "Go LOWER" and "Too Low" -> "Go HIGHER". Also removed the dead
# `except TypeError` branch that only existed to handle a string-coerced secret.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


# FIX: Refactored this function out of app.py into logic_utils.py (filled in
# the stub) so the scoring logic is importable and unit-testable.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


# FIX: New helper added to fix the "dead submit button" bug. The New Game
# handler in app.py reset attempts/secret but never reset status, leaving it
# at "won"/"lost" so the guard's st.stop() killed every guess. Centralizing the
# reset here (including status -> "playing") guarantees the game is playable
# again and makes the fix unit-testable.
def new_game_state(secret: int):
    """
    Build the fresh session state for starting a new game.

    Returns a dict resetting attempts/status/history and seeding the new
    secret. Crucially, status is reset to "playing" so the game accepts
    guesses again after a previous win or loss.
    """
    return {
        "secret": secret,
        "attempts": 0,
        "status": "playing",
        "history": [],
    }
