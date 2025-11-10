import sys
from main import main

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("Usage: python search.py <file_path> <method>")
        sys.exit(1)
    file_path = sys.argv[1].lower()
    algorithm = sys.argv[2].lower()
    main(file_path, algorithm, len(sys.argv))
