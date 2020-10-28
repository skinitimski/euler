from setuptools import find_packages
from setuptools import setup


setup(
    name='euler',
    version='0.0.0',
    packages=find_packages(exclude=['tests']),
    author='timski',
    entry_points={
        'console_scripts': [
            'euler = euler.euler:main'
        ]
    }
)

