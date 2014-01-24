echo "Cythonizing .pyx files to C files"

cython benchmarking.pyx
cython casts.pyx
cython file.pyx
cython ink.pyx
cython network.pyx
cython python.pyx
cython shell.pyx
cython state.pyx
cython system.pyx
cython types.pyx


echo "Cythonize is complete"
