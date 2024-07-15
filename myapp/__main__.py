"""
Main module for example app.

Code here runs whenever you run this application.
"""
# FYI: The "tutorial-" comments are used in documentation building
# for `making_your_first_app.rst` in ARMI documentation.
# (That's also why the imports aren't all at the top)

# ruff: noqa: E402

# tutorial-configure-start
import armi

from myapp import app

armi.configure(app.ExampleApp())
# tutorial-configure-end

# tutorial-material-start
from armi import materials

materials.setMaterialNamespaceOrder(["myapp.materials", "armi.materials"])
# tutorial-material-end

# tutorial-entry-point-start
import sys
from armi.cli import ArmiCLI


def main():
    code = ArmiCLI().run()
    sys.exit(code)


if __name__ == "__main__":
    main()
# tutorial-entry-point-end
