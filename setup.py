import os
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
def get_packages(name, root):
    pkgs = []
    for pkg in find_packages():
        pkgs.append(pkg.replace(root, name))
    return pkgs
config = {
    "name": "pagestat",
    "version": "0.0.1",
    "description": ("Generates tag usage statistics for web pages"),
    "url": "http://github.com/hrithikp/pagestat",
    "package_dir": {'pagestat':'src'},
    "packages": get_packages('pagestat','src'),
    "entry_points": {
      'console_scripts': ['pagestat=pagestat.cli:main'],
    },
    "long_description": read('README.md')
}
setup(**config)