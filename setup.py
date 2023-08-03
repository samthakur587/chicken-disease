from setuptools import setup, find_packages

# Read the dependencies from requirements.txt file
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')
if "-e ." in install_requires:
    install_requires.remove("-e .")

setup(
    name='pypl_testing',  # Replace 'your_project_name' with the actual name of your project
    version='0.1.0',  # Replace '0.1.0' with the version number of your project

    description='starting to build a end to end project for data science',
    long_description='countine...',  # You can provide a README file here

    author='Samunder Singh',  # Replace 'Your Name' with your name
    author_email='singhsamunder270@gmail.com',  # Replace 'your.email@example.com' with your email

    url='https://github.com/samthakur587/chicken-disease',  # Replace with the URL of your project repository
    license='MIT',  # Choose an appropriate license for your project

    packages=find_packages(exclude=['tests']),  # Automatically find all packages in your project

    install_requires=install_requires,  # Use the dependencies read from requirements.txt

    classifiers=[  # Classifiers help categorize your project for PyPI
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='ml, samunder , pranjal, chutiye log, bc kya h ye, or bhai kaisa h',  # Add relevant keywords for your project

    # You can include other data files like package data, scripts, etc., if needed
    # data_files=[('data', ['data/datafile.dat'])],

    # Add any entry points or console scripts here
    # entry_points={
    #     'console_scripts': [
    #         'your_script_name=your_package_name:main',
    #     ],
    # },

    # If you have non-Python dependencies, you can specify them here
    # setup_requires=['pytest-runner'],

    # Include package data, if any
    # include_package_data=True,
)
