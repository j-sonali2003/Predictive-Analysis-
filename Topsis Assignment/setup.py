from setuptools import setup 
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="Topsis_Deepankar_Varma_102003431",version="0.19",
description="This is a topsis package of Deepankar Varma version 0.19",
long_description=long_description,
    long_description_content_type="text/markdown",
author="Deepankar Varma",
author_email="satiwkdprhrit@gmail.com",
packages=['Topsis_Deepankar_Varma_102003431'],
install_requires=['pandas'],
include_package_data=True,
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Deepankar_Varma_102003431.Deepankar_Varma_102003431:main",
    ]  
    }
)