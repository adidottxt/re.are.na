'''
This is a setup.py file, created (for now) to allow tox to run
'''

from setuptools import setup, find_packages

with open("README.md", "r") as rm:
    LONG_DESCRIPTION = rm.read()

setup(
    name="re.are.na",
    version="0.0.1",
    author="Adi M (@adi_txt)",
    description="Enabling spaced repetition for are.na blocks",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/adi-txt/re.are.na",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
