from distutils.core import setup

setup(name='quaff',
      version='0.5.0',
      packages=['quaff', 'quaff/strategies'],
      install_requires=['flask', 'Jinja2'],
      )
