# End-To-end-Machine-Learning-Project
End To end Machine Learning Project with ML Flow

step1. 

    template.py
        it will create all the folder structure which we required for 
        end to end project.
        following folder we are creating:
            a. components
            b. utils : here we'll create a file, which we use frequently as a function or etc.
            c. config
            d. pipeline
            e. entity
            f. constant
            g. config
        apart from folder we'll create following files:
            a. params.yaml
            b. schema.yaml
            c. Dockerfile
            d. main.py
            e. app.py
            f. setup.py


step 2. 

    requirements.txt
    added all the required library name
        Note:- add "-e ." in the file to look for the setuptool.py file

step 3.

    setup.py
        import setuptools
        and basic setup

    following are the parameters which are to be in setuptools:
        setuptools.setup(
        name="",
        version="",
        author="",
        author_email="",
        description="",
        long_description="",
        long_description_content_type="text/markdown",
        url=f"https://github.com/{Author_User_Name}/{Repo_Name}",
        project_url={
            "Bug Tracker": f"https://github.com/{Author_User_Name}/{Repo_Name}/issues"
        },
        package_dir={"":"<src file folder name>"},
        packages=setuptools.find_packages(where="<src file folder name>")
            )

step 4. 

    update the basic logging  into "__init_file.py" inside the "src/mlproject "
    ex: we'll read the yaml file frequently

