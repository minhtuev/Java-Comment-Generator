from setuptools import setup, find_packages

setup(
    name='javacommentgenerator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'graphviz',
        'requests',
        'antlr4-python3-runtime==4.13.1',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'javacommentgenerator=javacommentgenerator.main:cli_entry_point'
        ]
    },
    author='Minh Tue Vo',
    description='Java code parser and comment generator with diagram support.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
