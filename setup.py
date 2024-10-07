from setuptools import setup, find_packages

setup(
    name='TTS-Framework',  
    version='0.1',        
    author='Crystal',  
    author_email='crystaljoyce226@gmail.com',  
    description='A bidirectional natural language processing framework for cross-linguistic text-to-speech generation in Tagalog and Ilocano.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='https://github.com/crystalarizala/TTS-Framework', 
    packages=find_packages(),
    install_requires=[
        'numpy', 
        'scipy',
        'tensorflow',  # or any other packages you use
        # Add more dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3'  
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ],
    python_requires='>=3.6',  
)
