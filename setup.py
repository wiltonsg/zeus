"""
Zeus
--------------

Fast create scaffold of flask.
"""

from setuptools import setup

setup(
    name="zeus-lab804",
    version="0.1.2",
    url="https://github.com/murilobsd/zeus",
    license="BSD",
    description="Fast create scaffold of flask.",
    author="Lab804",
    author_email="contato@lab804.com.br",
    long_description=__doc__,
    include_package_data=False,
    packages=["zeusproject"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "attrs==18.1.0",
        "colorama==0.3.9",
        "colorlog==3.1.4",
        "Jinja2==2.10",
        "MarkupSafe==1.0"<
        "more-itertools==4.1.0"<
        "pluggy==0.6.0",
        "py==1.5.3",
        "pyfiglet==0.7.5",
        "pytest==3.5.1",
        "six==1.11.0",
        "termcolor==1.1.0",
        "tox==3.0.0",
        "virtualenv==15.2.0"
    ],
    scripts=["zeus"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
