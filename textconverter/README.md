# TextConverter
Unified decoding for URL-encoded, hex-escaped, and HTML text.

## Install
```bash
pip install textconverter
```

## Usage
```python
from textconverter import decode_all
print(decode_all("%22\\x22Hello\\x22%22"))  # Outputs: "Hello"
```

## CLI
```bash
textconverter "%22\\x22Hi\\x22%22"
# Output: "Hi"
```