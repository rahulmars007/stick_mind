# Stick Mind

"Stick Mind" (also known as the 21 Sticks Game) is a logic-based strategy game for two players. The objective is to force the opponent to pick the last stick from a pile of 21.

## Game Rules
- **Total Sticks**: 21
- **Players**: 2 (Turn-based)
- **Moves**: Each player picks 1 to 4 sticks per turn.
- **Losing Condition**: The player who picks the last stick LOSES!

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rahulmars007/stick_mind
   cd stick_mind
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

## How to Play

### 1. Pygame Edition (Recommended)
The best version! Features animations, sound, and a modern UI.
```bash
python stick_mind_pygame.py
```
- Use the **+ / -** buttons to select sticks (1-4).
- Click **Player A Pick** or **Player B Pick** to confirm.

### 2. Desktop GUI (Tkinter)
A clean, windowed application.
```bash
python stick_on_GUI.py
```
- Enter the number of sticks or use the buttons.

### 3. Web Application (Flask)
Play in your browser.
```bash
python stick_mind_using_flask.py
```
- Open [http://localhost:777](http://localhost:777) in your browser.

### 4. Command Line (CLI)
Classic text-based version.
```bash
python Stick_mind_on_command.py
```

## Screenshots

*(Add your screenshots here)*
