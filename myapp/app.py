"""Application module"""

from armi import __version__ as armi_version
from armi.apps import App

from myapp import __version__ as myapp_version
from myapp.plugin import DummyPhysicsPlugin


class ExampleApp(App):
    name = "example-app"

    def __init__(self):
        # activate all built-in plugins
        App.__init__(self)

        # register our plugin with the plugin manager
        self._pm.register(DummyPhysicsPlugin)

    @property
    def splashText(self):
        return f"""                           
+===============================================+
+                                               +
+                 |\/|   /|                     +
+                 |  |\//-||)|)                 +
+                     /    | |                  +
+                                               +
+                Version: {myapp_version}                 +
+                                               +
+-----------------------------------------------+
+    Powered by ARMI (R) -- Version: {armi_version}      +
+===============================================+
"""
