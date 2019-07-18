""" Standard packaging setup """
# pylint: disable-all

import os
from setuptools import setup
import versioneer

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

setup(
    name=about['NAME'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
    classifiers=about['CLASSIFIERS']
)
