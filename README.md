# Example ARMI Application
This is a simple example application using the [Advanced Reactor Modeling
Interface (ARMI)](https://github.com/terrapower/armi). It is intended to serve
as a jumping-off point for new ARMI users and developers. Currently, it only
employs a single external plugin, TerraPower's open-source [Dragon
Plugin](https://github.com/terrapower/dragon-armi-plugin), which provides a
rudimentary interface to the [Dragon lattice physics
code](https://www.polymtl.ca/merlin/version5.htm). However, as new ARMI plugins
are made available to the public, this project may grow to encompass them as
well.

# Getting Started
As with other parts of the ARMI ecosystem, this project requires Python;
specifically Python 3.6 or greater. With Python installed, the Example ARMI App
can be installed in a couple of ways. The simplest is to install it straight
from this GitHub repository with:

    > python -m pip install git+https://github.com/terrapower/armi-example-app

This will cause `pip` to also install all of the dependencies of ARMI, the
Dragon ARMI plugin, and their dependencies in turn. You may notice that the
`armi` and `dragon-armi-plugin` packages are themselves coming from GitHub
repositories. This is because, for a number of reasons, they cannot be hosted as
wheels on the standard [Python Package Index](http://pypi.org).

Now that you have the ARMI components installed, you will also need to get set
up with Dragon. See the links above for some guidance on that. You will also
need to grab a data library to be able to run Dragon.

With Dragon set up properly, you should now be ready to run cases with the
example application. This is probably not going to be super earth-shattering,
though, since all it can do right now is produce cross sections.

Chances are, you are looking at this repository because you wish to make an ARMI
application of your own, or to experiment with adding a new ARMI plugin to an
existing application. If that's the case, you probably want to clone the whole
repository so that you can make modifications and see the documentation. Do that
now:

    > git clone https://github.com/terrapower/armi-example-app
    > cd armi-example-app

There is a simple example case in `doc/examples/ANL-AFCI-177/`, which is
explained in more detail
[here](https://terrapower.github.io/armi/user/tutorials/walkthrough_inputs.html).
You should be able to change directories into `doc/examples/ANL-AFCI-177/`, and
run the case with:

    > python -m armiexample run anl-afci-177.yaml

This fires up the built-in `run` ARMI entry point, which creates a [Standard
Operator](https://terrapower.github.io/armi/developer/guide.html#operators) and
runs through a single cycle, calculating cross sections using the Dragon Plugin.
After a whole bunch of output, you should see a handful of `ISOTXS` files that
were generated from the Dragon interface. If you see those, then you know it
worked.
