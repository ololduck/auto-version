from distutils.core import setup
from increment_version import __version__

setup(
    name='auto-version',
    version=__version__,
    author='Paul Ollivier',
    author_email='contact@paulollivier.fr',
    scripts=['increment_version.py'],
    url='https://github.com/paulollivier/auto_versionning',
    license='LICENSE.txt',
    modules=['auto_version'],
    description='A not-so-simple versionning semi-automation.',
    long_description=open('README.md', 'r').read(),
)
