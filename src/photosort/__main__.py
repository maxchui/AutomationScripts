"""Allow running the package with ``python -m photosort``."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
