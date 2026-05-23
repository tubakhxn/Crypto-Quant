
from pathlib import Path
import subprocess
import sys

print("Launching Market Regime Detection Engine dashboard...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
