# Developer Notes

## 📝 Essential Git Commands

### First Time Setup (Initialize Repository)

```bash
# Initialize a new Git repository
git init

# Add all files to staging
git add .

# Make your first commit
git commit -m "Initial commit: Chat app template"

# Connect to a remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/your-repo-name.git

# Push to GitHub (first time)
git push -u origin main
```

### Daily Git Workflow

```bash
# Check what files have changed
git status

# Add all changed files
git add .
# Or add specific file(s)
git add filename.py
git add frontend/src/App.js

# Commit your changes with a message
git commit -m "Describe what you changed"

# Push changes to GitHub
git push

# Pull latest changes from GitHub
git pull
```

### Security Best Practices

1. ✅ Never commit `.env` file to git (add to `.gitignore`)
2. ✅ Use separate keys for dev/staging/production
3. ✅ Rotate keys periodically in Azure Portal
4. ✅ Use Key Vault for production deployments
5. ✅ Implement rate limiting and authentication
6. ✅ Monitor usage for unexpected spikes

### Helpful Tips

- **Commit often**: Make small commits with clear messages
- **Write good commit messages**: "Fixed login bug" is better than "fixed stuff"
- **Pull before you push**: Always pull latest changes before pushing yours
- **Use branches**: Create a new branch for each feature or fix

### Example Commit Messages

- `"Added user authentication to backend"`
- `"Updated chat UI with new colors"`
- `"Fixed AI response timeout issue"`
- `"Added README documentation"`

### Ignore Files

The `.gitignore` file is already configured to ignore:
- `.env` (environment variables with API keys - **CRITICAL for security!**)
- `node_modules/` (React dependencies)
- `__pycache__/` (Python cache)
- `venv/` (Python virtual environment)
- `frontend/build/` (React production builds)
- IDE files (`.vscode/`, `.idea/`, `*.swp`)
- OS files (`.DS_Store`, `Thumbs.db`) (`.vscode/`, `.idea/`, etc.)



## 📌 Project Structure Quick Reference

```
frontend/   → React app (UI)
backend/    → FastAPI server (API)
ai/         → AI logic (separate from API)
```
