#!/bin/bash
#
# Install the "Sort Photos with PhotoSort" Finder Quick Action.
#
# After running this, right-click a folder in Finder and choose
#   Quick Actions > Sort Photos with PhotoSort
# to sort its contents in place.
#
set -euo pipefail

SERVICE_NAME="Sort Photos with PhotoSort"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="${SCRIPT_DIR}/${SERVICE_NAME}.workflow"
DEST_DIR="${HOME}/Library/Services"
DEST="${DEST_DIR}/${SERVICE_NAME}.workflow"

# Locate the photosort executable so Finder (which runs with a minimal PATH)
# can call it by absolute path.
PHOTOSORT_BIN="$(command -v photosort || true)"
if [ -z "${PHOTOSORT_BIN}" ]; then
	cat >&2 <<'EOF'
Error: 'photosort' was not found on your PATH.

Install it first, e.g. from the repository root:
    pip install -e .

Then re-run this script.
EOF
	exit 1
fi

echo "Using photosort at: ${PHOTOSORT_BIN}"

mkdir -p "${DEST_DIR}"
rm -rf "${DEST}"
cp -R "${SRC}" "${DEST}"

# Bake the resolved photosort path into the workflow's shell script.
WFLOW="${DEST}/Contents/document.wflow"
TMP="$(mktemp)"
sed "s#__PHOTOSORT_BIN__#${PHOTOSORT_BIN}#g" "${WFLOW}" > "${TMP}"
mv "${TMP}" "${WFLOW}"

# Ask the Services system to pick up the new action.
/System/Library/CoreServices/pbs -update >/dev/null 2>&1 || true

echo "Installed: ${DEST}"
echo
echo "Right-click any folder in Finder > Quick Actions > '${SERVICE_NAME}'."
echo "If it doesn't appear immediately, enable it under:"
echo "  System Settings > Keyboard > Keyboard Shortcuts > Services > Files and Folders,"
echo "or log out and back in."
