import argparse
from .core import decode_all

def main():
    parser = argparse.ArgumentParser(description="Decode encoded text")
    parser.add_argument("text", help="Text to decode")
    args = parser.parse_args()
    print(decode_all(args.text))

if __name__ == "__main__":
    main()