# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository implements a web-based Atari Breakout game with Temporal Difference (TD) learning capabilities. The project allows users to play Breakout in a browser and trains a Deep Q-Network (DQN) agent using TD learning principles.

## Key Components

1. **Web Application**: Flask-based backend with SocketIO for real-time communication
2. **Game Environment**: Gymnasium Atari Breakout environment
3. **Frontend**: HTML5 Canvas with JavaScript for rendering game frames
4. **TD Learning**: Planned DQN implementation for agent training

## Repository Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation and setup instructions
├── IMPLEMENTATION_PLAN.md # Detailed implementation roadmap
├── check_envs.py         # Environment verification script
├── templates/
│   └── index.html        # Frontend interface
└── src/
    └── game_session.py   # Game session management
```

## Common Development Commands

### Environment Setup
```bash
conda create -n py311_rl python=3.11 -y
conda activate py311_rl
pip install -r requirements.txt
```

### Running the Application
```bash
python app.py
```
Then access `http://127.0.0.1:5000` in your browser.

### Verifying Environments
```bash
python check_envs.py
```

## Code Architecture

### Web Layer (app.py)
- Flask application with SocketIO integration
- Handles WebSocket connections for real-time frame streaming
- Manages game sessions for multiple clients
- Routes user input (keyboard arrows) to game actions

### Game Layer (src/game_session.py)
- Wraps the Gymnasium Breakout environment
- Handles game state management and frame encoding
- Maps keyboard inputs to Atari actions
- Encodes frames as Base64 JPEG for web transmission

### Frontend (templates/index.html)
- Canvas-based rendering of game frames
- Keyboard event capture for user input
- SocketIO client for real-time communication

## Implementation Roadmap

According to IMPLEMENTATION_PLAN.md, the project follows these phases:

1. **Phase 1**: Environment & Web Interaction (playable game in browser)
2. **Phase 2**: RL Infrastructure (DQN model and agent implementation)
3. **Phase 3**: Training (training script with experience replay)
4. **Phase 4**: Model Inference (AI play mode in web interface)

## Key Technical Details

- Uses `BreakoutNoFrameskip-v4` environment from Gymnasium
- Frame encoding via OpenCV for efficient web transmission
- Asynchronous event handling with eventlet
- Action mapping: ArrowLeft=2, ArrowRight=3, No-Op=1

## Dependencies

Core packages include:
- flask, flask-socketio (web framework)
- gymnasium[atari], ale-py (Atari environment)
- opencv-python (frame processing)
- torch (deep learning - planned for DQN)
- eventlet (async support)