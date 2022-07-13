from setuptools import setup, find_packages

setup(name='montecarlo',
      version='1.0',
      
      # list folders, not files
      packages=['montecarlo'], # Include packages in the project
      install_requires=['click'],         # Required libraries
)
