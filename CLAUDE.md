# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running

```bash
python3 snes.py
```

Requires RetroArch and the snes9x libretro core on the host system. On Debian/Ubuntu aarch64:

```bash
sudo apt install retroarch libretro-snes9x -y
```

## Architecture

Single-file Python app (`snes.py`) — no build step, no external Python dependencies.

- `ROMS_DIR` — hardcoded to `roms/` relative to the script; place `.sfc`/`.smc`/`.zip` files there
- `CORE` — hardcoded aarch64 Linux path to the snes9x libretro core
- `get_roms()` → `draw()` → event loop → `launch()` is the full data flow
- After a game exits, the picker reopens via `curses.wrapper(main)` recursion

The curses UI uses three color pairs: 1=yellow accent (title/footer), 2=white highlight (selected row), 3=normal text.
