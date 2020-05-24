import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithm-prep",
    version="0.0.2",
    author="George Lei",
    author_email="george@lei.nz",
    description="Programming algorithm training package for programmers and students",
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