# Git Pre-Commit Hook Setup & Testing Guide

## 📌 Overview
This guide provides step-by-step instructions to configure and test a **pre-commit hook** in a local Git repository. The pre-commit hook will enforce commit message rules before allowing a commit.

---

## 🔹 Step 1: Navigate to Your Git Repository
Open **Command Prompt (cmd)** or **PowerShell** and navigate to your repository:

```sh
cd path/to/your-repo
```

---

## 🔹 Step 2: Create the Pre-Commit Hook
1. **Navigate to the `.git/hooks/` directory**:

   ```sh
   cd .git/hooks
   ```

2. **Create a new `pre-commit` file**:

   ```sh
   notepad pre-commit
   ```

3. **Paste the following script inside `pre-commit` and save it:**

   *(Modify it as needed to match your commit message rules)*

4. **Ensure the file is saved without a `.txt` extension**.

---

## 🔹 Step 3: Test the Pre-Commit Hook
### ✅ Expected Behavior
- **Valid commit** (with Task ID and proper length) → Commit succeeds.
- **Invalid commit** (missing Task ID or too short) → Commit fails.

### **Test Case 1: Invalid Commit (Should Be Blocked)**
```sh
git commit -m "Fixed a bug"
```
🚫 **Expected Output:**
> ❌ ERROR: Commit message must include a Task ID (e.g., ABC-123).

---

### **Test Case 2: Valid Commit (Should Be Allowed)**
```sh
git commit -m "ABC-123 Fixed login issue with session timeout"
```
✅ **Expected Output:**
> ✅ Commit message meets all requirements. Proceeding...

---

## 🔹 Step 4: Apply Hook to Another Repository
1. **Clone a new repository** or navigate to another Git project.
2. **Copy the `pre-commit` file into `.git/hooks/`**.
3. **Test by making a commit**.

✅ **The hook should work across different repositories!**

---

## 🔹 Step 5: Share the Hook with Other Developers
- **Ask developers to manually copy** `pre-commit` into their `.git/hooks/` folder.
- **Let them know:** This helps prevent invalid commits before pushing.

---

## 🚀 Next Steps
- If this works well, consider **automating the installation**.
- Gather feedback and **enhance enforcement rules** as needed.

🚀 **This setup ensures local enforcement without interfering with other repositories.**
