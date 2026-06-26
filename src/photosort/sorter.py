"""Core logic for sorting camera files into per-type folders."""

from __future__ import annotations

import logging
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .constants import EXTENSION_TO_FOLDER

logger = logging.getLogger(__name__)


@dataclass
class SortResult:
    """Summary of a sort run."""

    moved: int = 0
    skipped: int = 0
    errors: int = 0


def setup_logging(base_folder: Path) -> Path:
    """Configure logging to both the console and a timestamped log file.

    Returns the path to the created log file.
    """
    log_directory = base_folder / "logs"
    log_directory.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_directory / f"photosort_{timestamp}.log"
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        format="%(asctime)s %(levelname)s: %(message)s",
        force=True,
    )
    return log_file


def sort_folder(base_folder: Path) -> SortResult:
    """Move every recognised file in ``base_folder`` into a per-type subfolder.

    Files whose extension is not in :data:`EXTENSION_TO_FOLDER` are left in
    place and counted as skipped.
    """
    result = SortResult()

    files = [entry for entry in base_folder.iterdir() if entry.is_file()]
    if not files:
        logger.warning("No files found in %s; nothing to do.", base_folder)
        return result

    for entry in files:
        extension = entry.suffix[1:].upper()
        folder_name = EXTENSION_TO_FOLDER.get(extension)
        if folder_name is None:
            logger.info("Skipping %s (unrecognised extension '%s')", entry.name, extension)
            result.skipped += 1
            continue

        destination_folder = base_folder / folder_name
        destination_folder.mkdir(exist_ok=True)
        try:
            shutil.move(str(entry), str(destination_folder / entry.name))
            logger.debug("Moved %s -> %s/", entry.name, folder_name)
            result.moved += 1
        except OSError as exc:
            logger.error("Failed to move %s: %s", entry.name, exc)
            result.errors += 1

    logger.info(
        "Done: %d moved, %d skipped, %d errors.",
        result.moved,
        result.skipped,
        result.errors,
    )
    return result
