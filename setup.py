from setuptools import find_packages, setup

setup(
    name="ecombot",
    version="0.0.1",
    author="Tejas Dalvi",
    author_email="tejasdalvi.coep@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)