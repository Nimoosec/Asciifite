from setuptools import setup, find_packages

setup(
    name='asciifite',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    author='Nimoosec',
    author_email='nimuthudulsana@gmail.com',
    description='Professional ASCII conversion for images, video, and text banners.',
)