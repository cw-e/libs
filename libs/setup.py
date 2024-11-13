from setuptools import setup, find_packages

setup(
    name='libs',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp'
    ],
    entry_points={
        'console_scripts': [
            # Define your command line scripts here
        ],
    },
    author='cwe',
    author_email='ozu@protocol.lat',
    description='Carefully crafted standalone libraries created in the Python language.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/uhcode/libs',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)