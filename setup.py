'''
The setup.py file is and essential part of packageing and distributing python projects.it is used by setup tools (or distutils in older python version) to define the config of your project ,such as its metadata,dependencies and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirements
    '''
    requriement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != '-e.':
                    requriement_list.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not found')
    return requriement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Nithin chowdary",
    author_email="ntihinchowdarydavuluri05@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
