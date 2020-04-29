from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='oneoff',

    version='0.0.1',

    description='My one-off scripts',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ghing/one-off-scripts',

    # This should be your name or the name of the organization which owns the
    # project.
    author='Geoff Hing',

    author_email='geoffhing@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='scripts utility',

    packages=find_packages(),

    python_requires='>=3.5',

    install_requires=['beautifulsoup4', 'fire'],

    entry_points={
        'console_scripts': [
            'extract_bookmarks=oneoff.extract_bookmarks:main',
        ],
    },
)
