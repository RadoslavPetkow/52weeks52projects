# Super Mario Game

## Overview
This is a 2D Super Mario-inspired platformer game built using Python and the Pygame library. The game features multiple levels, platforms, and a menu system, along with player movement, collision detection, and scrolling backgrounds.

---

## Features
- **Player Movement**: Mario can move left, right, and jump.
- **Platform Collision**: Mario can stand on platforms and interact with them.
- **Scrolling Levels**: The game features large levels with camera scrolling.
- **Multiple Levels**: Players can select from different levels in the menu.
- **Start Menu**: Includes options to start the game and choose levels.

---

## Project Structure
```
/Super_mario
    /assets
        /backgrounds
            level1_bg.png
            level2_bg.png
        /platforms
            platform.png
        /sprites
            mario.png
    /levels
        __init__.py
        level_base.py
        level1.py
        level2.py
    game.py
    player.py
    main.py
```

### Key Files
- **`main.py`**: Entry point for the game. Handles the start menu and level selection.
- **`game.py`**: Manages the game loop and level switching.
- **`player.py`**: Defines the Player class and its behavior (movement, gravity, etc.).
- **`levels/level_base.py`**: Base class for all levels, including platform and background management.
- **`levels/level1.py` & `levels/level2.py`**: Specific configurations for Level 1 and Level 2.

---

## How to Run the Game
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd Super_mario
   ```

3. Install the required dependencies:
   ```bash
   pip install pygame
   ```

4. Run the game:
   ```bash
   python main.py
   ```

---

## Controls
- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Space**: Jump
- **Escape**: Return to the menu

---

## Future Enhancements
- Add enemies (e.g., Goombas, Koopas) with AI behavior.
- Implement power-ups (e.g., mushrooms, fire flowers).
- Add checkpoints and save progress.
- Include parallax scrolling for a better visual experience.
- Improve graphics and animations.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

---

## Acknowledgments
- Built using the [Pygame](https://www.pygame.org/) library.
- Inspired by Nintendo's Super Mario series.
