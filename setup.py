from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from a file.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]

            # Remove '-e .' if present
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
                
    except FileNotFoundError:
        print(f"Error: The requirements file '{file_path}' was not found.")
        raise
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vedaant',
    author_email='vedaant912@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('./requirements.txt'),
)
