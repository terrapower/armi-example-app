"""Application module"""

from armi.apps import App

from myapp.plugin import DummyPhysicsPlugin


class ExampleApp(App):
    def __init__(self):
        # activate all built-in plugins
        App.__init__(self)

        # (optionally) set the name class attribute
        name = "example-app"

        # register our plugin with the plugin manager
        self._pm.register(DummyPhysicsPlugin)

    @property
    def splashText(self):
        return "** My Example App **"
