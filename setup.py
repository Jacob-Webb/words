from setuptools import setup, find_packages

setup(
    name='permutations',
    version='0.1',
    description='Create all possible words from a set of letters',
    url='https://github.com/sanctifyd/permutations',
    author='sanctifyd',
    author_email='sanctifyd83@yahoo.com',
    packages=['tkinter'],
    python_requires='>=3',
    package_data={'': ['*.dic']},
    include_package_data=True
)
