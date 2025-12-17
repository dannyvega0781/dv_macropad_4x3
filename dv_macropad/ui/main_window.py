import json
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import ctypes
import time

from ui.macropad import MacroPad
from ui.config_dialog import ConfigDialog
from core.actions import run_action


class MainWindow:
    def __init__(self, config: dict, config_path: Path):
        self.config_data = config
        self.config_path = config_path
        self.project_root = self.config_path.parent.parent

        self.root = tk.Tk()
        self.root.title("DV MacroPad")
        self.root.minsize(520, 320)

        # Track de foco en Windows (para que Ctrl+A/C/V vaya al documento/web)
        self.hwnd = None
        self.last_external_hwnd = None

        self._build_ui()
        self._apply_window_settings()

        # Inicia tracking de foco (Windows 11)
        self.root.after(200, self._init_focus_tracker)

    def _build_ui(self):
        top = ttk.Frame(self.root, padding=8)
        top.pack(fill="x")

        self.always_var = tk.BooleanVar(value=self.config_data.get("window", {}).get("always_on_top", True))

        ttk.Checkbutton(
            top,
            text="Always on Top",
            variable=self.always_var,
            command=self._toggle_always_on_top
        ).pack(side="left")

        ttk.Button(top, text="Minimize", command=self.root.iconify).pack(side="right")
        ttk.Button(top, text="Config", command=self._open_config).pack(side="right", padx=(0, 8))
        ttk.Button(top, text="Compact", command=self._toggle_compact).pack(side="right", padx=(0, 8))

        body = ttk.Frame(self.root, padding=8)
        body.pack(fill="both", expand=True)

        self.macropad = MacroPad(
            parent=body,
            config=self.config_data,
            on_action=self._on_action,
            project_root=self.project_root
        )
        self.macropad.pack(fill="both", expand=True)

    def _apply_window_settings(self):
        self.root.attributes("-topmost", bool(self.always_var.get()))

        compact = self.config_data.get("window", {}).get("compact_mode", False)
        if compact:
            self.root.geometry("560x360")
        else:
            self.root.geometry("700x460")

    def _toggle_always_on_top(self):
        self.root.attributes("-topmost", bool(self.always_var.get()))
        self.config_data.setdefault("window", {})["always_on_top"] = bool(self.always_var.get())
        self._save_config()

    def _toggle_compact(self):
        current = self.config_data.get("window", {}).get("compact_mode", False)
        self.config_data.setdefault("window", {})["compact_mode"] = not current
        self._save_config()
        self._apply_window_settings()

    def _save_config(self):
        with self.config_path.open("w", encoding="utf-8") as f:
            json.dump(self.config_data, f, indent=2, ensure_ascii=False)

    def _open_config(self):
        ConfigDialog(
            parent=self.root,
            config=self.config_data,
            config_path=self.config_path,
            on_save=self._on_config_saved
        )

    def _on_config_saved(self, new_config: dict):
        self.config_data = new_config
        self.macropad.rebuild(self.config_data)

    # -------------------------
    # Focus tracking (Windows 11)
    # -------------------------

    def _init_focus_tracker(self):
        try:
            self.hwnd = self.root.winfo_id()
        except Exception:
            self.hwnd = None
        self._track_focus_loop()

    def _track_focus_loop(self):
        try:
            user32 = ctypes.windll.user32
            fg = user32.GetForegroundWindow()
            if self.hwnd and fg and fg != self.hwnd:
                self.last_external_hwnd = fg
        except Exception:
            pass
        self.root.after(200, self._track_focus_loop)

    def _focus_last_external_window(self):
        if not self.last_external_hwnd:
            return
        user32 = ctypes.windll.user32
        user32.ShowWindow(self.last_external_hwnd, 5)  # SW_SHOW
        user32.SetForegroundWindow(self.last_external_hwnd)

    # -------------------------
    # Actions
    # -------------------------

    def _on_action(self, action_id: str):
        """
        No ocultamos la ventana.
        Antes de enviar hotkeys, devolvemos foco a la última ventana externa.
        """
        try:
            self._focus_last_external_window()
            time.sleep(0.05)
            run_action(action_id, self.config_data)
            self.root.attributes("-topmost", bool(self.always_var.get()))
        except Exception as e:
            self.root.title(f"DV MacroPad - Error: {e}")

    def run(self):
        self.root.mainloop()
