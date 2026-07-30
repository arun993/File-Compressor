# Secure File Compressor

A simple desktop app (built with `customtkinter`) for compressing PDFs and images (`.jpg`, `.jpeg`, `.png`, `.webp`) — either by dragging files onto the window or browsing for them.

## Features

- Drag & drop or Browse to select files
- PDF compression via Ghostscript
- JPG / PNG / WEBP compression via Pillow
- Adjustable compression quality
- Progress bar while compressing

## Project Structure

```
secure_file_compressor/
├── app.py                    # Entry point
├── config.py                 # Constants (extensions, colors, window size, defaults)
├── requirements.txt
├── core/
│   └── compressor.py         # Compression logic
└── ui/
    ├── dnd_root.py            # Drag-and-drop window setup
    ├── file_selector.py       # Drop zone + Browse button
    └── compression_panel.py   # Quality slider + progress bar + Compress button
```

## Getting Started

These steps assume no prior setup — follow them in order.

### Step 1: Install Python

You need **Python 3.9 or newer**.

- **Windows / macOS**: download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it.
  - On Windows, tick **"Add Python to PATH"** during install.
- **Linux**: Python 3 usually comes preinstalled. Check with `python3 --version`; if missing, install it via your package manager (e.g. `sudo apt install python3 python3-pip` on Ubuntu/Debian).

Verify it worked:
```bash
python --version
# or on macOS/Linux if `python` isn't found:
python3 --version
```

### Step 2: Install Ghostscript (required for PDF compression)

The app shells out to a `gs` command to compress PDFs, so Ghostscript must be installed **separately** — it isn't a Python package and won't come from `requirements.txt`.

- **Windows**: download and install from [ghostscript.com/releases](https://www.ghostscript.com/releases/gsdnld.html).
- **macOS**: `brew install ghostscript`
- **Linux (Ubuntu/Debian)**: `sudo apt install ghostscript`

Verify it worked:
```bash
gs --version
```
If image compression is all you need right now, you can skip this step and come back to it later — only the PDF path depends on it.

### Step 3: Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

(Replace `<your-username>/<your-repo-name>` with your actual GitHub path.)

### Step 4: Create a virtual environment (recommended)

This keeps the project's dependencies separate from other Python projects on your machine.

```bash
python -m venv venv
```

Activate it:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

You'll know it worked if your terminal prompt now starts with `(venv)`.

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

This installs `customtkinter`, `Pillow`, and `tkinterdnd2`.

### Step 6: Run the app

```bash
python app.py
```

A window titled **"Secure File Compressor"** should open.

## Usage

1. Drag files onto the drop zone, or click **Browse Files** to pick them manually.
2. Adjust the **Compression Quality** slider (higher = better quality, larger file).
3. Click **Compress**.
4. Compressed files are saved next to the originals, with `_compressed` added to the filename (e.g. `photo.jpg` → `photo_compressed.jpg`).

## Troubleshooting

| Problem | Likely fix |
|---|---|
| `python: command not found` | Use `python3` instead, or reinstall Python with "Add to PATH" checked. |
| `gs: command not found` when compressing a PDF | Ghostscript isn't installed or isn't on your PATH — see Step 2. |
| Drag & drop does nothing | Make sure `tkinterdnd2` installed correctly (`pip install tkinterdnd2`); on Linux you may also need `sudo apt install python3-tk`. |
| `ModuleNotFoundError: No module named 'customtkinter'` | You're not in the virtual environment, or dependencies weren't installed — re-run Step 4 and Step 5. |

## Contributing

Issues and pull requests are welcome. Please keep new logic in the appropriate module (`core/` for compression logic, `ui/` for interface components) rather than adding it directly to `app.py`.

## License

This project is licensed under the MIT License.
