from setuptools import setup, find_packages

install_requires = [line.strip() for line in open("requirements.txt").readlines()]

setup(
    name="mysb-reminder",
    version="5.1",
    description="Remaining data notifications with LINE Notify",
    url="https://github.com/miya/mysb-reminder",
    author="miya",
    author_email="m0zurillex@gmail.com",
    keywords=["softbank", "scraping", "LINE Notify"],
    packages=find_packages(),
    install_requires=install_requires,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
