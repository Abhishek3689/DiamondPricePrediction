from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.01',
    author='Abhishek Nishad',
    author_email='abhinishadforu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)