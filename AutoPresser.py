import platform, sys, threading, time, random
import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui

running = False
IS_MAC = platform.system() == "Darwin"
IS_WIN = platform.system() == "Windows"


def logic_thread():
    global running
    try:
        key = entry_key.get().strip() or "e"
        delay = float(entry_delay.get().strip() or 15.0)
        reps = int(entry_reps.get().strip() or 2)
        interval = float(entry_interval.get().strip() or 0.1)
        mode = mode_var.get()

        if mode == 2 and interval < 0.01:
            root.after(0, lambda: messagebox.showwarning("Safety", "Interval min 0.01s"))
            interval = 0.01

        for i in range(5, 0, -1):
            if not running: return
            root.after(0, lambda i=i: status.config(text=f"Mulai dalam {i}s...", fg="orange"))
            time.sleep(1)

        root.after(0, lambda: [
            status.config(text="STATUS: AKTIF", fg="green"),
            btn_start.config(state="disabled"),
            btn_stop.config(state="normal")
        ])

        while running:
            if mode == 1:
                pyautogui.press(key)
                time.sleep(delay + random.uniform(0, 4))
                for _ in range(reps):
                    if not running: break
                    pyautogui.press(key)
                    time.sleep(random.uniform(1.2, 2.5))
            else:
                pyautogui.click()
                time.sleep(interval)
    except Exception:
        root.after(0, stop_script)


def start_script():
    global running
    if not running:
        running = True
        btn_start.config(state="disabled")
        btn_stop.config(state="normal")
        threading.Thread(target=logic_thread, daemon=True).start()


def stop_script():
    global running
    running = False
    status.config(text="STATUS: STANDBY", fg="red")
    btn_start.config(state="normal")
    btn_stop.config(state="disabled")


# ── UI ─────────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Universal Key-Action")
root.geometry("390x460")
root.resizable(False, False)
mode_var = tk.IntVar(value=1)

# Fix crash menu bar macOS saat jalan sebagai .app bundle
if IS_MAC:
    menubar = tk.Menu(root)
    root.config(menu=menubar)

inst = tk.Frame(root, bg="#e1e1e1", pady=6)
inst.pack(fill="x")
tk.Label(inst, text="SHORTCUT:", font=("Arial", 9, "bold"), bg="#e1e1e1").pack()
tk.Label(inst, text="[  = START     ]  = STOP",
         font=("Arial", 12, "bold"), fg="#1a5c96", bg="#e1e1e1").pack(pady=2)
tk.Label(inst, text="(Tombol [ dan ] ada di sebelah kanan huruf P)",
         font=("Arial", 8), fg="#555", bg="#e1e1e1").pack()

gm = ttk.LabelFrame(root, text=" Keyboard Macro ")
gm.pack(fill="x", padx=15, pady=8)
tk.Radiobutton(gm, text="Aktifkan Mode Ini", variable=mode_var, value=1).pack(anchor="w", padx=5)
for lbl, var_name, default, w in [("Tombol:", "entry_key", "e", 5),
                                   ("Jeda(s):", "entry_delay", "15.0", 5),
                                   ("Reps:", "entry_reps", "2", 4)]:
    ttk.Label(gm, text=lbl).pack(side="left", padx=4)
    e = ttk.Entry(gm, width=w); e.insert(0, default); e.pack(side="left", pady=4)
    globals()[var_name] = e

gc = ttk.LabelFrame(root, text=" Auto Clicker ")
gc.pack(fill="x", padx=15, pady=8)
tk.Radiobutton(gc, text="Aktifkan Mode Ini", variable=mode_var, value=2).pack(anchor="w", padx=5)
ttk.Label(gc, text="Interval (detik):").pack(side="left", padx=5)
entry_interval = ttk.Entry(gc, width=8)
entry_interval.insert(0, "0.1")
entry_interval.pack(side="left")

status = tk.Label(root, text="STATUS: STANDBY", font=("Arial", 11, "bold"), fg="red")
status.pack(pady=8)

bf = ttk.Frame(root)
bf.pack(pady=4)
btn_start = ttk.Button(bf, text="START  ( [ )", command=start_script, width=14)
btn_start.pack(side="left", padx=5)
btn_stop = ttk.Button(bf, text="STOP  ( ] )", command=stop_script, width=14, state="disabled")
btn_stop.pack(side="left", padx=5)

warn_label = tk.Label(root, text="", font=("Arial", 8, "italic"), fg="red")
warn_label.pack(pady=2)

def update_warning(*_):
    try:
        val = float(entry_interval.get().strip() or 0.1)
        warn_label.config(text="⚠️  Interval terlalu rendah! Min 0.01s"
                          if mode_var.get() == 2 and val < 0.01 else "")
    except ValueError:
        warn_label.config(text="")

entry_interval.bind("<KeyRelease>", update_warning)
mode_var.trace_add("write", update_warning)

root.attributes("-topmost", True)

root.bind("[", lambda e: start_script())
root.bind("]", lambda e: stop_script())

# Windows: tambahkan global hotkey via pynput jika tersedia
if IS_WIN:
    try:
        from pynput import keyboard as kb
        def _on_press(key):
            try:
                if getattr(key, "char", None) == "[": root.after(0, start_script)
                elif getattr(key, "char", None) == "]": root.after(0, stop_script)
            except Exception: pass
        lst = kb.Listener(on_press=_on_press)
        lst.daemon = True
        lst.start()
    except Exception:
        pass

root.mainloop()