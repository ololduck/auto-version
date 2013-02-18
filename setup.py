from distutils.core import setup
from bin.pyver import __version__

setup(
    name='pyversion',
    version=__version__,
    author='Paul Ollivier',
    author_email='contact@paulollivier.fr',
    scripts=['bin/pyver.py'],
    url='https://github.com/paulollivier/auto_versionning',
    license='LICENSE.txt',
    description='A simple versionning semi-automation.',
    long_description=open('README.md', 'r').read(),
)
