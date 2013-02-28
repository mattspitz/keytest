import curses

def init_screen():
    screen = curses.initscr()
    screen.keypad(1)
    return screen

def loop(screen):
    all_keys = []

    while True:
        screen.clear()

        OFFSET = 1
        max_height, max_width = screen.getmaxyx()
        for idx, key in enumerate(all_keys[:(max_height - OFFSET)]):
            screen.addstr(idx + OFFSET, 0, key, curses.A_NORMAL)

        screen.refresh()
        raw_key = screen.getch(0, 0)
        all_keys.insert(0, "{:d} => {}".format(raw_key, curses.keyname(raw_key)))

def cleanup_curses():
    curses.nocbreak()
    curses.echo()
    curses.endwin()

def main():
    screen = init_screen()

    try:
        loop(screen)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup_curses()

if __name__ == "__main__":
    main()
