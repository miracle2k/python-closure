#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
    name="closure",
    description="Closure compiler packaged for Python",
    long_description=open('README.rst').read(),
    author='Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    version="20160517",
    url="http://pypi.python.org/pypi/closure",
    license='BSD',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            "closure = closure:main"
        ]
    },
    package_data={
        '': ["*.jar"]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
