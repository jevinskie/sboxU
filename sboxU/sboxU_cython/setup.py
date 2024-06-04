from setuptools import setup
from distutils.core import Extension
from Cython.Build import cythonize
import os
from sys import platform


g_module = os.environ["SBOXU_MOD"]


if platform == 'darwin':	#macOs
	os.environ["CC"] = "clang"
	os.environ["CXX"] = "clang"
else:
	os.environ["CC"] = "g++"
	os.environ["CXX"] = "g++"
extra_compile_args = ["-O3", "-march=native", "-std=c++17", "-pthread", "-Wno-narrowing"]	#narrowing warnings in fp_lat when calling shape_t{p}
extra_link_args=[]

HOME = os.path.expanduser('~')
if platform == 'darwin':
	extra_compile_args += ['-lomp', '-I/opt/homebrew/opt/libomp/include']
	extra_link_args += ['-lomp', '-L/opt/homebrew/opt/libomp/lib']
else:
	extra_compile_args += ['-fopenmp']
	extra_link_args += ['-fopenmp']



module_diff_lin = Extension("cpp_diff_lin",
						sources=["cpp_diff_lin.pyx"],
								libraries=[],
						include_dirs=['.'], 
						language='c++',
				extra_link_args=extra_link_args,
				extra_compile_args=extra_compile_args)
				

module_utils = Extension("cpp_utils",
		         sources=["cpp_utils.pyx"], 
		         include_dirs=['.'],
		         language='c++',
			 extra_link_args=extra_link_args,
                         extra_compile_args=extra_compile_args)

module_equiv = Extension("cpp_equiv",
		         sources=["cpp_equiv.pyx"], 
		         include_dirs=['.'], 
		         language='c++',
			 extra_link_args=extra_link_args,
                         extra_compile_args=extra_compile_args)

module_equiv_approx = Extension("cpp_equiv_approx",
		         sources=["cpp_equiv_approx.pyx"], 
		         include_dirs=['.'], 
		         language='c++',
			 extra_link_args=extra_link_args,
                         extra_compile_args=extra_compile_args)

module_ccz = Extension("cpp_ccz",
		       sources=["cpp_ccz.pyx"], 
		       include_dirs=['.'], 
		       language='c++',
 		       extra_link_args=extra_link_args,
                       extra_compile_args=extra_compile_args)

if g_module == "cpp_utils":
	setup(name='cpp_utils',    ext_modules=cythonize([module_utils],    language_level = "3"))
elif g_module == "cpp_diff_lin":
	setup(name='cpp_diff_lin', ext_modules=cythonize([module_diff_lin], language_level = "3"))
elif g_module == "cpp_equiv":
	setup(name='cpp_equiv',    ext_modules=cythonize([module_equiv],    language_level = "3"))
elif g_module == "cpp_equiv_approx":
	setup(name='cpp_equiv_approx',    ext_modules=cythonize([module_equiv_approx],    language_level = "3"))
elif g_module == "cpp_czz":
	setup(name='cpp_ccz',      ext_modules=cythonize([module_ccz],      language_level = "3"))
else:
	raise ValueError('must select a module using SBOXU_MOD=<mod_name} from: cpp_utils cpp_diff_lin cpp_equiv cpp_equiv_approx cpp_czz')
