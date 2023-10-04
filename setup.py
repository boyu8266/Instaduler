import subprocess

from setuptools import find_packages, setup


def get_version(default: str = '0.1.0-alpha0') -> str:
    '''
    Get the version name through Git Tag, default is '0.1.0-alpha0'.
    '''
    ret = default
    try:
        # Call the Git command to retrieve all tag information
        git_tags = subprocess.check_output(
            ['git', 'tag', '-l']).decode().splitlines()

        if len(git_tags) > 0:
            git_tags.reverse()
            ret = git_tags[0]
    except:
        ret = default
    return ret


setup(
    name="instaduler",
    version=get_version(),
    author="boyu8266",
    author_email="boryuh8266@gmail.com",
    packages=find_packages(),
    install_requires=[
        'instagrapi==2.0.0',
        'Pillow==10.0.1',
        'tpdp==0.1.0',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'instaduler=instaduler.__main__:main',
        ],
    },
)
