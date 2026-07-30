"""Secure File Compressor — entry point.

This file only wires things together: build the window, drop in the two
panels, and connect the Compress button to the compression logic. See
ui/ for the widgets and core/compressor.py for the actual compression work.
"""
import customtkinter as ctk

import config
from ui.dnd_root import DnDCTk
from ui.file_selector import FileSelector
from ui.compression_panel import CompressionPanel
from core.compressor import compress_file


def run_compression():
    files = file_selector.get_selected_files()
    if not files:
        print("No files selected")
        return

    quality = compression_panel.get_quality()
    total = len(files)

    for index, path in enumerate(files, start=1):
        output = compress_file(path, quality=quality)
        if output:
            print(f"Compressed → {output}")
        else:
            print(f"Unsupported file: {path}")

        compression_panel.set_progress(index / total)


ctk.set_appearance_mode(config.APPEARANCE_MODE)
ctk.set_default_color_theme(config.COLOR_THEME)

app = DnDCTk()
app.title(config.WINDOW_TITLE)
app.geometry(config.WINDOW_SIZE)

title = ctk.CTkLabel(app, text=config.WINDOW_TITLE, font=("Arial", 28, "bold"))
title.pack(pady=20)

file_selector = FileSelector(app)
file_selector.pack()

compression_panel = CompressionPanel(app, on_compress=run_compression)
compression_panel.pack(fill="x")

app.mainloop()
