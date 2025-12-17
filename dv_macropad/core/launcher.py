import os
import subprocess
import webbrowser


def _safe_popen(cmd):
    """Lanza un proceso sin bloquear la app (Windows-friendly)."""
    subprocess.Popen(cmd, shell=True)


def open_powershell(powershell_exe: str = "powershell"):
    """Abre PowerShell."""
    _safe_popen([powershell_exe])


def open_cmd():
    """Abre CMD."""
    _safe_popen(["cmd"])


def open_python(python_exe: str = "python"):
    """Abre Python en consola."""
    _safe_popen([python_exe])


def open_windows_terminal():
    """Abre Windows Terminal (si está instalado)."""
    # 'wt' suele existir si tienes Windows Terminal.
    _safe_popen(["wt"])


def open_pycharm(pycharm_path: str):
    """Abre PyCharm desde una ruta configurable."""
    if pycharm_path and os.path.exists(pycharm_path):
        os.startfile(pycharm_path)
        return
    webbrowser.open("https://www.jetbrains.com/pycharm/")


def open_word(word_path: str = ""):
    """Abre Microsoft Word (ruta configurable)."""
    if word_path and os.path.exists(word_path):
        os.startfile(word_path)
        return
    # Fallback simple (si no hay Word instalado/ruta)
    webbrowser.open("https://www.office.com/")


def open_file_explorer():
    """Abre File Explorer."""
    os.startfile("explorer")


def open_notepad():
    """Abre Notepad."""
    _safe_popen(["notepad"])


def open_calculator():
    """Abre Calculator."""
    _safe_popen(["calc"])


def open_task_manager():
    """Abre Task Manager."""
    _safe_popen(["taskmgr"])


def open_settings():
    """Abre Windows Settings."""
    try:
        os.startfile("ms-settings:")
    except Exception:
        _safe_popen(["cmd", "/c", "start", "ms-settings:"])


def open_snipping_tool():
    """Abre Snipping Tool."""
    _safe_popen(["snippingtool"])


def open_browser():
    """Abre el navegador default."""
    webbrowser.open("about:blank")


def open_google():
    webbrowser.open("https://www.google.com")


def open_github():
    webbrowser.open("https://github.com")


def open_email():
    """Abre el cliente de email default."""
    webbrowser.open("mailto:")
