from setuptools import setup

setup(
        name="LillyMedChemFilter",
        version="0.1",
        py_modules=["lillymcf"],
        install_requires=[
            'Click', 'pandas'
            ],
        entry_points="""
            [console_scripts]
            lillyfilter = lillymcf:filtermol
        """,
        )
