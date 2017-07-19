#from setuptools import setup
import shutil
from distutils.core import setup, Extension
from Cython.Build import cythonize
import os
import stat



cy=['pycam/cutils.pyx']
cy_ext=Extension('pycam/cutils',sources=cy)

ext_modules=cythonize(cy_ext)

setup(
		name='pycam',
		version='2.5.0',
		author='Giuliano Iorio',
		author_email='',
		url='',
		packages=['pycam'],
        scripts=['pycam/script/makehalo.py'],
        ext_modules=ext_modules
	)


#script
try:
    file='pycam/script/makehalo.py'
    st = os.stat(file)
    os.chmod('pycam/script/makehalo.py', st.st_mode | stat.S_IEXEC)
    shutil.copy(file,'/usr/bin/makehalo')
except:
    print('Impossible to mv the script makehalo')

try:
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('pycam.egg-info')
    print('Done')
except:
    print('Done')
