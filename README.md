WaaS
====

WaaS stands for Weather as a Service. It is a simple command line utility
which retrieves the current weather conditions for the location identified
by the supplied IP. This defaults to the IP address of the system the
command is run on if no IP is supplied.

Setup
=====
WaaS can be installed with the normal virtualenv steps:

    virtualenv --python=python2.7 venv
    . venv/bin/activate
    python setup.py develop```

and then run with:

    waas
