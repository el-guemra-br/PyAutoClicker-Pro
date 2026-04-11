import threading
import time
import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
from io import BytesIO
from pathlib import Path

import pyautogui

try:
    from PIL import Image, ImageTk
except (ImportError, OSError):
    Image = None
    ImageTk = None

try:
    import cairosvg
except (ImportError, OSError, Exception):
    cairosvg = None

try:
    import keyboard  # Optional global hotkeys
except Exception:
    keyboard = None


class AutoClickerModernApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("PyAutoClicker Pro Modern")
        self.root.geometry("520x520")
        self.root.minsize(500, 500)

        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self._configure_styles()

        self.running = False
        self.paused = False
        self.stop_event = threading.Event()
        self.worker_thread = None

        self.click_count = 0
        self.started_at = None

        self.icon_images = {}
        self._load_svg_icons()

        self._build_ui()
        self._setup_hotkeys()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _load_svg_icons(self):
        """Load SVG icons and convert to PhotoImage."""
        if not (Image and ImageTk and cairosvg):
            return
        
        icons = {"github": "github_icon.svg", "instagram": "instagram_icon.svg"}
        script_dir = Path(__file__).parent
        
        for name, filename in icons.items():
            icon_path = script_dir / filename
            if icon_path.exists():
                try:
                    png_bytes = BytesIO()
                    cairosvg.svg2png(url=str(icon_path), write_to=png_bytes, output_width=32, output_height=32)
                    png_bytes.seek(0)
                    image = Image.open(png_bytes).convert("RGBA")
                    self.icon_images[name] = ImageTk.PhotoImage(image)
                except Exception:
                    pass

    def _configure_styles(self):
        bg = "#10141c"
        panel = "#171c26"
        card = "#1f2633"
        text = "#e8edf7"
        subtle = "#9aa8c7"
        accent = "#00c389"
        warning = "#f4b400"
        danger = "#ff5d73"

        self.colors = {
            "bg": bg,
            "panel": panel,
            "card": card,
            "text": text,
            "subtle": subtle,
            "accent": accent,
            "warning": warning,
            "danger": danger,
        }

        self.root.configure(bg=bg)

        self.style.configure("Root.TFrame", background=bg)
        self.style.configure("Panel.TFrame", background=panel)
        self.style.configure("Card.TFrame", background=card)

        self.style.configure(
            "Title.TLabel",
            background=bg,
            foreground=text,
            font=("Segoe UI", 18, "bold"),
        )
        self.style.configure(
            "Subtitle.TLabel",
            background=bg,
            foreground=subtle,
            font=("Segoe UI", 10),
        )
        self.style.configure(
            "Label.TLabel",
            background=card,
            foreground=text,
            font=("Segoe UI", 10),
        )
        self.style.configure(
            "Value.TLabel",
            background=card,
            foreground=accent,
            font=("Consolas", 10, "bold"),
        )

        self.style.configure(
            "TEntry",
            fieldbackground="#0f1320",
            background="#0f1320",
            foreground=text,
            insertcolor=text,
            bordercolor="#2c3750",
            lightcolor="#2c3750",
            darkcolor="#2c3750",
            relief="flat",
            padding=6,
        )

        self.style.configure(
            "TCombobox",
            fieldbackground="#0f1320",
            background="#0f1320",
            foreground=text,
            arrowsize=14,
            relief="flat",
            padding=6,
        )

        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#0f1320")],
            selectbackground=[("readonly", "#0f1320")],
            selectforeground=[("readonly", text)],
        )

        self.style.configure(
            "Accent.TButton",
            background=accent,
            foreground="#07150f",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            borderwidth=0,
            relief="flat",
        )
        self.style.map(
            "Accent.TButton",
            background=[("active", "#00b27d"), ("disabled", "#4c5967")],
            foreground=[("disabled", "#d4d9e1")],
        )

        self.style.configure(
            "Warn.TButton",
            background=warning,
            foreground="#2b2001",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            borderwidth=0,
            relief="flat",
        )
        self.style.map("Warn.TButton", background=[("active", "#dda400")])

        self.style.configure(
            "Danger.TButton",
            background=danger,
            foreground="#2f0310",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            borderwidth=0,
            relief="flat",
        )
        self.style.map("Danger.TButton", background=[("active", "#e44f64")])

        self.style.configure(
            "Status.Horizontal.TProgressbar",
            troughcolor="#0f1320",
            background=accent,
            bordercolor="#0f1320",
            lightcolor=accent,
            darkcolor=accent,
        )

        self.style.configure(
            "Icon.TButton",
            background="#0f1320",
            foreground=text,
            font=("Segoe UI", 12, "bold"),
            padding=6,
            borderwidth=0,
            relief="flat",
        )
        self.style.map(
            "Icon.TButton",
            background=[("active", "#2a3346")],
            foreground=[("active", accent)],
        )

    def _build_ui(self):
        root_wrap = ttk.Frame(self.root, style="Root.TFrame", padding=16)
        root_wrap.pack(fill="both", expand=True)

        header_row = ttk.Frame(root_wrap, style="Root.TFrame")
        header_row.pack(fill="x", pady=(0, 12))

        ttk.Label(header_row, text="PyAutoClicker Pro", style="Title.TLabel").pack(side="left", anchor="w")

        icon_container = ttk.Frame(header_row, style="Root.TFrame")
        icon_container.pack(side="right", padx=(0, 0))

        if "github" in self.icon_images:
            gh_btn = tk.Button(
                icon_container,
                image=self.icon_images["github"],
                command=lambda: self._open_link("https://github.com/el-guemra-br"),
                bg=self.colors["bg"],
                border=0,
                highlightthickness=0,
                activebackground=self.colors["card"],
            )
            gh_btn.image = self.icon_images["github"]
            gh_btn.pack(side="right", padx=(6, 0))
        else:
            ttk.Button(
                icon_container,
                text="GH",
                style="Icon.TButton",
                command=lambda: self._open_link("https://github.com/el-guemra-br"),
            ).pack(side="right", padx=(6, 0))

        if "instagram" in self.icon_images:
            ig_btn = tk.Button(
                icon_container,
                image=self.icon_images["instagram"],
                command=lambda: self._open_link("https://instagram.com/el_guemra_br"),
                bg=self.colors["bg"],
                border=0,
                highlightthickness=0,
                activebackground=self.colors["card"],
            )
            ig_btn.image = self.icon_images["instagram"]
            ig_btn.pack(side="right")
        else:
            ttk.Button(
                icon_container,
                text="IG",
                style="Icon.TButton",
                command=lambda: self._open_link("https://instagram.com/el_guemra_br"),
            ).pack(side="right")

        ttk.Label(
            root_wrap,
            text="Modern control panel with live status and safe start/pause/stop flow",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(0, 14))

        card = ttk.Frame(root_wrap, style="Card.TFrame", padding=14)
        card.pack(fill="x")

        self.start_delay_var = tk.StringVar(value="3")
        self.interval_ms_var = tk.StringVar(value="120")
        self.hold_ms_var = tk.StringVar(value="15")
        self.max_clicks_var = tk.StringVar(value="0")
        self.button_var = tk.StringVar(value="left")
        self.smart_pause_var = tk.BooleanVar(value=True)
        self.settle_ms_var = tk.StringVar(value="250")

        self._row_entry(card, 0, "Start Delay (s)", self.start_delay_var)
        self._row_entry(card, 1, "Interval (ms)", self.interval_ms_var)
        self._row_entry(card, 2, "Hold Duration (ms)", self.hold_ms_var)
        self._row_entry(card, 3, "Max Clicks (0 = infinite)", self.max_clicks_var)

        ttk.Label(card, text="Mouse Button", style="Label.TLabel").grid(
            row=4, column=0, sticky="w", pady=(8, 8)
        )
        button_box = ttk.Combobox(
            card,
            textvariable=self.button_var,
            values=("left", "right", "middle"),
            state="readonly",
            width=22,
        )
        button_box.grid(row=4, column=1, sticky="ew", pady=(8, 8), padx=(12, 0))

        ttk.Checkbutton(
            card,
            text="Smart Pause While Cursor Is Moving",
            variable=self.smart_pause_var,
            style="Label.TLabel",
        ).grid(row=5, column=0, sticky="w", pady=(6, 0))
        settle_entry = ttk.Entry(card, textvariable=self.settle_ms_var)
        settle_entry.grid(row=5, column=1, sticky="ew", pady=(6, 0), padx=(12, 0))

        card.columnconfigure(1, weight=1)

        status_card = ttk.Frame(root_wrap, style="Card.TFrame", padding=14)
        status_card.pack(fill="x", pady=(12, 0))

        self.status_var = tk.StringVar(value="Idle")
        self.count_var = tk.StringVar(value="Clicks: 0")
        self.uptime_var = tk.StringVar(value="Uptime: 00:00")

        ttk.Label(status_card, text="Status", style="Label.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(status_card, textvariable=self.status_var, style="Value.TLabel").grid(
            row=0, column=1, sticky="e"
        )

        ttk.Label(status_card, text="Counter", style="Label.TLabel").grid(row=1, column=0, sticky="w", pady=(6, 0))
        ttk.Label(status_card, textvariable=self.count_var, style="Value.TLabel").grid(
            row=1, column=1, sticky="e", pady=(6, 0)
        )

        ttk.Label(status_card, text="Runtime", style="Label.TLabel").grid(row=2, column=0, sticky="w", pady=(6, 0))
        ttk.Label(status_card, textvariable=self.uptime_var, style="Value.TLabel").grid(
            row=2, column=1, sticky="e", pady=(6, 0)
        )

        status_card.columnconfigure(1, weight=1)

        self.progress = ttk.Progressbar(
            root_wrap,
            style="Status.Horizontal.TProgressbar",
            orient="horizontal",
            mode="indeterminate",
        )
        self.progress.pack(fill="x", pady=(12, 8))

        controls = ttk.Frame(root_wrap, style="Root.TFrame")
        controls.pack(fill="x", pady=(4, 6))

        self.start_btn = ttk.Button(controls, text="Start", style="Accent.TButton", command=self.start)
        self.pause_btn = ttk.Button(controls, text="Pause", style="Warn.TButton", command=self.toggle_pause)
        self.stop_btn = ttk.Button(controls, text="Stop", style="Danger.TButton", command=self.stop)

        self.start_btn.pack(side="left", padx=(0, 8), fill="x", expand=True)
        self.pause_btn.pack(side="left", padx=(0, 8), fill="x", expand=True)
        self.stop_btn.pack(side="left", fill="x", expand=True)

        footer = ttk.Label(
            root_wrap,
            text=(
                "Hotkeys: Shift+P = Pause/Resume, Esc = Stop"
                if keyboard
                else "Hotkeys disabled (keyboard module unavailable)."
            ),
            style="Subtitle.TLabel",
        )
        footer.pack(anchor="w", pady=(6, 0))

        self._refresh_ui_state()
        self._tick_ui()

    def _row_entry(self, parent, row, label, variable):
        ttk.Label(parent, text=label, style="Label.TLabel").grid(row=row, column=0, sticky="w", pady=(8, 0))
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=(8, 0), padx=(12, 0))

    def _setup_hotkeys(self):
        if not keyboard:
            return

        try:
            keyboard.add_hotkey("shift+p", self._hotkey_toggle_pause)
            keyboard.add_hotkey("esc", self._hotkey_stop)
        except Exception:
            # Some systems block global hotkeys without admin rights.
            pass

    def _hotkey_toggle_pause(self):
        self.root.after(0, self.toggle_pause)

    def _hotkey_stop(self):
        self.root.after(0, self.stop)

    def _parse_config(self):
        try:
            start_delay = float(self.start_delay_var.get().strip())
            interval_ms = float(self.interval_ms_var.get().strip())
            hold_ms = float(self.hold_ms_var.get().strip())
            max_clicks = int(self.max_clicks_var.get().strip())
            settle_ms = float(self.settle_ms_var.get().strip())
            button = self.button_var.get().strip().lower()
        except ValueError:
            raise ValueError("All numeric fields must contain valid numbers.")

        if start_delay < 0:
            raise ValueError("Start delay must be 0 or greater.")
        if interval_ms <= 0:
            raise ValueError("Interval must be greater than 0 ms.")
        if hold_ms < 0:
            raise ValueError("Hold duration must be 0 or greater.")
        if max_clicks < 0:
            raise ValueError("Max clicks must be 0 or a positive number.")
        if settle_ms < 0:
            raise ValueError("Settle delay must be 0 or greater.")
        if button not in {"left", "right", "middle"}:
            raise ValueError("Mouse button must be left, right, or middle.")

        return {
            "start_delay": start_delay,
            "interval_s": interval_ms / 1000.0,
            "hold_s": hold_ms / 1000.0,
            "max_clicks": max_clicks,
            "smart_pause": self.smart_pause_var.get(),
            "settle_s": settle_ms / 1000.0,
            "button": button,
        }

    def start(self):
        if self.running:
            return

        try:
            config = self._parse_config()
        except ValueError as exc:
            messagebox.showerror("Invalid Configuration", str(exc))
            return

        self.running = True
        self.paused = False
        self.stop_event.clear()
        self.click_count = 0
        self.started_at = time.time()

        self.worker_thread = threading.Thread(target=self._click_loop, args=(config,), daemon=True)
        self.worker_thread.start()

        self.status_var.set("Armed")
        self.progress.start(10)
        self._refresh_ui_state()

    def toggle_pause(self):
        if not self.running:
            return

        self.paused = not self.paused
        self.status_var.set("Paused" if self.paused else "Running")
        self.pause_btn.configure(text="Resume" if self.paused else "Pause")

    def stop(self):
        if not self.running and not self.paused:
            self.status_var.set("Idle")
            self._refresh_ui_state()
            return

        self.stop_event.set()
        self.running = False
        self.paused = False
        self.progress.stop()
        self.status_var.set("Stopped")
        self.pause_btn.configure(text="Pause")
        self._refresh_ui_state()

    def _click_loop(self, config):
        delay_end = time.time() + config["start_delay"]
        while time.time() < delay_end and not self.stop_event.is_set():
            self.root.after(0, lambda: self.status_var.set("Countdown"))
            time.sleep(0.05)

        if self.stop_event.is_set():
            return

        self.root.after(0, lambda: self.status_var.set("Running"))
        last_pos = pyautogui.position()
        last_move_at = time.time()

        while not self.stop_event.is_set():
            if self.paused:
                time.sleep(0.05)
                continue

            if config["smart_pause"]:
                current_pos = pyautogui.position()
                if current_pos != last_pos:
                    last_pos = current_pos
                    last_move_at = time.time()
                    self.root.after(0, lambda: self.status_var.set("Mouse Moving"))
                    time.sleep(0.03)
                    continue
                if (time.time() - last_move_at) < config["settle_s"]:
                    self.root.after(0, lambda: self.status_var.set("Waiting Stable"))
                    time.sleep(0.03)
                    continue
                self.root.after(0, lambda: self.status_var.set("Running"))

            pyautogui.mouseDown(button=config["button"])
            if config["hold_s"] > 0:
                time.sleep(config["hold_s"])
            pyautogui.mouseUp(button=config["button"])

            self.click_count += 1
            self.root.after(0, self._update_counter)

            if config["max_clicks"] > 0 and self.click_count >= config["max_clicks"]:
                self.root.after(0, self.stop)
                return

            time.sleep(config["interval_s"])

    def _update_counter(self):
        self.count_var.set(f"Clicks: {self.click_count}")

    def _tick_ui(self):
        if self.started_at and self.running:
            elapsed = int(time.time() - self.started_at)
            mm = elapsed // 60
            ss = elapsed % 60
            self.uptime_var.set(f"Uptime: {mm:02d}:{ss:02d}")
        elif not self.running:
            self.uptime_var.set("Uptime: 00:00")

        self.root.after(250, self._tick_ui)

    def _refresh_ui_state(self):
        can_edit = not self.running
        state = "normal" if can_edit else "disabled"

        for child in self.root.winfo_children():
            self._set_entries_state_recursive(child, state)

        self.start_btn.configure(state="normal" if not self.running else "disabled")
        self.pause_btn.configure(state="normal" if self.running else "disabled")
        self.stop_btn.configure(state="normal" if self.running else "disabled")

        if not self.running:
            self.count_var.set(f"Clicks: {self.click_count}")

    def _set_entries_state_recursive(self, widget, state):
        if isinstance(widget, ttk.Entry):
            widget.configure(state=state)
        if isinstance(widget, ttk.Combobox):
            widget.configure(state="readonly" if state == "normal" else "disabled")
        if isinstance(widget, ttk.Checkbutton):
            widget.configure(state=state)
        for child in widget.winfo_children():
            self._set_entries_state_recursive(child, state)

    def _on_close(self):
        self.stop_event.set()
        if keyboard:
            try:
                keyboard.clear_all_hotkeys()
            except Exception:
                pass
        self.root.destroy()

    def _open_link(self, url):
        try:
            webbrowser.open_new_tab(url)
        except Exception:
            messagebox.showerror("Open Link", "Could not open the link in your browser.")


def main():
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0

    root = tk.Tk()
    app = AutoClickerModernApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
