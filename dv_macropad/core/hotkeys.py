import pyautogui

# Nota:
# - Los hotkeys se envían a la ventana ACTIVA.
# - En Windows, si el MacroPad toma foco, el atajo puede ir al MacroPad.
# - Por eso, la ventana principal intenta devolver el foco a la última app externa antes de enviar hotkeys.


def ctrl_a():
    """Select All -> Ctrl + A"""
    pyautogui.hotkey("ctrl", "a")


def ctrl_f():
    """Find -> Ctrl + F"""
    pyautogui.hotkey("ctrl", "f")


def ctrl_z():
    """Undo -> Ctrl + Z"""
    pyautogui.hotkey("ctrl", "z")


def ctrl_y():
    """Redo -> Ctrl + Y"""
    pyautogui.hotkey("ctrl", "y")


def ctrl_c():
    """Copy -> Ctrl + C"""
    pyautogui.hotkey("ctrl", "c")


def ctrl_v():
    """Paste -> Ctrl + V"""
    pyautogui.hotkey("ctrl", "v")


def ctrl_x():
    """Cut -> Ctrl + X"""
    pyautogui.hotkey("ctrl", "x")


def ctrl_s():
    """Save -> Ctrl + S"""
    pyautogui.hotkey("ctrl", "s")


def ctrl_shift_s():
    """Save As -> Ctrl + Shift + S"""
    pyautogui.hotkey("ctrl", "shift", "s")


def ctrl_p():
    """Print -> Ctrl + P"""
    pyautogui.hotkey("ctrl", "p")


def ctrl_n():
    """New -> Ctrl + N"""
    pyautogui.hotkey("ctrl", "n")


def ctrl_t():
    """New Tab -> Ctrl + T"""
    pyautogui.hotkey("ctrl", "t")


def ctrl_w():
    """Close Tab/Window -> Ctrl + W"""
    pyautogui.hotkey("ctrl", "w")


def ctrl_l():
    """Focus address bar / location -> Ctrl + L"""
    pyautogui.hotkey("ctrl", "l")


def ctrl_shift_t():
    """Reopen closed tab -> Ctrl + Shift + T"""
    pyautogui.hotkey("ctrl", "shift", "t")


def ctrl_shift_n():
    """New incognito window (Chrome) / new window -> Ctrl + Shift + N"""
    pyautogui.hotkey("ctrl", "shift", "n")


def win_tab():
    """Task View -> Win + Tab"""
    pyautogui.hotkey("win", "tab")


def alt_tab():
    """Switch app -> Alt + Tab"""
    pyautogui.hotkey("alt", "tab")


def win_d():
    """Show desktop -> Win + D"""
    pyautogui.hotkey("win", "d")


def win_e():
    """Open File Explorer -> Win + E"""
    pyautogui.hotkey("win", "e")


def win_v():
    """Clipboard history -> Win + V"""
    pyautogui.hotkey("win", "v")


def win_shift_s():
    """Screen snip -> Win + Shift + S"""
    pyautogui.hotkey("win", "shift", "s")


def win_period():
    """Emoji panel -> Win + ."""
    pyautogui.hotkey("win", ".")


def f5():
    """Run/Refresh -> F5"""
    pyautogui.press("f5")


def delete_key():
    """Delete -> tecla Delete"""
    pyautogui.press("delete")
