
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='sshaws',
    version='0.5.0',
    description='Simply connect to your "EC2 Instance Connect"-capable AWS EC2 servers using one command',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/FrederikP/sshaws',
    author='Frederik Petersen',
    author_email='sshaws@the-imperfection.de',
    classifiers=[  
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='aws connect ssh cli instance',
    packages=[],
    python_requires='>=3.0, <4',
    install_requires=['boto3'],
    scripts=['sshaws'],
    project_urls={
        'Bug Reports': 'https://github.com/FrederikP/sshaws/issues',
        'Source': 'https://github.com/FrederikP/sshaws',
    },
)