try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from auto_version.main import __version__

setup(
    name='auto-version',
    version=__version__,
    author='Paul Ollivier',
    author_email='contact@paulollivier.fr',
    url='https://github.com/paulollivier/auto-version',
    license=open('LICENSE.txt', 'r').read(),
    packages=['auto_version'],
    description='A not-so-simple versioning semi-automation.',
    long_description=open('README.rst', 'r').read(),
    requires=["argparse"],
    entry_points={
      'console_scripts': [
          'auto-version = auto_version.main:main',
          ]
      },
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
