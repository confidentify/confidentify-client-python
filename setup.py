from setuptools import setup

NAME = "confidentify-client-python"
VERSION = "1.0.0"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Confidentify Client for Python",
    author="Confidentify",
    author_email="info@confidentify.com",
    url="https://confidentify.com",
    keywords=["Confidentify", "API"],
    install_requires=REQUIRES,
    packages=["confidentify_client"],
    include_package_data=True,
    long_description="A Python client for the Conf·ident·ify APIs."
)
