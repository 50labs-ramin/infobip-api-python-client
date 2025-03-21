# coding: utf-8

"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.

    The version of the OpenAPI document: 1.0.0
    Contact: support@infobip.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "infobip-api-python-client"
VERSION = "5.1.0"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python_dateutil >= 2.5.3",
    "setuptools >= 72.1.0",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="This is a Python package for Infobip API and you can use it as a dependency to add Infobip APIs to your application.",
    author="Infobip support",
    author_email="support@infobip.com",
    url="https://pypi.org/project/infobip-api-python-client",
    keywords=[
        "infobip",
        "sms",
        "tfa",
        "2fa",
        "calls",
        "voice",
        "sdk",
        "rest",
        "api",
        "openapi",
    ],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description="""\
    OpenAPI specification containing public endpoints supported in client API libraries.
    """,  # noqa: E501
    package_data={"infobip_api_client": ["py.typed"]},
    cmdclass={"bdist_egg": None},
)
