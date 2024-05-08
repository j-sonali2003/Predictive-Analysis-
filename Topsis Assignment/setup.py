from setuptools import setup 
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="Topsis_Sonali_Jindal_102116117",version="0.19",
description="This is a topsis package of Sonali Jindal version 0.19",
long_description=long_description,
    long_description_content_type="text/markdown",
author="Sonali Jindal",
author_email="sonalijindal4141@gmail.com",
packages=['Topsis_Sonali_Jindal_102116117'],
install_requires=['pandas'],
include_package_data=True,
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Sonali_Jindal_102116117.Sonali_Jindal_102116117:main",
    ]  
    }
)
