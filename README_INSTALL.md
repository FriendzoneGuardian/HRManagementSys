# Quick install instructions

Use the included `scripts/quick_install.py` to create a virtual environment and install required packages.

PowerShell (Windows):

```powershell
python .\scripts\quick_install.py
# for dev extras (if you have requirements-dev.txt):
python .\scripts\quick_install.py --dev

# Activate the venv:
. .\.venv\Scripts\Activate.ps1
# then run your app, e.g. `flask run` or your entrypoint
```

macOS / Linux (bash):

```bash
python3 ./scripts/quick_install.py
python3 ./scripts/quick_install.py --dev

source .venv/bin/activate
# then run your app, e.g. `flask run`
```

Notes:
- The script will create a `.venv` directory at the repository root if it doesn't exist.
- It installs packages from `requirements.txt`. Add a `requirements-dev.txt` for additional dev-only packages.
