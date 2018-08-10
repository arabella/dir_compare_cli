from setuptools import setup

setup(
    name='dir comparing app',
    version='1.0',
    py_modules=['dircompare.py'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        dircompare.py=dircompare.py:cli
    ''',
)