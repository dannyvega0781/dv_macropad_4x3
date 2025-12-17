import json
import sys
from pathlib import Path

from ui.main_window import MainWindow


def app_dir() -> Path:
    """
    Devuelve el directorio base de la app.

    Por qué:
    - En desarrollo, usamos la carpeta del proyecto.
    - En EXE (PyInstaller), queremos leer/escribir config al lado del .exe
      para que sea **editable** y portable.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def load_config(config_path: Path) -> dict:
    """
    Carga la configuración desde JSON.

    Por qué:
    - Queremos cambiar botones sin tocar código.
    - JSON es fácil de editar y de respaldar (Veeam).
    """
    if not config_path.exists():
        raise FileNotFoundError(f"No existe el archivo de config: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    base = app_dir()

    # Config externa (editable)
    config_path = base / "config" / "buttons.json"

    config = load_config(config_path)
    app = MainWindow(config=config, config_path=config_path)
    app.run()


if __name__ == "__main__":
    main()
