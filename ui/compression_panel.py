"""Quality slider + progress bar + Compress button, bundled as one
self-contained component."""
import customtkinter as ctk

import config


class CompressionPanel(ctk.CTkFrame):
    def __init__(self, master, on_compress, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.quality_label = ctk.CTkLabel(self, text="Compression Quality")
        self.quality_label.pack()

        self.quality_slider = ctk.CTkSlider(self, from_=10, to=100)
        self.quality_slider.set(config.DEFAULT_QUALITY)
        self.quality_slider.pack(fill="x", padx=80, pady=10)

        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=80, pady=20)
        self.progress.set(0)

        self.compress_btn = ctk.CTkButton(self, text="Compress", command=on_compress)
        self.compress_btn.pack(pady=20)

    def get_quality(self) -> int:
        return int(self.quality_slider.get())

    def set_progress(self, value: float):
        self.progress.set(value)
