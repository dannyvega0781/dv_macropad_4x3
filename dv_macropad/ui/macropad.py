import tkinter as tk
from tkinter import ttk
from pathlib import Path

from PIL import Image, ImageTk


# Paleta simple pero más amplia (listas cerradas en Config)
COLOR_MAP = {
    "gray": "#3b3b3b",
    "blue": "#2b579a",
    "green": "#107c10",
    "orange": "#d83b01",
    "purple": "#5c2d91",
    "red": "#a80000",
    "teal": "#00796b",
    "yellow": "#f9a825",
    "pink": "#c2185b",
    "black": "#111111",
    "white": "#f5f5f5"
}


class MacroPad(ttk.Frame):
    """
    Grid configurable (por defecto 4x3 = 12 botones).
    Todos los botones salen de config/buttons.json -> config["buttons"].

    Soporta:
    - label (puede incluir emojis ✅)
    - color (lista cerrada)
    - icon (opcional): nombre de archivo dentro de assets/icons/
    """

    def __init__(self, parent, config: dict, on_action, project_root: Path):
        super().__init__(parent)
        self.config_data = config
        self.on_action = on_action
        self.project_root = project_root

        # Guardamos referencias de imágenes para que Tkinter no las "borre"
        self._images = []

        self._build_ui()

    def _build_ui(self):
        grid_cfg = self.config_data.get("grid", {})
        rows = int(grid_cfg.get("rows", 3))
        cols = int(grid_cfg.get("cols", 4))

        for r in range(rows):
            self.rowconfigure(r, weight=1)
        for c in range(cols):
            self.columnconfigure(c, weight=1)

        buttons = self.config_data.get("buttons", [])
        buttons = sorted(buttons, key=lambda b: b.get("slot", 0))

        total = rows * cols

        # Completa para que siempre exista el número exacto de botones del grid
        while len(buttons) < total:
            slot = len(buttons) + 1
            buttons.append({
                "slot": slot,
                "label": f"Slot {slot}",
                "action_id": "OPEN_BROWSER",
                "color": "gray",
                "icon": ""
            })

        positions = [(r, c) for r in range(rows) for c in range(cols)]

        for i, (row, col) in enumerate(positions):
            btn_cfg = buttons[i]
            label = btn_cfg.get("label", f"Slot {i + 1}")
            action_id = btn_cfg.get("action_id", "OPEN_BROWSER")
            color = btn_cfg.get("color", "gray")
            icon_name = btn_cfg.get("icon", "")

            self._make_button(
                row=row,
                col=col,
                label=label,
                action_id=action_id,
                color=color,
                icon_name=icon_name
            )

    def rebuild(self, new_config: dict):
        """Reconstruye el grid cuando se guarda configuración."""
        self.config_data = new_config
        self._images.clear()

        for child in self.winfo_children():
            child.destroy()

        self._build_ui()

    def _load_icon(self, icon_name: str):
        """Carga un icono PNG desde assets/icons/."""
        if not icon_name:
            return None

        icon_path = self.project_root / "assets" / "icons" / icon_name
        if not icon_path.exists():
            return None

        try:
            img = Image.open(icon_path).convert("RGBA")
            img = img.resize((26, 26))
            tk_img = ImageTk.PhotoImage(img)
            self._images.append(tk_img)
            return tk_img
        except Exception:
            return None

    def _make_button(self, row: int, col: int, label: str, action_id: str, color: str, icon_name: str = ""):
        bg = COLOR_MAP.get(color, COLOR_MAP["gray"])

        icon_img = self._load_icon(icon_name)

        # Si el color es "white", el texto negro se ve mejor
        fg = "black" if color == "white" else "white"
        active_fg = fg
        active_bg = bg

        btn = tk.Button(
            self,
            text=label,
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=active_fg,
            relief="raised",
            bd=2,
            command=lambda a=action_id: self.on_action(a)
        )

        if icon_img is not None:
            btn.configure(image=icon_img, compound="top")

        btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
