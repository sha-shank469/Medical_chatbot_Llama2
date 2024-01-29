# We use setup.py because If you are planning to distribute your Python package to other users, 
# then you should use setup.py. It is a powerful tool that can help you to automate the process
# of building and distributing your package.

from setuptools import find_packages,setup
#setuptool is a prebuilt package inside python 
setup(
    
    name='medical-chatbot',
    version = '0.0.0',
    author= 'Shashank',
    author_email='shashankmishra892@gmmial.com',
    packages=find_packages(),
    # find_package will look for constructor file __init__.py, where that file will be present that folder will be considered as local package.
    install_requires = []
)