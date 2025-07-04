import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_version_ = "0.0.1"

REPO_NAME = "Kidney-Disease-Classification" 
AUTHOR_USER_NAME = "chirag003214"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL = "csharma@kgpian.iitkgp.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
