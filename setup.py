from setuptools import setup, find_packages

setup(
    name='naked',
    version='0.1.0',
    description='A command line application bootstrap framework',
    long_description=(open('README.rst').read() + '\n\n' +
                      open('HISTORY.rst').read() + '\n\n' +
                      open('AUTHORS.rst').read()),
    url='http://github.com/chrissimpkins/naked/',
    license='MIT',
    author='Christopher Simpkins',
    author_email='chris@zerolabs.net',
    platforms=['any'],
    py_modules=['naked'],
    scripts=['naked'],
    packages=find_packages(exclude=['tests*']),
    install_requires=['###', '###'],
    license='MIT License',
    keywords='python,command line,CLI,bootstrap,application,app,framework',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
