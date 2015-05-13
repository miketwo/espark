from setuptools import setup

setup(
    name='espark',
    version='0.0.1',
    description='Calculates a study path for students.',
    url='https://github.com/miketwo/espark',
    keywords="espark students",
    packages=['espark'],
    scripts=['bin/esparkify'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=open('README.md', 'r').read(),
    )
