import subprocess
import sys


def test_main_prints_hello():
    proc = subprocess.run(
        [sys.executable, "src/main.py"],
        capture_output=True,
        text=True
    )
    assert proc.returncode == 0
    assert "Hello from new-app" in proc.stdout
