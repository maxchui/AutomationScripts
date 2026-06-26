#!/bin/bash
#
# Remove the "Sort Photos with PhotoSort" Finder Quick Action.
#
set -euo pipefail

SERVICE_NAME="Sort Photos with PhotoSort"
DEST="${HOME}/Library/Services/${SERVICE_NAME}.workflow"

if [ -d "${DEST}" ]; then
	rm -rf "${DEST}"
	/System/Library/CoreServices/pbs -update >/dev/null 2>&1 || true
	echo "Removed: ${DEST}"
else
	echo "Nothing to remove (not installed at ${DEST})."
fi
