from setuptools import setup, find_packages

setup(
    name="instructional_design_notebook_helper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ipywidgets"
    ],
    description="Helpers for educational notebooks",
)
