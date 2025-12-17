from core import hotkeys
from core import launcher


# Lista cerrada (la UI solo debe permitir elegir de aquí)
# Nota: Esta lista es el "contrato" entre UI <-> Core.
ACTION_IDS = [
    # Hotkeys (productividad)
    "HOTKEY_CTRL_A",
    "HOTKEY_CTRL_F",
    "HOTKEY_CTRL_Z",
    "HOTKEY_CTRL_Y",
    "HOTKEY_CTRL_C",
    "HOTKEY_CTRL_V",
    "HOTKEY_CTRL_X",
    "HOTKEY_CTRL_S",
    "HOTKEY_CTRL_SHIFT_S",
    "HOTKEY_CTRL_P",
    "HOTKEY_CTRL_N",
    "HOTKEY_CTRL_T",
    "HOTKEY_CTRL_W",
    "HOTKEY_CTRL_L",
    "HOTKEY_CTRL_SHIFT_T",
    "HOTKEY_CTRL_SHIFT_N",
    "HOTKEY_WIN_TAB",
    "HOTKEY_ALT_TAB",
    "HOTKEY_WIN_D",
    "HOTKEY_WIN_E",
    "HOTKEY_WIN_V",
    "HOTKEY_WIN_SHIFT_S",
    "HOTKEY_WIN_PERIOD",
    "HOTKEY_F5",
    "HOTKEY_DELETE",

    # Launchers (apps)
    "OPEN_POWERSHELL",
    "OPEN_CMD",
    "OPEN_WINDOWS_TERMINAL",
    "OPEN_PYTHON",
    "OPEN_PYCHARM",
    "OPEN_WORD",
    "OPEN_FILE_EXPLORER",
    "OPEN_NOTEPAD",
    "OPEN_CALCULATOR",
    "OPEN_TASK_MANAGER",
    "OPEN_SETTINGS",
    "OPEN_SNIPPING_TOOL",

    # Web
    "OPEN_BROWSER",
    "OPEN_GOOGLE",
    "OPEN_GITHUB",

    # Comunicación
    "OPEN_EMAIL",
]


def run_action(action_id: str, config: dict):
    """
    Ejecuta una acción basada en un ID.

    Por qué:
    - La UI no debe tener lógica de negocio.
    - La UI solo dice: "ejecuta ACTION_X".
    - Aquí centralizamos comportamiento y mantenemos el proyecto fácil de mantener.
    """
    action_id = (action_id or "").strip()
    app_paths = config.get("app_paths", {})

    # --- Hotkeys ---
    if action_id == "HOTKEY_CTRL_A":
        hotkeys.ctrl_a()
    elif action_id == "HOTKEY_CTRL_F":
        hotkeys.ctrl_f()
    elif action_id == "HOTKEY_CTRL_Z":
        hotkeys.ctrl_z()
    elif action_id == "HOTKEY_CTRL_Y":
        hotkeys.ctrl_y()

    elif action_id == "HOTKEY_CTRL_C":
        hotkeys.ctrl_c()
    elif action_id == "HOTKEY_CTRL_V":
        hotkeys.ctrl_v()
    elif action_id == "HOTKEY_CTRL_X":
        hotkeys.ctrl_x()

    elif action_id == "HOTKEY_CTRL_S":
        hotkeys.ctrl_s()
    elif action_id == "HOTKEY_CTRL_SHIFT_S":
        hotkeys.ctrl_shift_s()

    elif action_id == "HOTKEY_CTRL_P":
        hotkeys.ctrl_p()
    elif action_id == "HOTKEY_CTRL_N":
        hotkeys.ctrl_n()
    elif action_id == "HOTKEY_CTRL_T":
        hotkeys.ctrl_t()
    elif action_id == "HOTKEY_CTRL_W":
        hotkeys.ctrl_w()
    elif action_id == "HOTKEY_CTRL_L":
        hotkeys.ctrl_l()
    elif action_id == "HOTKEY_CTRL_SHIFT_T":
        hotkeys.ctrl_shift_t()
    elif action_id == "HOTKEY_CTRL_SHIFT_N":
        hotkeys.ctrl_shift_n()

    elif action_id == "HOTKEY_WIN_TAB":
        hotkeys.win_tab()
    elif action_id == "HOTKEY_ALT_TAB":
        hotkeys.alt_tab()
    elif action_id == "HOTKEY_WIN_D":
        hotkeys.win_d()
    elif action_id == "HOTKEY_WIN_E":
        hotkeys.win_e()
    elif action_id == "HOTKEY_WIN_V":
        hotkeys.win_v()
    elif action_id == "HOTKEY_WIN_SHIFT_S":
        hotkeys.win_shift_s()
    elif action_id == "HOTKEY_WIN_PERIOD":
        hotkeys.win_period()

    elif action_id == "HOTKEY_F5":
        hotkeys.f5()
    elif action_id == "HOTKEY_DELETE":
        hotkeys.delete_key()

    # --- Launchers ---
    elif action_id == "OPEN_POWERSHELL":
        launcher.open_powershell(app_paths.get("powershell_exe", "powershell"))
    elif action_id == "OPEN_CMD":
        launcher.open_cmd()
    elif action_id == "OPEN_WINDOWS_TERMINAL":
        launcher.open_windows_terminal()
    elif action_id == "OPEN_PYTHON":
        launcher.open_python(app_paths.get("python_exe", "python"))
    elif action_id == "OPEN_PYCHARM":
        launcher.open_pycharm(app_paths.get("pycharm_exe", ""))
    elif action_id == "OPEN_WORD":
        launcher.open_word(app_paths.get("word_exe", ""))
    elif action_id == "OPEN_FILE_EXPLORER":
        launcher.open_file_explorer()
    elif action_id == "OPEN_NOTEPAD":
        launcher.open_notepad()
    elif action_id == "OPEN_CALCULATOR":
        launcher.open_calculator()
    elif action_id == "OPEN_TASK_MANAGER":
        launcher.open_task_manager()
    elif action_id == "OPEN_SETTINGS":
        launcher.open_settings()
    elif action_id == "OPEN_SNIPPING_TOOL":
        launcher.open_snipping_tool()

    # --- Web / Comunicación ---
    elif action_id == "OPEN_BROWSER":
        launcher.open_browser()
    elif action_id == "OPEN_GOOGLE":
        launcher.open_google()
    elif action_id == "OPEN_GITHUB":
        launcher.open_github()
    elif action_id == "OPEN_EMAIL":
        launcher.open_email()

    else:
        raise ValueError(f"Acción no soportada: {action_id}")
