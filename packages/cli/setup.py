"""
Acelang - Python SDK for FiveM Configuration Files
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent.parent.parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="acelang",
    version="1.0.0",
    description="Python SDK for parsing and validating FiveM Acelang configuration files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Acelang Contributors",
    author_email="",
    url="https://github.com/n11kol11c/acelang",
    project_urls={
        "Documentation": "https://github.com/n11kol11c/acelang#readme",
        "Source": "https://github.com/n11kol11c/acelang",
        "Tracker": "https://github.com/n11kol11c/acelang/issues",
    },
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "ruff>=0.1.0",
            "mypy>=1.0.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    keywords="fivem acelang configuration game-server",
)
