import gymnasium as gym
import ale_py
import cv2
import base64

class GameSession:
    def __init__(self, env_id='BreakoutNoFrameskip-v4'):
        self.env = gym.make(env_id, render_mode='rgb_array')
        self.action_map = {
            'ArrowLeft': 3,
            'ArrowRight': 2,
        }
        self.noop_action = 0
        self.fire_action = 1
        self.current_action = self.noop_action
        self.is_done = False
        self.reset()

    def reset(self):
        self.state, _ = self.env.reset()
        # Fire once to start the game
        self.env.step(self.fire_action)
        self.current_action = self.noop_action
        self.is_done = False

    def advance(self):
        if not self.is_done:
            self.state, _, terminated, truncated, _ = self.env.step(self.current_action)
            self.is_done = terminated or truncated
        return self._encode_frame(), self.is_done

    def set_action(self, action_key):
        self.current_action = self.action_map.get(action_key, self.noop_action)

    def _encode_frame(self):
        frame = self.env.render()
        _, buffer = cv2.imencode('.jpg', frame)
        return base64.b64encode(buffer).decode('utf-8')

    def close(self):
        self.env.close()
