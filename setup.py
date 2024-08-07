import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_description=f.read()
    
__version__="0.0.0"

Repo_Name="End-To-end-Machine-Learning-Project"
Author_User_Name="sujeetkumae132"
Src_Repo="mlproject"
Author_Email="kumar.sujeet132@gmail.com"

setuptools.setup(
    name=Src_Repo,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_Email,
    description="A python package for end to end ml project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{Repo_Name}",
    project_url={
        "Bug Tracker": f"https://github.com/{Author_User_Name}/{Repo_Name}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)