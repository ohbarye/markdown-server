import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
    name = 'markdown-server',
    version  = '0.1.1',
    description = 'A simple markdown server.',
    long_description = read_file('README.rst'),
    author = 'Masato Ohba',
    author_email = 'over.rye@gmail.com',
    url = 'https://github.com/ohbarye/markdown-server',
    classifiers = [
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Framework :: Bottle',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages = find_packages(),
    include_package_data = True,
    keywords = ['web', 'markdown'],
    license = 'MIT License',
    install_requires = [
        'bottle',
        'Markdown',
        'Pygments',
        'py-gfm',
    ],
    entry_points = {
        'console_scripts': [
            'mdsvr = markdownserver:main',
            'convert = markdownserver.markdown_converter:main'
        ]
    },
)
