from setuptools import find_packages,setup
from typing import List

hypen_e_dot = "-e ."

def get_requirements(filepath:str) -> List[str]:

    requirements =[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for  req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)

setup (
name="Student Performance Prediction Project",
version="0.1",
description="Predict Scores in Different Subjects",
author="Naveen Narasimhappa",
packages= find_packages(),
install_requires= get_requirements("requirements.txt")
)