from distutils.core import setup
from increment_version import __version__

long_description = ""

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='auto-version',
    version=__version__,
    author='Paul Ollivier',
    author_email='contact@paulollivier.fr',
    scripts=['increment_version.py'],
    url='https://github.com/paulollivier/auto_versionning',
    license='LICENSE.txt',
    packages=['auto_version'],
    description='A not-so-simple versionning semi-automation.',
    long_description="TODO: Write a bit more about that"
)
