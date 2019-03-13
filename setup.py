from setuptools import setup
import io, codecs, os, sys
from setuptools.command.test import test as TestCommand

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = {}
        self.test_suite = True

    def run_tests(self):
        sys.exit()

setup(
    name='PyPub',
    url='http://github.com/speeddown/pypub/',
    license='MIT License',
    author='Ben Arceneaux',
    author_email='benarceneaux0@gmail.com',
    tests_require=['pytest'],
    #cmdclass={'test' : PyTest},
    description='Simple Event Publishing Library',
    long_description = long_description,
    packages=['pypub'],
    include_package_data=True,
    platforms='any',
    test_suite='pypub.tests.test_pypub',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
    # extras_require={
    #     'testing' : ['pytest'],
    # }
)