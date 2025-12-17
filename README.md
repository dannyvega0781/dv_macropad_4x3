DV MacroPad (v1.1)
MacroPad de escritorio (software) para Windows 11, pensado para productividad diaria y para aprender:

GUI (Tkinter)
eventos / callbacks
configuración externa (JSON)
empaquetado a EXE (PyInstaller)
Qué incluye
Grid 4×3 (12 botones) configurables
Botón Config para editar:
Label (admite emojis ✅)
Action (lista cerrada)
Color (lista cerrada)
Icon (opcional, desde assets/icons/)
Always on Top (opcional)
Modo compacto
Hotkeys (importante)
Los hotkeys (Ctrl+A/C/V/etc.) se envían a la ventana activa. Esta app intenta devolver el foco a tu última ventana externa (Chrome/Word/Notepad) antes de enviar el atajo.

Si un hotkey no funciona:

Asegúrate de que el cursor esté dentro del documento (no en la barra de direcciones).
Si la app destino está abierta como Administrador, ejecuta el MacroPad como Administrador también.
Estructura
dv_macropad/
├─ app.py
├─ requirements.txt
├─ config/
│  └─ buttons.json
├─ ui/
├─ core/
├─ assets/
│  └─ icons/
└─ build/
   └─ build_exe.py
Ejecutar en desarrollo
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
Empaquetar a EXE portable
python build\build_exe.py
Salida típica:

dist\DV_MacroPad.exe
Portable recomendado
Crea una carpeta:

DV_MacroPad_Portable/
DV_MacroPad.exe
config/buttons.json
assets/icons/ (solo si usas iconos)
