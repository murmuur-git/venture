import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="venture-tools",
    version="2020.10.22",
    author="murmuur",
    description="a CLI tool to initialize a new project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murmuur-git/venture.git",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'venture = venture.__main__:main'
        ]
    })
