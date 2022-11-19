from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='egucolours',
    version='0.1.0',
    author='Andreas Kvas',
    description='Color palettes of the European Geosciences Union (EGU) visual identity.',
    packages=['egucolours']
)
