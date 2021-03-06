from setuptools import setup, find_packages
__VERSION__ = '1.2.0'

setup(
    name='nicedjango',
    version=__VERSION__,
    description="Nice extensions for django",
    long_description=(open('README.rst').read()),
    author='Mathias Seidler',
    author_email='seishin@gmail.com',
    maintainer='Mathias Seidler',
    maintainer_email='seishin@gmail.com',
    url='http://github.com/katakumpo/nicedjango',
    license='MIT License',
    platforms=['any'],
    packages=find_packages(exclude=['tests*']),
    install_requires=['Django>=1.5', 'six>=1.2'],
    tests_require=['Django', 'pytest', 'pytest-django'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
)
