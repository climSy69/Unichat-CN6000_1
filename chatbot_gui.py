import sys
import ctypes
import webbrowser
import tkinter as tk
from datetime import datetime

# Tell Windows to render at native DPI instead of scaling a blurry bitmap
if sys.platform == "win32":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


# ─── CHATBOT LOGIC ────────────────────────────────────────────────────────────

def get_response(user_input):
    user = user_input.lower()

    if "τηλέφωνο" in user or "τηλεφωνο" in user:
        return "Το τηλέφωνο της γραμματείας είναι 210XXXXXXX.\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("ωρες" in user or "ώρες" in user) and "γραμματ" in user:
        return "Η γραμματεία λειτουργεί από 09:00 έως 15:00.\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("που" in user or "πού" in user or "διευθυνση" in user or "διεύθυνση" in user
          or "βρίσκεται" in user or "βρισκεται" in user
          or "location" in user or "maps" in user or "address" in user):
        return ("Το πανεπιστήμιο βρίσκεται στο Μαρούσι.\n"
                "Πώς αλλιώς μπορώ να σε βοηθήσω;"
                "\n__MAPLINK__:https://maps.app.goo.gl/ad64hHNiE3wW3HUM9")

    elif ("email" in user or "μειλ" in user or "mail" in user
          or "επικοινωνια" in user or "επικοινωνία" in user):
        return "Το email της σχολής είναι info@mitropolitiko.edu.gr\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("εξεταστικη" in user or "εξεταστική" in user
          or "exams" in user or "exam" in user
          or "εξετασεις" in user or "εξετάσεις" in user):
        return "Η εξεταστική περίοδος ξεκινά τον Ιούνιο.\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("βαθμοι" in user or "βαθμοί" in user
          or "grades" in user or "results" in user
          or "αποτελεσματα" in user or "αποτελέσματα" in user
          or "moodle" in user):
        return ("Οι βαθμοί ανακοινώνονται μέσω της εφαρμογής Moodle,\n"
                "στο section INFORMATION & ANNOUNCEMENTS.\n"
                "Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εγγραφες" in user or "εγγραφές" in user
          or "registration" in user or "registrations" in user
          or "enroll" in user or "enrollment" in user):
        return "Οι εγγραφές πραγματοποιούνται έως τα τέλη Σεπτεμβρίου.\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("βιβλιοθηκη" in user or "βιβλιοθήκη" in user
          or "library" in user
          or "βιβλια" in user or "βιβλία" in user):
        return ("Η βιβλιοθήκη του Μητροπολιτικού Κολλεγίου διαθέτει\n"
                "χιλιάδες τίτλους βιβλίων, υπολογιστές και δωρεάν WiFi.\n"
                "Email Campus Αμαρουσίου: amclibrary@mitropolitiko.edu.gr\n"
                "Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("isic" in user or "card" in user
          or "καρτα" in user or "κάρτα" in user
          or "student card" in user):
        return ("Η κάρτα ISIC εκδίδεται ηλεκτρονικά μέσω του Κολλεγίου.\n"
                "Απαιτούνται βεβαίωση σπουδών, στοιχεία φοιτητή και κόστος 15€.\n"
                "Η ενεργοποίηση ολοκληρώνεται σε 1-3 ημέρες μέσω εφαρμογής.\n"
                "Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("χειμερινα" in user or "χειμερινά" in user
          or "μαθηματα" in user or "μαθήματα" in user
          or "winter" in user or "courses" in user):
        return "Τα χειμερινά μαθήματα ξεκινούν στα μέσα Οκτωβρίου.\nΠώς αλλιώς μπορώ να σε βοηθήσω;"

    elif ("εκπτωση" in user or "έκπτωση" in user
          or "discount" in user
          or "προσφορα" in user or "προσφορά" in user
          or "διδακτρα" in user or "δίδακτρα" in user):
        return ("Υπάρχει έκπτωση 20% στα δίδακτρα\n"
                "για εγγραφές έως τα τέλη Φεβρουαρίου.\n"
                "Πώς αλλιώς μπορώ να σε βοηθήσω;")

    return "Συγγνώμη, δεν κατάλαβα την ερώτηση.\nΜπορείς να δοκιμάσεις ξανά."


# ─── THEMES ───────────────────────────────────────────────────────────────────

DARK = {
    "bg":           "#1a1a1a",
    "topbar":       "#111111",
    "sidebar_bg":   "#161616",
    "chat_bg":      "#1a1a1a",
    "user_bubble":  "#a93226",
    "bot_bubble":   "#242424",
    "user_fg":      "#ffffff",
    "bot_fg":       "#e4e4e4",
    "user_time":    "#f0a0a0",
    "bot_time":     "#606060",
    "input_bg":     "#1f1f1f",
    "input_fg":     "#f0f0f0",
    "input_border": "#383838",
    "send_bg":      "#c0392b",
    "send_fg":      "#ffffff",
    "sidebar_fg":   "#bbbbbb",
    "sidebar_btn":  "#1e1e1e",
    "sidebar_bfg":  "#e4e4e4",
    "title_fg":     "#f0f0f0",
    "divider":      "#272727",
    "quick_bg":     "#1e1e1e",
    "quick_fg":     "#c0c0c0",
    "quick_accent": "#c0392b",
    "toggle":       "☾",
}

LIGHT = {
    "bg":           "#f2f2f2",
    "topbar":       "#ffffff",
    "sidebar_bg":   "#fafafa",
    "chat_bg":      "#f2f2f2",
    "user_bubble":  "#c0392b",
    "bot_bubble":   "#e8e8e8",
    "user_fg":      "#ffffff",
    "bot_fg":       "#1a1a1a",
    "user_time":    "#ffcccc",
    "bot_time":     "#999999",
    "input_bg":     "#ffffff",
    "input_fg":     "#1a1a1a",
    "input_border": "#d0d0d0",
    "send_bg":      "#c0392b",
    "send_fg":      "#ffffff",
    "sidebar_fg":   "#444444",
    "sidebar_btn":  "#eeeeee",
    "sidebar_bfg":  "#1a1a1a",
    "title_fg":     "#1a1a1a",
    "divider":      "#e0e0e0",
    "quick_bg":     "#f5f5f5",
    "quick_fg":     "#444444",
    "quick_accent": "#c0392b",
    "toggle":       "☀",
}

QUICK_ACTIONS = [
    ("  Πού βρίσκεται η σχολή;",    "πού βρίσκεται η σχολή"),
    ("  Email επικοινωνίας σχολής",  "email επικοινωνίας σχολής"),
    ("  Τηλέφωνο γραμματείας",       "τηλέφωνο γραμματείας"),
]


# ─── GUI APPLICATION ──────────────────────────────────────────────────────────

class UniChatApp:

    FAQ_ITEMS = [
        ("Πού βρίσκεται η σχολή;",            "πού βρίσκεται η σχολή"),
        ("Πληροφορίες βιβλιοθήκης",           "πληροφορίες βιβλιοθήκης"),
        ("Email επικοινωνίας σχολής",          "email επικοινωνίας σχολής"),
        ("Πληροφορίες κάρτας ISIC",            "isic card πληροφορίες"),
        ("Πού ανακοινώνονται οι βαθμοί;",     "moodle βαθμοί"),
        ("Πότε είναι η εξεταστική περίοδος;",  "εξεταστική περίοδος"),
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("UniChat")
        self.root.geometry("1050x780")
        self.root.minsize(850, 600)

        self.dark_mode = True
        self.t = DARK
        self.sidebar_open = False
        self._bubble_refs = []
        self._quick_btns = []

        self.root.configure(bg=self.t["bg"])
        self._build_ui()
        self._add_bot_bubble("Γεια σου! Είμαι το UniChat.\nΠώς μπορώ να σε βοηθήσω;")

    # ── BUILD ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        self._build_topbar()
        self._build_body()
        self._build_input()      # pack input first → sits at very bottom
        self._build_quick_bar()  # pack quick bar above input

    def _build_topbar(self):
        self.topbar = tk.Frame(self.root, bg=self.t["topbar"], height=56)
        self.topbar.pack(fill="x", side="top")
        self.topbar.pack_propagate(False)

        self.menu_btn = tk.Button(
            self.topbar, text="☰", font=("Segoe UI", 18),
            bg=self.t["topbar"], fg=self.t["title_fg"],
            activebackground=self.t["divider"],
            activeforeground=self.t["title_fg"],
            relief="flat", cursor="hand2",
            command=self.toggle_sidebar, bd=0, padx=16
        )
        self.menu_btn.pack(side="left")

        self.title_lbl = tk.Label(
            self.topbar, text="UniChat",
            font=("Segoe UI", 14, "bold"),
            bg=self.t["topbar"], fg=self.t["title_fg"]
        )
        self.title_lbl.pack(side="left", padx=6)

        self.toggle_btn = tk.Button(
            self.topbar, text=self.t["toggle"],
            font=("Segoe UI", 18),
            bg=self.t["topbar"], fg=self.t["title_fg"],
            activebackground=self.t["divider"],
            activeforeground=self.t["title_fg"],
            relief="flat", cursor="hand2",
            command=self.toggle_theme, bd=0, padx=16
        )
        self.toggle_btn.pack(side="right")

        self.topbar_sep = tk.Frame(self.root, bg=self.t["divider"], height=1)
        self.topbar_sep.pack(fill="x", side="top")

    def _build_body(self):
        self.body = tk.Frame(self.root, bg=self.t["bg"])
        self.body.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self.body, bg=self.t["sidebar_bg"], width=240)

        self.chat_frame = tk.Frame(self.body, bg=self.t["chat_bg"])
        self.chat_frame.pack(fill="both", expand=True, side="left")

        self.canvas = tk.Canvas(
            self.chat_frame, bg=self.t["chat_bg"], highlightthickness=0
        )
        self.scrollbar = tk.Scrollbar(
            self.chat_frame, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.bubbles_frame = tk.Frame(self.canvas, bg=self.t["chat_bg"])
        self._cw = self.canvas.create_window((0, 0), window=self.bubbles_frame, anchor="nw")

        self.canvas.bind("<Configure>", self._on_resize)
        self.bubbles_frame.bind("<Configure>", self._on_frame_config)
        self.canvas.bind_all("<MouseWheel>", self._on_scroll)

        self._build_sidebar_contents()

    def _build_sidebar_contents(self):
        t = self.t
        for w in self.sidebar.winfo_children():
            w.destroy()
        self.sidebar.configure(bg=t["sidebar_bg"])

        tk.Label(
            self.sidebar, text="  Menu",
            font=("Segoe UI", 12, "bold"),
            bg=t["sidebar_bg"], fg=t["sidebar_fg"],
            pady=16, anchor="w"
        ).pack(fill="x", padx=8)

        tk.Frame(self.sidebar, bg=t["divider"], height=1).pack(fill="x", padx=10)

        for label, cmd in [("+  Νέα Συνομιλία", self.new_chat),
                            ("×  Καθαρισμός Chat", self.clear_chat)]:
            tk.Button(
                self.sidebar, text=label, font=("Segoe UI", 10),
                bg=t["sidebar_btn"], fg=t["sidebar_bfg"],
                activebackground=t["divider"], activeforeground=t["sidebar_bfg"],
                relief="flat", cursor="hand2",
                anchor="w", padx=16, pady=9, command=cmd
            ).pack(fill="x", padx=10, pady=3)

        tk.Frame(self.sidebar, bg=t["divider"], height=1).pack(fill="x", padx=10, pady=8)

        tk.Label(
            self.sidebar, text="  Γρήγορες Ερωτήσεις",
            font=("Segoe UI", 9, "bold"),
            bg=t["sidebar_bg"], fg=t["quick_accent"],
            anchor="w", pady=2
        ).pack(fill="x", padx=8, pady=4)

        for label, query in self.FAQ_ITEMS:
            tk.Button(
                self.sidebar, text=label, font=("Segoe UI", 9),
                bg=t["sidebar_btn"], fg=t["sidebar_bfg"],
                activebackground=t["divider"], activeforeground=t["sidebar_bfg"],
                relief="flat", cursor="hand2",
                anchor="w", padx=16, pady=7,
                wraplength=200, justify="left",
                command=lambda q=query: self._faq_click(q)
            ).pack(fill="x", padx=10, pady=2)

    def _build_input(self):
        # Packed first → sits at the very bottom of root
        self.input_bar = tk.Frame(self.root, bg=self.t["topbar"], padx=16, pady=12)
        self.input_bar.pack(fill="x", side="bottom")

        self.input_sep = tk.Frame(self.root, bg=self.t["divider"], height=1)
        self.input_sep.pack(fill="x", side="bottom")

        # Entry with 1px border container
        self.entry_container = tk.Frame(
            self.input_bar, bg=self.t["input_border"], padx=1, pady=1
        )
        self.entry_container.pack(side="left", fill="x", expand=True, padx=(0, 12))

        self.entry_inner = tk.Frame(self.entry_container, bg=self.t["input_bg"])
        self.entry_inner.pack(fill="both", expand=True)

        self.entry = tk.Entry(
            self.entry_inner, font=("Segoe UI", 11),
            bg=self.t["input_bg"], fg=self.t["input_fg"],
            insertbackground=self.t["input_fg"],
            relief="flat", bd=0
        )
        self.entry.pack(fill="x", expand=True, ipady=10, padx=14)
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_btn = tk.Button(
            self.input_bar, text="  Αποστολή  ➤",
            font=("Segoe UI", 10, "bold"),
            bg=self.t["send_bg"], fg=self.t["send_fg"],
            activebackground="#8e1f1f",
            activeforeground="#ffffff",
            relief="flat", cursor="hand2",
            command=self.send_message, padx=18, pady=10, bd=0
        )
        self.send_btn.pack(side="right")

    def _build_quick_bar(self):
        # Packed after input → sits above input bar
        self.quick_bar = tk.Frame(self.root, bg=self.t["topbar"], pady=10)
        self.quick_bar.pack(fill="x", side="bottom")

        self.quick_sep = tk.Frame(self.root, bg=self.t["divider"], height=1)
        self.quick_sep.pack(fill="x", side="bottom")

        self.quick_inner = tk.Frame(self.quick_bar, bg=self.t["topbar"])
        self.quick_inner.pack()

        self._quick_btns = []
        for label, query in QUICK_ACTIONS:
            btn = tk.Button(
                self.quick_inner, text=label,
                font=("Segoe UI", 9),
                bg=self.t["quick_bg"], fg=self.t["quick_fg"],
                activebackground=self.t["divider"],
                activeforeground=self.t["quick_fg"],
                relief="flat", cursor="hand2",
                padx=16, pady=7, bd=0,
                command=lambda q=query: self.send_message(q)
            )
            btn.pack(side="left", padx=6)
            self._quick_btns.append(btn)

    # ── CANVAS HELPERS ────────────────────────────────────────────────────

    def _on_resize(self, event):
        self.canvas.itemconfig(self._cw, width=event.width)

    def _on_frame_config(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_scroll(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _scroll_bottom(self):
        self.root.after(60, lambda: self.canvas.yview_moveto(1.0))

    # ── SIDEBAR ───────────────────────────────────────────────────────────

    def toggle_sidebar(self):
        if self.sidebar_open:
            self.sidebar.pack_forget()
            self.sidebar_open = False
        else:
            self.sidebar.pack(side="left", fill="y", before=self.chat_frame)
            self.sidebar_open = True

    # ── THEME ─────────────────────────────────────────────────────────────

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.t = DARK if self.dark_mode else LIGHT
        self._apply_theme()

    def _apply_theme(self):
        t = self.t
        self.root.configure(bg=t["bg"])
        self.topbar.configure(bg=t["topbar"])
        self.topbar_sep.configure(bg=t["divider"])
        self.menu_btn.configure(bg=t["topbar"], fg=t["title_fg"],
                                activebackground=t["divider"])
        self.title_lbl.configure(bg=t["topbar"], fg=t["title_fg"])
        self.toggle_btn.configure(bg=t["topbar"], fg=t["title_fg"],
                                  text=t["toggle"], activebackground=t["divider"])
        self.body.configure(bg=t["bg"])
        self.chat_frame.configure(bg=t["chat_bg"])
        self.canvas.configure(bg=t["chat_bg"])
        self.bubbles_frame.configure(bg=t["chat_bg"])
        self.quick_sep.configure(bg=t["divider"])
        self.quick_bar.configure(bg=t["topbar"])
        self.quick_inner.configure(bg=t["topbar"])
        for btn in self._quick_btns:
            btn.configure(bg=t["quick_bg"], fg=t["quick_fg"],
                          activebackground=t["divider"])
        self.input_sep.configure(bg=t["divider"])
        self.input_bar.configure(bg=t["topbar"])
        self.entry_container.configure(bg=t["input_border"])
        self.entry_inner.configure(bg=t["input_bg"])
        self.entry.configure(bg=t["input_bg"], fg=t["input_fg"],
                             insertbackground=t["input_fg"])
        self.send_btn.configure(bg=t["send_bg"], fg=t["send_fg"])
        self._build_sidebar_contents()

        for outer, bubble, kind in self._bubble_refs:
            try:
                b_bg = t["user_bubble"] if kind == "user" else t["bot_bubble"]
                b_fg = t["user_fg"]     if kind == "user" else t["bot_fg"]
                t_fg = t["user_time"]   if kind == "user" else t["bot_time"]
                outer.configure(bg=t["chat_bg"])
                bubble.configure(bg=b_bg)
                children = list(bubble.winfo_children())
                if not children:
                    continue
                # Last child is always the timestamp Label
                children[-1].configure(bg=b_bg, fg=t_fg)
                # First child is the message: Text for bot, Label for user
                first = children[0]
                if isinstance(first, tk.Text):
                    first.config(state="normal")
                    first.configure(bg=b_bg, fg=b_fg)
                    first.config(state="disabled")
                elif isinstance(first, tk.Label):
                    first.configure(bg=b_bg, fg=b_fg)
            except tk.TclError:
                pass

    # ── MESSAGING ─────────────────────────────────────────────────────────

    def send_message(self, text=None):
        msg = text if text else self.entry.get().strip()
        if not msg:
            return
        self.entry.delete(0, "end")
        self._add_user_bubble(msg)
        self._show_typing()
        self.root.after(1000, lambda: self._deliver(msg))

    def _faq_click(self, query):
        if self.sidebar_open:
            self.toggle_sidebar()
        self.send_message(query)

    def _deliver(self, msg):
        self._hide_typing()
        response = get_response(msg)
        if "\n__MAPLINK__:" in response:
            text, url = response.split("\n__MAPLINK__:", 1)
            self._add_bot_bubble_with_link(text, url)
        else:
            self._add_bot_bubble(response)

    def _add_user_bubble(self, text):
        t = self.t
        now = datetime.now().strftime("%H:%M")

        outer = tk.Frame(self.bubbles_frame, bg=t["chat_bg"])
        outer.pack(fill="x", pady=6, padx=18)

        bubble = tk.Frame(outer, bg=t["user_bubble"])
        bubble.pack(side="right")

        tk.Label(
            bubble, text=text, font=("Segoe UI", 10),
            bg=t["user_bubble"], fg=t["user_fg"],
            wraplength=320, justify="left", padx=14, pady=10
        ).pack(anchor="w")

        tk.Label(
            bubble, text=now, font=("Segoe UI", 8),
            bg=t["user_bubble"], fg=t["user_time"],
            padx=12, pady=5
        ).pack(anchor="e")

        self._bubble_refs.append((outer, bubble, "user"))
        self._scroll_bottom()

    def _add_bot_bubble(self, text):
        t = self.t
        now = datetime.now().strftime("%H:%M")

        outer = tk.Frame(self.bubbles_frame, bg=t["chat_bg"])
        outer.pack(fill="x", pady=6, padx=18)

        bubble = tk.Frame(outer, bg=t["bot_bubble"])
        bubble.pack(side="left")

        msg = tk.Text(
            bubble, font=("Segoe UI", 10),
            bg=t["bot_bubble"], fg=t["bot_fg"],
            relief="flat", bd=0, highlightthickness=0,
            wrap="word", cursor="xterm",
            width=52, height=text.count('\n') + 1,
            padx=14, pady=10,
            selectbackground="#4a90d9", selectforeground="#ffffff",
        )
        msg.insert("1.0", text)
        msg.config(state="disabled")
        msg.pack(anchor="w")

        tk.Label(
            bubble, text=now, font=("Segoe UI", 8),
            bg=t["bot_bubble"], fg=t["bot_time"],
            padx=12, pady=5
        ).pack(anchor="w")

        self._bubble_refs.append((outer, bubble, "bot"))
        self._scroll_bottom()

    def _add_bot_bubble_with_link(self, text, url):
        t = self.t
        now = datetime.now().strftime("%H:%M")

        outer = tk.Frame(self.bubbles_frame, bg=t["chat_bg"])
        outer.pack(fill="x", pady=6, padx=18)

        bubble = tk.Frame(outer, bg=t["bot_bubble"])
        bubble.pack(side="left")

        msg = tk.Text(
            bubble, font=("Segoe UI", 10),
            bg=t["bot_bubble"], fg=t["bot_fg"],
            relief="flat", bd=0, highlightthickness=0,
            wrap="word", cursor="xterm",
            width=52, height=text.count('\n') + 1,
            padx=14, pady=10,
            selectbackground="#4a90d9", selectforeground="#ffffff",
        )
        msg.insert("1.0", text)
        msg.config(state="disabled")
        msg.pack(anchor="w")

        tk.Button(
            bubble, text="↗  Άνοιγμα Τοποθεσίας",
            font=("Segoe UI", 9, "bold"),
            bg=t["quick_accent"], fg="#ffffff",
            activebackground="#8e1f1f", activeforeground="#ffffff",
            relief="flat", cursor="hand2",
            padx=12, bd=0,
            command=lambda u=url: webbrowser.open(u)
        ).pack(anchor="w", padx=14, pady=(0, 8))

        tk.Label(
            bubble, text=now, font=("Segoe UI", 8),
            bg=t["bot_bubble"], fg=t["bot_time"],
            padx=12, pady=5
        ).pack(anchor="w")

        self._bubble_refs.append((outer, bubble, "bot"))
        self._scroll_bottom()

    # ── TYPING INDICATOR ──────────────────────────────────────────────────

    def _show_typing(self):
        t = self.t
        self._typing_outer = tk.Frame(self.bubbles_frame, bg=t["chat_bg"])
        self._typing_outer.pack(fill="x", pady=6, padx=18)

        self._typing_bubble = tk.Frame(self._typing_outer, bg=t["bot_bubble"])
        self._typing_bubble.pack(side="left")

        tk.Label(
            self._typing_bubble,
            text="●  UniChat πληκτρολογεί...",
            font=("Segoe UI", 9, "italic"),
            bg=t["bot_bubble"], fg=t["bot_time"],
            padx=14, pady=10
        ).pack()
        self._scroll_bottom()

    def _hide_typing(self):
        try:
            self._typing_outer.destroy()
        except AttributeError:
            pass

    # ── ACTIONS ───────────────────────────────────────────────────────────

    def clear_chat(self):
        for w in self.bubbles_frame.winfo_children():
            w.destroy()
        self._bubble_refs.clear()
        self._add_bot_bubble("Γεια σου! Είμαι το UniChat.\nΠώς μπορώ να σε βοηθήσω;")

    def new_chat(self):
        if self.sidebar_open:
            self.toggle_sidebar()
        self.clear_chat()


# ─── ENTRY POINT ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    if sys.platform == "win32":
        try:
            dpi = root.winfo_fpixels('1i')
            root.tk.call('tk', 'scaling', dpi / 72.0)
        except Exception:
            pass
    app = UniChatApp(root)
    root.mainloop()
