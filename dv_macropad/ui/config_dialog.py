import json
import tkinter as tk
from tkinter import ttk
from pathlib import Path

from core.actions import ACTION_IDS


COLOR_CHOICES = [
    "gray", "blue", "green", "orange", "purple", "red",
    "teal", "yellow", "pink", "black", "white"
]


class ConfigDialog(tk.Toplevel):
    """
    Configuración de botones (12 por defecto, grid 4x3).
    - Label: editable (puede incluir emojis ✅)
    - Action: lista cerrada (ACTION_IDS)
    - Color: lista cerrada
    - Icon: lista cerrada leyendo assets/icons/
    """

    def __init__(self, parent, config: dict, config_path: Path, on_save):
        super().__init__(parent)
        self.title("Configurar botones")
        self.resizable(True, True)

        self.parent = parent
        self.config_data = config
        self.config_path = config_path
        self.on_save = on_save

        self.project_root = self.config_path.parent.parent
        self.icon_choices = self._load_icon_choices()

        # Modal + traer al frente (importantísimo con Always on Top)
        self.transient(parent)
        self.grab_set()
        self.lift()
        self.focus_force()

        self._rows = []
        self._build_ui()

    def _load_icon_choices(self):
        icons_dir = self.project_root / "assets" / "icons"
        if not icons_dir.exists():
            return [""]

        files = sorted([p.name for p in icons_dir.iterdir() if p.is_file() and p.suffix.lower() in [".png", ".jpg", ".jpeg"]])
        return [""] + files

    def _build_ui(self):
        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Edita tus botones (Label admite emojis):").pack(anchor="w")

        table = ttk.Frame(container)
        table.pack(fill="both", expand=True, pady=(10, 10))

        headers = ["Slot", "Label", "Action", "Color", "Icon"]
        for c, h in enumerate(headers):
            ttk.Label(table, text=h).grid(row=0, column=c, sticky="w", padx=6, pady=6)

        grid_cfg = self.config_data.get("grid", {})
        rows = int(grid_cfg.get("rows", 3))
        cols = int(grid_cfg.get("cols", 4))
        total = rows * cols

        buttons = self.config_data.get("buttons", [])
        buttons = sorted(buttons, key=lambda b: b.get("slot", 0))

        while len(buttons) < total:
            slot = len(buttons) + 1
            buttons.append({
                "slot": slot,
                "label": f"Slot {slot}",
                "action_id": "OPEN_BROWSER",
                "color": "gray",
                "icon": ""
            })

        for i, btn in enumerate(buttons[:total]):
            slot = btn.get("slot", i + 1)

            label_var = tk.StringVar(value=btn.get("label", f"Slot {slot}"))
            action_var = tk.StringVar(value=btn.get("action_id", "OPEN_BROWSER"))
            color_var = tk.StringVar(value=btn.get("color", "gray"))
            icon_var = tk.StringVar(value=btn.get("icon", ""))

            ttk.Label(table, text=str(slot)).grid(row=i + 1, column=0, sticky="w", padx=6, pady=6)

            ttk.Entry(table, textvariable=label_var, width=20).grid(row=i + 1, column=1, sticky="we", padx=6, pady=6)

            ttk.Combobox(
                table, textvariable=action_var, values=ACTION_IDS, state="readonly", width=28
            ).grid(row=i + 1, column=2, sticky="we", padx=6, pady=6)

            ttk.Combobox(
                table, textvariable=color_var, values=COLOR_CHOICES, state="readonly", width=10
            ).grid(row=i + 1, column=3, sticky="we", padx=6, pady=6)

            ttk.Combobox(
                table, textvariable=icon_var, values=self.icon_choices, state="readonly", width=18
            ).grid(row=i + 1, column=4, sticky="we", padx=6, pady=6)

            self._rows.append((slot, label_var, action_var, color_var, icon_var))

        actions = ttk.Frame(container)
        actions.pack(fill="x")

        ttk.Button(actions, text="Guardar", command=self._save).pack(side="right", padx=(6, 0))
        ttk.Button(actions, text="Cancelar", command=self.destroy).pack(side="right")

    def _save(self):
        updated = dict(self.config_data)

        grid_cfg = updated.setdefault("grid", {})
        rows = int(grid_cfg.get("rows", 3))
        cols = int(grid_cfg.get("cols", 4))
        total = rows * cols

        new_buttons = []
        for (slot, label_var, action_var, color_var, icon_var) in self._rows[:total]:
            new_buttons.append({
                "slot": slot,
                "label": label_var.get().strip() or f"Slot {slot}",
                "action_id": action_var.get(),
                "color": color_var.get(),
                "icon": icon_var.get()
            })

        updated["buttons"] = new_buttons

        with self.config_path.open("w", encoding="utf-8") as f:
            json.dump(updated, f, indent=2, ensure_ascii=False)

        self.on_save(updated)
        self.destroy()
