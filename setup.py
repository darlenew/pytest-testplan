"""Setup for pytest-testplan plugin."""
from setuptools import setup


setup(
    name='pytest-testplan',
    version='0.1.0',
    description='A pytest plugin to generate a CSV test report.',
    author='Darlene Wong',
    author_email='darlene.py@gmail.com',
    license='MIT',
    py_modules=['pytest_testplan'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['testplan = pytest_testplan', ]},
)
