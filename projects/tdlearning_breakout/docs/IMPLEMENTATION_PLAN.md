# Implementation Plan: Web-Based Atari Breakout with TD Learning

## 1. Project Overview
We will create a Python-based web application that allows users to play Atari Breakout in their browser, trains a Deep Q-Network (DQN) agent using Temporal Difference learning, and allows the user to watch the trained agent play.

**Technology Stack:**
*   **Backend:** Python (Flask + Flask-SocketIO)
*   **Frontend:** HTML5 + JavaScript (Socket.IO client)
*   **RL Environment:** Gymnasium (Atari Breakout)
*   **ML Framework:** PyTorch

## 2. Architecture

### A. Web Interface (The "Game")
To fulfill the requirement of playing in a webpage, we will not write the game physics from scratch (which would deviate from the standard RL benchmark). Instead, we will stream the **Gymnasium environment** to the browser.

*   **Server (Python):** Runs the game loop. Captures the rendered frame, encodes it (JPEG/Base64), and sends it to the client via WebSocket.
*   **Client (Browser):** Renders the image on an HTML `<canvas>`. Captures keyboard input (Left/Right) and sends actions back to the server via WebSocket.

### B. TD Learning Agent (DQN)
We will implement a standard Deep Q-Network.
*   **Model:** A Convolutional Neural Network (CNN) taking stacked game frames as input and outputting Q-values for actions (No-Op, Fire, Right, Left).
*   **Algorithm:** Q-learning with Experience Replay and Target Network.

## 3. Step-by-Step Implementation Plan

### Phase 1: Environment & Web Interaction
**Goal:** A playable Breakout game in the browser.
1.  **Setup:** Initialize `requirements.txt` (flask, flask-socketio, gymnasium, opencv-python, torch, shimmy, ale-py).
2.  **Game Wrapper:** Create a `GameSession` class in Python that manages a Gymnasium instance, handles stepping, and frame encoding.
3.  **Web Backend:** Create `app.py` with Flask-SocketIO.
    *   Event `connect`: Start a new game session.
    *   Event `input`: Receive user action (Left/Right).
    *   Loop: Continuously yield frames to the client.
4.  **Frontend:** Create `templates/index.html`.
    *   Display video stream.
    *   Capture arrow keys and emit socket events.

### Phase 2: RL Infrastructure
**Goal:** Build the agent that can learn.
1.  **Preprocessing:** Implement standard Atari wrappers (Grayscale, Resize 84x84, Frame Stacking).
2.  **Network:** Define the DQN architecture in `src/model.py`.
3.  **Agent:** Implement `DQNAgent` in `src/agent.py` with:
    *   `select_action(state)`: Epsilon-greedy.
    *   `optimize_model()`: The TD error minimization step.

### Phase 3: Training
**Goal:** Train the agent.
1.  **Training Script:** Create `train.py`.
    *   Initializes environment and agent.
    *   Runs the training loop (Interacts with env, stores in memory, updates model).
    *   Saves checkpoints (`breakout_dqn.pth`).

### Phase 4: Model Inference in Web
**Goal:** Watch the AI play.
1.  **Inference Mode:** Add a toggle in the Web UI: "User Play" vs "AI Play".
2.  **Backend Logic:**
    *   If "AI Play" is active, the backend ignores user input.
    *   Instead, it feeds the current state to the trained `DQNAgent`, gets the action, and steps the environment.

## 4. Verification
*   **Playability:** Can the user move the paddle via the browser?
*   **Learning:** Does the training script show decreasing loss and increasing average reward?
*   **Demo:** Can the AI control the paddle in the browser effectively?
