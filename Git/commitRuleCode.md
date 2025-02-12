#!/bin/sh

# Get commit message
COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Define TASK ID pattern (e.g., ABC-123)
Regex_PATTERN="([A-Z]+-[0-9]+)"

# Define minimum commit message length (excluding TASK ID)
MIN_MSG_LENGTH=20

# Extract commit message without TASK ID
COMMIT_MSG_CLEANED=$(echo "$COMMIT_MSG" | sed -E "s/$Regex_PATTERN//")

# Check if commit message contains a TASK ID
if ! [[ "$COMMIT_MSG" =~ $Regex_PATTERN ]]; then
    echo "❌ ERROR: Commit message must include a TASK ID (e.g., ABC-123)."
    echo "✅ FIX: Use 'git commit --amend' to update your commit message."
    exit 1  # Block commit
fi

# Check if commit message length (excluding TASK ID) is at least 20 characters
if [[ ${#COMMIT_MSG_CLEANED} -lt $MIN_MSG_LENGTH ]]; then
    echo "❌ ERROR: Commit message must be at least $MIN_MSG_LENGTH characters long (excluding TASK ID)."
    echo "✅ FIX: Use 'git commit --amend' to update your commit message."
    exit 1  # Block commit
fi

echo "✅ Commit message meets all requirements. Proceeding..."
exit 0  # Allow commit
