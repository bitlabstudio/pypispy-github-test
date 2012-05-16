import os
from setuptools import setup, find_packages
import pypispy_github_test


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="pypispy-github-test",
    version=pypispy_github_test.__version__,
    description=read('README.md'),
    keywords='python packages maintenance',
    author='Martin Brochhaus',
    author_email='martin.brochhaus@bitmazk.com',
    url="https://github.com/bitmazk/pypispy-github-test",
    packages=find_packages(),
    include_package_data=True,
)
