import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplesimdb",
    version="1.0.3",
    author="Matthias Wiesenberger",
    author_email="mattwi@fysik.dtu.dk",
    description="Create, access and manage simple simulation data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwiesenberger/simplesimdb",
    py_modules=["simplesimdb"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        "Topic :: Database"
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
