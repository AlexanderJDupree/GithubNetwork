from setuptools import setup, find_packages

setup(
        name = 'github-network',
        version = '1.0.0a',
        description='Visualize your GitHub social Network!',
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
        install_requires=['requests', 'matplotlib', 'networkx', 'numpy'],
        entry_points = {
            'console_scripts': [
                'github-network = GithubNetwork.app:main'
                ]
            }
        )

