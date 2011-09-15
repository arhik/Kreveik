from setuptools import setup, find_packages

setup(
    name = "Kreveik",
    version = "0.5.0 dev",
    packages = find_packages(),
    # scripts = ['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Mehmet Ali Anil",
    author_email = "mehmet.ali.anil@ieee.org",
    description = "Kreveik is a Python module for Boolean networks. With Kreveik, one can build Boolean networks, create random Boolean networks, investigate dynamics of these networks, form families of them, investigate macroscopic variables and expose them to genetic algorithms.",
    license = "LICENSE.txt",
    keywords = "random boolean networks genetic algorithm",
    url = "http://github.com/mehmetalianil/Kreveik/",    
    # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)