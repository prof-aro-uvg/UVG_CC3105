from setuptools import setup, find_packages

setup(
    name="movie_etl",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="ARO",
    description="A simple ETL pipeline for movie ratings",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
