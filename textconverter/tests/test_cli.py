import subprocess
from textconverter import __version__

def test_cli():
    result = subprocess.run(
        ["textconverter", "%22Hi%22"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == '"Hi"'

def test_version():
    result = subprocess.run(
        ["textconverter", "--version"],
        capture_output=True,
        text=True
    )
    assert __version__ in result.stdout