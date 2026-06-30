from setuptools import find_packages,setup
from typing import List

HYPHER_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will retun the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)

    return requirements

setup
(
   name='mlproject',
   version='0.0.1',
   description='a dummy end to end ml project',
   author = 'zaro_the_coder',
   author_email='author07@gmail.com',
   packages=find_packages(),  #same as name
   install_requires= get_requirements('requirements.txt') #external packages as dependencies
)