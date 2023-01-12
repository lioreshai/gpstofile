import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gpstofile',
    author='pubudeux',
    # author_email='liores@gmail.com',
    description='Quick and easy way to read GPS sentences to file with no gpsd required.',
    keywords='gps, serial, gpsd, gps sentences',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pubudeux/gpstofile',
    project_urls={
        'Documentation': 'https://github.com/pubudeux/gpstofile',
        'Bug Reports':
        'https://github.com/pubudeux/gpstofile/issues',
        'Source Code': 'https://github.com/pubudeux/gpstofile',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)