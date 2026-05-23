
from pathlib import Path
import subprocess
import sys

print("Launching Order Flow Imbalance Predictor dashboard...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
