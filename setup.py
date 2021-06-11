import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3dbgutil",
    version="1.0.0",
    author="Benjamin R. Hall",
    author_email="ben.hall@rpsgroup.com",
    description="Debugging utility modules for Python 3 code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asascience-open/python3-debug-utils",
    project_urls={
        "Source Code": "https://github.com/asascience-open/python3-debug-utils",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2-Clause License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.8",
)