# Pixel Lab

A minimal terminal ROM launcher for SNES games, built with Python and curses.

## Requirements

- Python 3
- RetroArch
- snes9x libretro core

## Setup

### 1. Install git and clone

```bash
sudo apt install git -y
git clone https://github.com/YOUR/repo.git ~/pixel-lab
```

### 2. Install RetroArch

```bash
sudo apt install retroarch -y
```

### 3. Find the SNES core path

```bash
find /usr -name "*snes*libretro*" 2>/dev/null
find /opt -name "*snes*libretro*" 2>/dev/null
```

### 4. Update the core path in `snes.py`

Set `CORE` at the top of `snes.py` to match the path found above.

> **Note:** The Raspberry Pi Zero v1.3 is ARMv6 32-bit — the core path will use `arm-linux-gnueabihf` instead of `aarch64-linux-gnu`.

### 5. Add ROMs

```bash
scp roms/*.sfc user@<ZERO_IP>:~/pixel-lab/roms/
```

### 6. Run

```bash
cd ~/pixel-lab
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
