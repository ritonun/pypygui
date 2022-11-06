from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pypygui",
    version="0.2.0",
    description="GUI/HUD library for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ritonun/pypygui",
    author="ritonun",
    # author_email=
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment"
    ],
    keywords="pygame, gui, hud, menu, label, button",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=[
        "pygame >= 2.0.0"
    ],
    data_files=[("fonts", ["res/fonts/m5x7.ttf"])],
    project_urls={"source": "https://github.com/ritonun/pypygui"}
)
