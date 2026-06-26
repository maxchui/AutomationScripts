"""Command-line entry point for PhotoSort."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .sorter import setup_logging, sort_folder


def _pick_folder_with_dialog() -> str | None:
    """Show a folder picker dialog and return the chosen path, or None."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError:
        return None

    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select the folder to sort")
    root.destroy()
    return folder or None


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="photosort",
        description="Sort a folder of camera photos/videos into per-type subfolders "
        "(RAW, JPG, HIF, MP4).",
    )
    parser.add_argument(
        "folder",
        nargs="?",
        type=Path,
        help="Folder to sort. If omitted, a folder picker dialog is shown.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    folder = args.folder
    if folder is None:
        chosen = _pick_folder_with_dialog()
        if chosen is None:
            print("No folder selected. Exiting.", file=sys.stderr)
            return 1
        folder = Path(chosen)

    if not folder.is_dir():
        print(f"Not a directory: {folder}", file=sys.stderr)
        return 1

    setup_logging(folder)
    result = sort_folder(folder)
    return 0 if result.errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
