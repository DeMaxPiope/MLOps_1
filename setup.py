from setuptools import setup, find_packages

setup(
    name="credit_default_analysis",
    version="1.1b3",
    description="Credit default analysis package",
    author="M_Akulov",
    packages=find_packages(),
    install_requires=[
        # не забыть указать зависимости
    ],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
