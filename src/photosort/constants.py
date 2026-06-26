"""Mapping of camera file extensions to their destination folders.

Extensions are compared case-insensitively (stored here uppercase, without the
leading dot). Add new formats by inserting an ``"EXT": "FOLDER"`` entry.
"""

EXTENSION_TO_FOLDER: dict[str, str] = {
    # RAW images
    "ARW": "RAW",  # Sony
    "RAW": "RAW",  # Sony
    "CR2": "RAW",  # Canon
    "CR3": "RAW",  # Canon
    "NEF": "RAW",  # Nikon
    "ORF": "RAW",  # Olympus
    "RW2": "RAW",  # Panasonic
    "RAF": "RAW",  # Fuji
    "SR2": "RAW",  # Sony
    "SRF": "RAW",  # Sony
    "DNG": "RAW",  # Adobe
    "PEF": "RAW",  # Pentax
    "MRW": "RAW",  # Minolta
    "KDC": "RAW",  # Kodak
    "3FR": "RAW",  # Hasselblad
    "FFF": "RAW",  # Imacon/Hasselblad
    "MEF": "RAW",  # Mamiya
    "ERF": "RAW",  # Epson
    "IIQ": "RAW",  # Phase One
    "MOS": "RAW",  # Leaf
    "NRW": "RAW",  # Nikon
    "PTX": "RAW",  # Pentax
    "R3D": "RAW",  # RED
    "X3F": "RAW",  # Sigma
    # Compressed images
    "JPG": "JPG",
    "JPEG": "JPG",
    "HIF": "HIF",
    "HEIF": "HIF",
    "HEIC": "HIF",
    # Videos
    "MP4": "MP4",
    "MOV": "MP4",
}
