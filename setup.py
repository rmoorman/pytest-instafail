from setuptools import setup

setup(
    name='pytest-instafail',
    description='py.test plugin to show failures instantly',
    long_description=open("README.rst").read(),
    version='0.3.0',
    url='https://github.com/pytest-dev/pytest-instafail',
    license='BSD',
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    py_modules=['pytest_instafail'],
    entry_points={'pytest11': ['instafail = pytest_instafail']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=2.9'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
