"""Setup file"""

from setuptools import setup, find_packages

with open("requirements.txt",encoding='UTF-8') as f:
    required = f.read().splitlines()

setup(
    name="analyzer_model",
    version="0.1",
    description="It analyze your doc and answer your",
    author="Boss",
    # author_email='vi',
    # license='MIT',
    install_requires=required,
    packages=find_packages(where="analyzer_model"),
    # zip_safe=False
)
