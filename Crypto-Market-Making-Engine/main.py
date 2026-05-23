
from pathlib import Path
import subprocess
import sys

print("Launching Crypto Market Making Engine dashboard...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
