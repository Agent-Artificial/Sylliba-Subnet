from setuptools import setup

setup(
    name="translation_module",
    version="1",
    entry_points={
        "translation": ["translation=modules.translation.translation.Translation:process"],
    }
)