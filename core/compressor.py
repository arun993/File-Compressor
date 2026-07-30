"""Compression logic for each supported file type.

This module has no UI dependencies — it just takes a file path and returns
the path to the compressed output, so it can be tested or reused on its own.
"""
import os
import subprocess
from typing import Optional

from PIL import Image

from config import SUPPORTED_EXTS


def compress_pdf(path: str) -> str:
    output = path.replace(".pdf", "_compressed.pdf")

    subprocess.run([
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output}",
        path
    ])

    return output


def compress_image(path: str, quality: int = 75) -> str:
    ext = os.path.splitext(path)[1].lower()
    output = path[: -len(ext)] + "_compressed" + ext

    img = Image.open(path)
    save_kwargs = {"optimize": True}
    if ext in (".jpg", ".jpeg", ".webp"):
        save_kwargs["quality"] = quality

    img.save(output, **save_kwargs)
    return output


def compress_file(path: str, quality: int = 75) -> Optional[str]:
    """Dispatch to the right compressor based on file extension.

    Returns the output path, or None if the file type isn't supported.
    """
    ext = os.path.splitext(path)[1].lower()

    if ext not in SUPPORTED_EXTS:
        return None

    if ext == ".pdf":
        return compress_pdf(path)

    return compress_image(path, quality=quality)
