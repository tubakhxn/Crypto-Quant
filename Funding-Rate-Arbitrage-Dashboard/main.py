
from pathlib import Path
import subprocess
import sys

print("Launching Funding Rate Arbitrage Dashboard dashboard...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
