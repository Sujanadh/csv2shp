from setuptools import setup, find_packages

setup(
    name='csv2shp',
    version='1.0.0',
    description='A Python package to convert CSV to Shapefile',
    author='Sujan Adhikari',
    author_email='sujanadh07@email.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'geopandas',
        'shapely',
    ],
    license='MIT',
)
