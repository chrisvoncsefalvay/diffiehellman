# coding=utf-8
import io
from distutils.core import setup


# Shamelessly stolen from Jeff Knupp.
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name='diffiehellman',
    version='diffiehellman.__version__',
    packages=[''],
    url='http://www.github.com/chrisvoncsefalvay/diffiehellman',
    license='MIT',
    author='Chris von Csefalvay',
    author_email='chris@chrisvoncsefalvay.com',
    description='A Pythonic implementation of the Diffie-Hellman key exchange protocol',
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
    ]
)