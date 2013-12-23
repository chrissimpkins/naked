import os
from setuptools import setup, find_packages
from Naked.commands.version import Version


def description_read(fname):
    return open(os.path.join(os.path.dirname(__file__), 'docs', fname)).read()

setup(
    name='Naked',
    version=Version().get_version(),
    description='A command line application framework',
    long_description=(description_read('README.rst')),
    url='http://github.com/chrissimpkins/naked/',
    license='MIT',
    author='Christopher Simpkins',
    author_email='chris@zerolabs.net',
    platforms=['any'],
    #py_modules=['naked'],
    #scripts=['naked'],
    entry_points = {
        'console_scripts': [
            'naked = Naked.app:main'
        ],
    },
    packages=find_packages("lib"),
    package_dir={'': 'lib'},
    install_requires=['Naked'],
    keywords='python,command line,system,application,framework,CLI,bootstrap',
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
