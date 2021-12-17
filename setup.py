try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='ThermoSim',
    version='0.6',
    license='GPL',
    author='Pierre Vaudry',
    author_email='pierrevaudry4@gmail.com',
    description='A tkinter GUI builder.',
    long_description=open('README.md').read(),
    url='https://github.com/Rsky-20/EquationVanDerWaals',

    packages=['tkinter','pillow','pyscreenshot','matplotlib','numpy'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Software Development :: User Interfaces",
    ],
)