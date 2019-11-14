import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
setuptools.setup(
    name='ScheMatch',
    version='0.21',
    scripts=['schematch/scr'],
    author="Sumit Mukhija",
    author_email="sumukhija@gmail.com",
    packages=['schematch'],
    description="Basic dictionary schema checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sumitmukhija/ScheMatch",
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
