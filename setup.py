from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'github-network',
        version = '1.0.0a',
        description='Visualize your GitHub social Network!',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/AlexanderJDupree/GithubNetwork',
        author='Alexander Dupree',
        author_email='alexanderjdupree@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Education',
            'Topic :: Scientific/Engineering :: Visualization',
            'Programming Language :: Python :: 3'
            ],
        keywords='GitHub Social Network',
        packages = find_packages(),
        python_requires='>=3.5',
        install_requires=['requests', 'matplotlib', 'networkx', 'numpy', 'PyYAML'],
        entry_points = {
            'console_scripts': [
                'github-network = GithubNetwork.app:main'
                ]
            }
        )

