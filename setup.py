from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='BibFilmes',
    version='0.0.1',
    license='MIT License',
    author='Luiz Felipe',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='luiz.nogueira@ufpi.edu.br',
    keywords='BibFilmes',
    description=u'',
    packages=['BilFilmes'],
    install_requires=[''],)#biblioteca necessaria para a biblioteca funcionar
