# Pixel Lab

A minimal terminal ROM launcher for SNES games, built with Python and curses.

## Requirements

- Python 3
- RetroArch
- snes9x libretro core

On Debian/Ubuntu (aarch64):

```bash
sudo apt install retroarch libretro-snes9x -y
```

## Setup

1. Clone the repo
2. Drop your `.sfc`, `.smc`, or `.zip` ROM files into the `roms/` directory
3. Run:

```bash
python3 snes.py
```

## Controls

| Key | Action |
|-----|--------|
| ↑ / k | Move up |
| ↓ / j | Move down |
| Enter | Launch game |
| Q | Quit |

After a game exits, the launcher reopens automatically.
