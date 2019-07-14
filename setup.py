
import os
import sys
from setuptools import setup

PACKAGE_NAME = 'parse_bom_stations'

about = {}

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, PACKAGE_NAME, 'about.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requires = [
    "pandas>=0.24"
]

setup_requires = [

]

tests_requires = [
    'pytest-cov>=2.6',
    'pytest>=4.2',
    'pytest-datafiles==2.0'
]

setup(
    name=about['NAME'],
    version=about['VERSION'],
    description=about['__doc__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['AUTHOR'],
    author_email=about['AUTHOR_EMAIL'],
    url='https://github.com/weather-balloon/lib-py-parse-bom-stations',
    license=about['LICENCE'],
    packages=[about['NAME']],
    python_requires='>=3.6',
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_requires=tests_requires,
    classifiers=about['CLASSIFIERS']
)
