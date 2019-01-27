import pip
from sherlock import __version__ as serlockv
from sherlock import __description__ as serlockd
from setuptools import setup
from setuptools.command.install import install as InstallCommand


class Install(InstallCommand):
    def run(self, *args, **kwargs):
        pip.main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)

# Requirements for the pypi

deps = open("requirements.txt", "r")
_requirements = []
with open("requirements.txt", "r") as f:
    for line in f:
        line=line.strip("\n")
        _requirements.append(line)
        

# Packages part of setup
_packages = [
    "sherlock",
    "sherlock.core",
    "sherlock.exception"
]

# Setup for the project
setup(
    name="thesherlock",
    version=serlockv,
    description="Sherlock the username detective",
    long_description=serlockd,
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    keywords="sherlock finder username pypi",
    url="https://github.com/TheYahya/sherlock/",
    license="MIT",
    packages=_packages,
    install_requires=_requirements,
    python_requires=">=3.5",
    classifiers=[
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only"
    ],
    entry_points={
        'console_scripts': ['sherlock=sherlock._sherlock_main:main'],
    }
)
