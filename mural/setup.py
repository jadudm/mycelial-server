from setuptools import setup

setup(
    name='mycelial',
    packages=['mycelial'],
    include_package_data=True,
    install_requires=[
        'flask',
        'peewee'
    ],
)