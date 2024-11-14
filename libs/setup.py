from setuptools import setup, find_packages

setup(
    name='libs',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'ciphey',
        'colorama'
    ],
    entry_points={
        'console_scripts': [],
    },
    author='cwe', # https://github.com/uhcode
    author_email='ozu@protocol.lat',
    description='Carefully crafted standalone libraries created in the Python language.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/uhcode/libs', # URL TO REPOSITORY
    classifiers=[
        'Programming Language :: Python :: 3', # Python version
        'License :: OSI Approved :: MIT License', # License
        'Operating System :: OS Independent', # OS
    ],
    python_requires='>=3.10',
)