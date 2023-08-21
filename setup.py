from setuptools import setup

setup(
    name='arithmopkg',
    version='0.1',
    packages=['arithmopkg'],
    entry_points={
        'console_scripts': [
            'arithmopkg = arithmopkg.__main__:main',
        ],
    },
)
