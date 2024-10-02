from setuptools import setup

setup(
    name='i18n_tools',
    version='0.1.0',
    description='i18n tools for python',
    author='FY',
    packages=['i18n_tools'],
    entry_points={
        'console_scripts': [
            'i18n_tools = i18n_tools.main:main'
        ]
    }
)
