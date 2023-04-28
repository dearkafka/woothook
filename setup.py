from setuptools import setup, find_packages


def long_description():
    with open("README.md") as readme:
        return readme.read()


setup(
    name="woothook",
    version="0.0.1",
    author="Aleksei Ushakov",
    author_email="isfluid@proton.me",
    description="Chatwoot webhook server template using woot",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    packages=["woothook"],
    license="Cooperative Non-Violent Public License v7 or later (CNPLv7+)",
    project_urls={
        "Bug Tracker": "https://github.com/dearkafka/woothook/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.27.1",
        "woot @ git+https://github.com/dearkafka/woot#egg=woot",
        "typer",
        "fastapi",
        "uvicorn",
    ],
    entry_points={  # Optional
        "console_scripts": [
            "woothook=woothook.service:app",
        ],
    },
)
