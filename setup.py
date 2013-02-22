try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from increment_version import __version__

setup(
    name='auto-version',
    version=__version__,
    author='Paul Ollivier',
    author_email='contact@paulollivier.fr',
    scripts=['increment_version.py'],
    url='https://github.com/paulollivier/auto_versionning',
    license=open('LICENSE.txt', 'r').read(),
    packages=['auto_version'],
    description='A not-so-simple versionning semi-automation.',
    long_description=open('README.rst', 'r').read(),
    requires=["argparse"],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 2.7',
    ),
)
