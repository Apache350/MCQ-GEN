from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.1',
    author='Vishal Tiwari',
    author_email='vishaltiwari5984@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain',
'streamlit',
'openai',
'PyPDF2',
'python-dotenv',
'langchain_community',
    ]
)