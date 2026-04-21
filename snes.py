#!/usr/bin/env python3
"""
Pixel Lab — SNES Launcher
Pick a ROM with arrow keys, launch with Enter.
"""

import curses
import subprocess
import os
import sys

ROMS_DIR = os.path.join(os.path.dirname(__file__), "snes")
CORE = "/usr/lib/aarch64-linux-gnu/libretro/snes9x_libretro.so"
EXTENSIONS = (".sfc", ".smc", ".zip")


def get_roms():
    if not os.path.isdir(ROMS_DIR):
        return []
    files = [
        f for f in sorted(os.listdir(ROMS_DIR))
        if f.lower().endswith(EXTENSIONS)
    ]
    return files


def draw(stdscr, roms, selected):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Title
    title = "▓ PIXEL LAB — SNES LAUNCHER ▓"
    stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(1, max(0, (w - len(title)) // 2), title[:w])
    stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)

    # Divider
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(2, 0, "─" * (w - 1))
    stdscr.attroff(curses.color_pair(3))

    # ROM list
    list_start = 4
    for i, rom in enumerate(roms):
        y = list_start + i
        if y >= h - 3:
            break
        name = os.path.splitext(rom)[0]  # strip extension
        label = f"  {name}"
        if i == selected:
            stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
            stdscr.addstr(y, 0, label[:w - 1].ljust(w - 1))
            stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)
        else:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, 0, label[:w - 1])
            stdscr.attroff(curses.color_pair(3))

    # Footer
    footer = " ↑↓ Navigate   Enter Launch   Q Quit "
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(h - 2, max(0, (w - len(footer)) // 2), footer[:w])
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()


def launch(rom):
    path = os.path.join(ROMS_DIR, rom)
    subprocess.run(["retroarch", "--fullscreen", "-L", CORE, path])


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    # Colors: 1=accent, 2=selected, 3=normal
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, -1)

    roms = get_roms()

    if not roms:
        stdscr.addstr(0, 0, f"No ROMs found in {ROMS_DIR}")
        stdscr.addstr(1, 0, "Press any key to exit.")
        stdscr.getch()
        return

    selected = 0

    while True:
        draw(stdscr, roms, selected)
        key = stdscr.getch()

        if key in (curses.KEY_UP, ord('k')) and selected > 0:
            selected -= 1
        elif key in (curses.KEY_DOWN, ord('j')) and selected < len(roms) - 1:
            selected += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            curses.endwin()
            launch(roms[selected])
            curses.wrapper(main)  # reopen picker after game exits
            return
        elif key in (ord('q'), ord('Q')):
            break


if __name__ == "__main__":
    if not os.path.isfile(CORE):
        print(f"RetroArch SNES core not found at:\n  {CORE}")
        print("Install with: sudo apt install libretro-snes9x -y")
        sys.exit(1)
    curses.wrapper(main)
