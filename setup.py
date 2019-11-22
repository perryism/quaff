from distutils.core import setup

setup(name='quaff',
      version='0.4.1',
      packages=['quaff', 'quaff/strategies'],
      install_requires=['flask', 'Jinja2'],
      )
