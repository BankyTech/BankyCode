```
stages:
  - cherry-pick
  - merge

cherry-pick-release-2:
  stage: cherry-pick
  script:
    - |
      set -e  # Exit on any error
      echo "🚀 Fetching latest merge commit from release-1..."
      echo "🔍 Debugging Variables..."
      echo "CI_JOB_TOKEN length: ${#CI_JOB_TOKEN} characters"
      echo "CI_PROJECT_PATH: ${CI_PROJECT_PATH}"
      echo "GITLAB_PAT length: ${#GITLAB_PAT} characters"
      if [[ -z "${GITLAB_PAT}" ]]; then
        echo "❌ ERROR: GITLAB_PAT is not set"
        exit 1
      fi
    - git config --global user.name "GitLab AutoMerge Bot"
    - git config --global user.email "gitlab-bot@example.com"
    - git fetch --all
    - |
      git checkout release-2 || git checkout -b release-2 origin/release-2
    - |
      MR_MERGE_COMMIT=$(git log --merges --oneline -n 1 origin/release-1 | awk '{print $1}')
      echo "Merge commit: ${MR_MERGE_COMMIT}"
      if [[ -z "${MR_MERGE_COMMIT}" ]]; then
        echo "❌ ERROR: No merge commit found"
        exit 1
      fi
    - |
      git cherry-pick -x -m 1 "${MR_MERGE_COMMIT}" || (echo "🚨 Conflict detected! Manual intervention needed." && exit 1)
    - echo "🔑 Setting up authentication for Git push..."
    - |
      git remote set-url origin "https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.com/${CI_PROJECT_PATH}.git"
    - |
      git push origin release-2 || (echo "❌ ERROR: Push to release-2 failed!" && exit 1)
  only:
    refs:
      - release-1

merge-release-2-to-release-3:
  stage: merge
  script:
    - |
      set -e
      echo "🚀 Merging release-2 into release-3..."
    - git fetch --all
    - |
      git checkout release-3 || git checkout -b release-3 origin/release-3
    - |
      git merge --no-ff release-2 || (echo "🚨 Merge conflict detected! Manual intervention required." && exit 1)
    - echo "🔑 Setting up authentication for Git push..."
    - |
      git remote set-url origin "https://${GITLAB_PAT}@gitlab.com/${CI_PROJECT_PATH}.git"
    - |
      git push origin release-3 || (echo "❌ ERROR: Push to release-3 failed!" && exit 1)
  only:
    refs:
      - release-2
```
