import sys

from armi.cli import ArmiCLI

if __name__ == "__main__":
    code = ArmiCLI().run()
    sys.exit(code)

