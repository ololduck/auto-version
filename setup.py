from distutils.core import setup

setup(
    name='pyVersion',
    version='0.1.2',
    author='Paul Ollivier  ',
    author_email='contact@paulollivier.fr',
    scripts=['bin/pyver.py'],
    url='https://github.com/paulollivier/auto_versionning',
    license='LICENSE.txt',
    description='A simple versionning automation.',
    long_description=open('README.md').read(),
)
