# center of all activites in building
from setuptools import find_packages,setup
from typing import List
hyphone_e="-e ."
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hyphone_e in requirements:
            requirements.remove(hyphone_e)


setup(name='ml_pipeline_project',
      version='0.0.1',
      description='MAchine Learning Pipeline project',
      author='Drashti Shah',
      author_email='drashtishah058@gmail.com',
      url='https://github.com/Drashti-shah05/ml_pipeline_project',
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
     )