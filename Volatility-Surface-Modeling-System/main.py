
from pathlib import Path
import subprocess
import sys

print("Launching Volatility Surface Modeling System dashboard...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
