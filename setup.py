from setuptools import setup

setup(name='pycfg',
      version='0.1',
      description='The python3 ast based control flow graph',
      long_description="""
This package generates a control flow graph of the passed python file based on the AST generated (rather than the bytecode). It supports only a few python statements at this point. Notably absent are exceptions and generators. Essentially, only those constructs found in example.py are supported.

        Compatibility
        -------------
        It was tested on Python 3.6
        
        
        To run
        ------
        
          python pycfg/pycfg.py <program to be analyzed> -d
          or
          python pycfg/pycfg.py <program to be analyzed> -d -y <branch coverage file>

          Inspect Makefile for a better idea
       """,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Compilers'
      ],
      keywords='control-flow-graph abstract-syntax-tree',
      url='http://github.com/vrthra/pycfg',
      author='Rahul Gopinath',
      author_email='rahul@gopinath.org',
      license='GPLv3',
      packages=['pycfg'],
      zip_safe=False)
