# UniChat — Student Support Chatbot

**UniChat** is a rule-based chatbot developed in Python to support students of an academic institution by providing immediate answers to frequently asked questions. It is available in two versions: a terminal (CLI) version and a full graphical desktop application (GUI).

---

## Project Structure

```
chatbot_project/
│
├── chatbot.py          # Terminal (CLI) version — no GUI required
├── chatbot_gui.py      # Full graphical version with Tkinter GUI
├── README.md           # This file
├── .gitignore          # Excludes .vscode/, .claude/, __pycache__/, *.pyc
├── .vscode/            # VS Code project settings
└── .git/               # Git version control internals
```

**Total lines of code:** 792 (chatbot.py: 116 | chatbot_gui.py: 676)

---

## Requirements

| Requirement | Details |
|---|---|
| Python version | Python 3.x (any modern version) |
| External packages | **None** — standard library only |
| OS compatibility | Windows (primary), macOS, Linux |
| Tkinter | Bundled with Python on Windows. On Linux: `sudo apt install python3-tk` |

No virtual environment, no `requirements.txt`, no installation steps needed.

---

## How to Run

### Terminal version (CLI)
```bash
python chatbot.py
```

### Graphical version (GUI)
```bash
python chatbot_gui.py
```

Both commands must be run from inside the `chatbot_project/` directory.

---

## Features

### Terminal Version (`chatbot.py`)
- Reads user input from the console and prints responses
- Recognises 11 question topics in Greek and English
- Handles unrecognised queries with a friendly fallback message
- Exit by typing: `exit`, `τελος`, or `αντιο`

### Graphical Version (`chatbot_gui.py`)
- Modern chat bubble interface (similar to WhatsApp / Messenger)
- **Dark / Light theme** toggle (☾ / ☀) with full dynamic re-colouring
- **Sidebar** with 6 FAQ quick-buttons and chat management options
- **Quick-action bar** with 3 instant-access buttons
- **Typing indicator** ("● UniChat πληκτρολογεί...") for natural interaction feel
- **Copyable bot responses** (selectable text, Ctrl+C to copy)
- **Interactive Google Maps button** for the location query
- **Timestamps** (HH:MM) on every message bubble
- **HiDPI / High-resolution display support** on Windows

---

## Supported Topics

The chatbot recognises 11 question categories:

| # | Topic | Example keywords |
|---|---|---|
| 1 | Secretary phone number | τηλέφωνο, τηλεφωνο |
| 2 | Secretary office hours | ώρες + γραμματ, ωρες + γραμματ |
| 3 | University location / address | πού, που, διεύθυνση, location, maps, address |
| 4 | Contact email | email, mail, μειλ, επικοινωνία |
| 5 | Exam period | εξεταστική, εξεταστικη, exams, εξετάσεις |
| 6 | Grades / Moodle | βαθμοί, βαθμοι, grades, αποτελέσματα, moodle |
| 7 | Course registration | εγγραφές, εγγραφες, registration, enroll |
| 8 | Library | βιβλιοθήκη, βιβλιοθηκη, library, βιβλία |
| 9 | ISIC student card | isic, card, κάρτα, student card |
| 10 | Winter courses | χειμερινά, χειμερινα, μαθήματα, winter, courses |
| 11 | Tuition discount | έκπτωση, εκπτωση, discount, δίδακτρα, προσφορά |

Both toned (with accent) and un-toned Greek variants are supported, as well as English equivalents.

---

## Dependencies

All imports are from the **Python standard library**. No `pip install` required.

| Library | Used in | Purpose |
|---|---|---|
| `tkinter` | `chatbot_gui.py` | Entire GUI — windows, frames, buttons, canvas, entry |
| `datetime` | `chatbot_gui.py` | Message timestamps (HH:MM format) |
| `webbrowser` | `chatbot_gui.py` | Opens Google Maps link in default browser |
| `ctypes` | `chatbot_gui.py` | Windows HiDPI awareness (`SetProcessDpiAwareness`) |
| `sys` | `chatbot_gui.py` | OS detection (`sys.platform`) |
| *(none)* | `chatbot.py` | Pure Python built-ins only |

---

## How It Works

### Processing Flow
1. **User input** — typed text or quick-button click
2. **Preprocessing** — converted to lowercase with `.lower()`
3. **Intent recognition** — `get_response()` checks `if/elif` conditions for keyword matches
4. **Response generation** — returns predefined answer or fallback message
5. **Display** — printed to terminal or shown as a styled chat bubble

### Google Maps Button
When the location topic is detected, `get_response()` returns a special string containing an internal `__MAPLINK__:` marker with the URL. The GUI detects this marker, separates the display text from the URL, and renders a clickable "↗ Άνοιγμα Τοποθεσίας" button inside the response bubble.

---

## GUI Window Details

| Property | Value |
|---|---|
| Default window size | 1050 × 780 pixels |
| Minimum window size | 850 × 600 pixels |
| Window title | UniChat |
| Default theme | Dark |
| Sidebar width | 240 pixels |

---

## Version History

| Commit | Description |
|---|---|
| `657beaf` | Add explanatory comments to UniChat code |
| `1afe1ff` | Adjust UniChat GUI startup window size |
| `ab4164a` | Improve UniChat GUI with copyable bot messages |
| `ac124b6` | Add polished UniChat GUI with theme toggle and Maps button |
| `3a6b53b` | Refactor UniChat into functions and improve Python entry point |
| `7142ba2` | Add ISIC card, winter courses, and tuition discount support |
| `8e52ae8` | Add grades, registrations, and library support |
| `4f5b918` | Add location with Maps link, update school email, add exam period support |
| `243a29a` | Merge remote README |
| `aac6c87` | Initial commit: UniChat first version |

---

## Author

**Alexandru Sacara Marian**
Student ID: 2678458
School of Architecture Computing and Engineering
Metropolitan College — University of East London
Academic Year 2025–2026

Supervisor: Spentzas Dimitrios
Course: CN6000_1 — Mental Wealth Professional Life 3
