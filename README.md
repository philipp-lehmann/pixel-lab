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
git clone https://github.com/philipp-lehmann/pixel-lab.git ~/pixel-lab
```

### 2. Install RetroArch and the snes9x core

```bash
sudo apt install retroarch libretro-snes9x -y
```

### 3. Set the core path in `snes.py`

The `CORE` constant at the top of `snes.py` must point to the snes9x libretro core. The path differs by board:

| Board | Architecture | Core path |
|-------|-------------|-----------|
| Raspberry Pi 3 | aarch64 | `/usr/lib/aarch64-linux-gnu/libretro/snes9x_libretro.so` |
| Raspberry Pi Zero v1.3 | ARMv6 32-bit | `/usr/lib/arm-linux-gnueabihf/libretro/snes9x_libretro.so` |

If unsure, find it with:

```bash
find /usr -name "*snes*libretro*" 2>/dev/null
```

### 4. Add ROMs

```bash
scp roms/*.sfc user@<PI_IP>:~/pixel-lab/roms/
```

### 5. Run

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
