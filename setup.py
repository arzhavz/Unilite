from setuptools import setup

setup(
    name='unilite',
    version='1.0',
    py_modules=['unilite'],
	install_requires=[
        'prompt_toolkit'
    ],
    entry_points={
        'console_scripts': [
            'unilite=unilite:main'
        ]
    }
)
