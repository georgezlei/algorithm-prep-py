import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithm-training",
    version="0.0.1",
    author="George Lei",
    author_email="george@lei.nz",
    description="A training package for Python programmers to practice the algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/georgezlei/algorithm-training-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)