# Copyright 2019 TerraPower, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
ExampleApp class definition.

In this module, we define our ExampleApp class, which is responsible for most of the
customization that our example application applies to the base ARMI framework.
"""
import armi
from armi.apps import App

# For our example App, we will be pulling in the open-source Dragon plugin
from terrapower.physics.neutronics.dragon import DragonPlugin

class ExampleApp(App):
    """
    Our example App class.

    This should subclass the base App class from the ARMI framework. Since for now, the
    App class is pretty rudimentary, we can only do a couple of things:
     - Turn on plugins
     - Define a fancy splash screen for when our app is set up.

    Here, we do both.
    """
    def __init__(self):
        # For our app, we want access to all of the default ARMI plugins, so we call the
        # base __init__() function.
        App.__init__(self)

        # Now our object has a private instance attribute, called _pm, which is a
        # PluginManager that already has ARMI's basic plugins enabled. If we didn't want
        # any of these to be on, we could either turn them off.

        # To add our own plugin, we just need to register it with the plugin manager:
        self._pm.register(DragonPlugin)

    @property
    def splashText(self):
        return r"""
             ╔════════════════════════════════════════════════════╗
             ║       ______                           _           ║
             ║      |  ____|                         | |          ║
             ║      | |__  __  ____ _ _ __ ___  _ __ | | ___      ║
             ║      |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \     ║
             ║      | |____ >  < (_| | | | | | | |_) | |  __/     ║
             ║      |______/_/\_\__,_|_| |_| |_| .__/|_|\___|     ║
             ║                                 | |                ║
             ║                                 |_|   ARMI         ║
             ╚════════════════════════════════════════════════════╝
                             Version: {0:10s}
              ARMI Framework Version: {1:10s}
""".format("0.1", armi.meta.__version__)
