import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "Multi-Document-Summarizer-Project"
AUTHOR_USER_NAME = "Manojkumar-web-cyber"
SOR_REPO = "documentsSummarizer"
AUTHOR_EMAIL = "manojbag2014@gmail.com"


setuptools.setup(
    name=SOR_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A multi-document summarizer project using NLP techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SOR_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SOR_REPO}/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)