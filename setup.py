from setuptools import find_packages, setup

setup(
    name = "e-commerce-chatbot",
    version = "0.0.1",
    author = "Syed Areeb Ahmad",
    author_email = "ahmad.syedareeb7@gmail.com",
    packages = find_packages(),
    install_requires = ['langchain-astradb','langchain']
)