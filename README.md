# PhotoSort

A small command-line tool for tidying up photography file dumps. Point it at a
folder of mixed camera files and it sorts them into per-type subfolders so RAW,
JPEG, HEIF, and video files no longer live in one messy pile.

I shoot on a Sony A7 IV and save both lossless-compressed RAW (`ARW`) and
compressed HEIF (`HIF`). Separating those by hand after every shoot was tedious,
so this tool does it for me — and it recognises RAW formats from most other
camera brands too.

## Installation

```bash
pip install -e .
```

This installs a `photosort` command (Python 3.9+). No third-party dependencies
are required.

## Usage

Copy the files off your SD card into a local folder first, then run:

```bash
# Pass the folder directly...
photosort /path/to/photos

# ...or omit it to get a folder-picker dialog
photosort
```

You can also run it without installing:

```bash
python -m photosort /path/to/photos
```

The tool creates the relevant subfolders (`RAW`, `JPG`, `HIF`, `MP4`) and moves
each file into the one matching its extension. Unrecognised files are left
untouched. A timestamped log of every run is written to a `logs/` folder inside
the target directory.

### Right-click in Finder (macOS)

You can sort a folder straight from Finder via a Quick Action. After installing
the `photosort` command (above), run:

```bash
./integrations/macos/install.sh
```

Then right-click any folder in Finder and choose
**Quick Actions → Sort Photos with PhotoSort**. A notification appears when it
finishes. (If the action doesn't show up right away, enable it under *System
Settings → Keyboard → Keyboard Shortcuts → Services → Files and Folders*, or log
out and back in.)

To remove it:

```bash
./integrations/macos/uninstall.sh
```

## Supported file types

| Folder | Extensions |
| ------ | ---------- |
| `RAW`  | ARW, CR2, CR3, NEF, ORF, RW2, RAF, DNG, and many more |
| `JPG`  | JPG, JPEG |
| `HIF`  | HIF, HEIF, HEIC |
| `MP4`  | MP4, MOV |

The full mapping lives in [`src/photosort/constants.py`](src/photosort/constants.py).
To support a new format, add an `"EXT": "FOLDER"` entry there.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
