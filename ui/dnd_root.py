"""Hybrid Tk root that supports both customtkinter's widgets/theming and
tkinterdnd2's drag-and-drop events. The two libraries don't combine directly,
so this small wrapper is the standard workaround.
"""
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD


class DnDCTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
