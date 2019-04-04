from setuptools import setup, find_packages

setup(
        name = 'github-network',
        version = 'v0.0.1-alpha',
        packages = find_packages(),
        entry_points = {
            'console_scripts': [
                'github-network = GithubNetwork.app:main' 
                ]
            }
        )
