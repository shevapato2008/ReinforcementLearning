from src.game_session import GameSession
try:
    game = GameSession()
    print("GameSession initialized successfully")
    frame = game._encode_frame()
    print(f"Encoded frame length: {len(frame)}")
    game.close()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
