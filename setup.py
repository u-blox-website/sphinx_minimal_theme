from setuptools import setup, find_packages

setup(
    name='minimal_theme',
    version='0.1.0',
    description='A minimal custom Sphinx theme.',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sphinx',
    ],
    entry_points={
        'sphinx.html_themes': [
            'minimal_theme = minimal_theme',
        ]
    },
    classifiers=[
        'Framework :: Sphinx :: Theme',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
    ],
)
