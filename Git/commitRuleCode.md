#!/bin/sh

# Get the last commit message from Git
COMMIT_MSG=$(git log -1 --pretty=%B)

# Define a required pattern (e.g., specific issue ID, task number, etc.)
REQUIRED_PATTERN="([A-Z]+-[0-9]+)"

# Define minimum commit message length (excluding required pattern)
MIN_MSG_LENGTH=20

# Extract commit message without required pattern
COMMIT_MSG_CLEANED=$(echo "$COMMIT_MSG" | sed -E "s/$REQUIRED_PATTERN//")

# Check if commit message contains the required pattern
if ! echo "$COMMIT_MSG" | grep -qE "$REQUIRED_PATTERN"; then
    echo "❌ ERROR: Commit message must include a required pattern (e.g., TASK-123)."
    echo "✅ FIX: Use 'git commit --amend' to update your commit message."
    exit 1  # Block commit
fi

# Check if commit message length (excluding required pattern) is at least MIN_MSG_LENGTH
if [ ${#COMMIT_MSG_CLEANED} -lt $MIN_MSG_LENGTH ]; then
    echo "❌ ERROR: Commit message must be at least $MIN_MSG_LENGTH characters long (excluding required pattern)."
    echo "✅ FIX: Use 'git commit --amend' to update your commit message."
    exit 1  # Block commit
fi

echo "✅ Commit message meets all requirements. Proceeding..."
exit 0  # Allow commit
