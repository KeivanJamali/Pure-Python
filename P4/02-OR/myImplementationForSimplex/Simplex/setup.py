from setuptools import setup, find_packages

setup(
    name='Simplextep',
    version='1.13.2',
    packages=find_packages(where="scr"),
    package_dir={'':'scr'},
    description='Simplex implementation with steps.',
    author='Keivan Jamali',
    author_website='Keivanjamali.com',
    author_email='K1Jamali01@gmail.com',
    url='https://github.com/KeivanJamali/simplextep',
    install_requires=["numpy", "pandas", "tabulate", "matplotlib"],
    license="MIT"
)