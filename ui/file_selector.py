"""Drop zone + Browse button + selected-files label, bundled as one
self-contained component. Keeps its own selection state instead of relying
on a module-level global.
"""
import os
from tkinter import filedialog

import customtkinter as ctk
from tkinterdnd2 import DND_FILES

import config


class FileSelector(ctk.CTkFrame):
    """A panel for picking input files, either by dragging them onto the
    drop zone or via the Browse button."""

    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self._selected_files = []

        self.drop_frame = ctk.CTkFrame(
            self,
            width=700,
            height=250,
            corner_radius=15,
            border_width=2,
            border_color=config.DROP_ZONE_DEFAULT_BORDER
        )
        self.drop_frame.pack(pady=20)
        self.drop_frame.pack_propagate(False)

        self.drop_label = ctk.CTkLabel(
            self.drop_frame,
            text="📂\n\nDrag & Drop Files Here\n\nor",
            font=("Arial", 20)
        )
        self.drop_label.pack(expand=True)

        self.selected_files_label = ctk.CTkLabel(self, text="No files selected")
        self.selected_files_label.pack(pady=10)

        self.browse_btn = ctk.CTkButton(self, text="Browse Files", command=self._browse_files)
        self.browse_btn.pack(pady=10)

        self._register_drop_targets()

    # ---------- public API ----------

    def get_selected_files(self):
        return list(self._selected_files)

    # ---------- internals ----------

    def _register_drop_targets(self):
        # Register both the frame and the label — the label sits on top of
        # the frame, so without registering it too, drops on the visible
        # icon/text would be silently ignored.
        for widget in (self.drop_frame, self.drop_label):
            widget.drop_target_register(DND_FILES)
            widget.dnd_bind("<<Drop>>", self._on_drop)
            widget.dnd_bind("<<DropEnter>>", self._on_drag_enter)
            widget.dnd_bind("<<DropLeave>>", self._on_drag_leave)

    def _browse_files(self):
        files = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=[
                ("Supported Files", "*.pdf *.jpg *.jpeg *.png *.webp"),
                ("All Files", "*.*")
            ]
        )
        if files:
            self._set_selected(list(files))

    def _on_drop(self, event):
        # tkinterdnd2 returns a single string; paths with spaces are wrapped
        # in {curly braces}, which tk's splitlist() parses correctly.
        paths = self.tk.splitlist(event.data)

        valid = [p for p in paths if os.path.isfile(p) and p.lower().endswith(config.SUPPORTED_EXTS)]
        skipped = [p for p in paths if p not in valid]

        if valid:
            self._set_selected(valid)
        if skipped:
            print(f"Skipped unsupported file(s): {skipped}")

        self._on_drag_leave(event)

    def _on_drag_enter(self, event):
        self.drop_frame.configure(border_color=config.DROP_ZONE_ACTIVE_BORDER)

    def _on_drag_leave(self, event):
        self.drop_frame.configure(border_color=config.DROP_ZONE_DEFAULT_BORDER)

    def _set_selected(self, files):
        self._selected_files = files
        self.selected_files_label.configure(text=f"{len(files)} file(s) selected")
        print(self._selected_files)
