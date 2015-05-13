from setuptools import setup, find_packages

setup(
    name='espark-pathmaker',
    packages=find_packages('espark'),
    package_dir={'': 'espark'},
    version='0.0.1',
    description='Calculates a study path for students.',
    url='https://github.com/miketwo/espark',
    download_url='',
    keywords="espark students",
    license='MIT',
    scripts=['bin/create_path'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=open('README.md', 'r').read(),
    tests_require=['nose>=1.3.6'],
    include_package_data=True,
    )
