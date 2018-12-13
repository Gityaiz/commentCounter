setup(
    name='comment_counter',
    version='0.0.1',
    description='This program lets you help to count comment lines in your source code. ',
    long_description=readme,
    author='Yuji Mochizuki',
    install_requires=['glob'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)