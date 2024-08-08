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


step 5:
    note: we read allthe "yaml" file into the __init__ file inside the constant folder
    workflow: for each step we follow te below workflow
        1. update config.yaml
        2. update schema.yaml : while doing the data validation into the config.yaml, we'll require the validate the schema. hence, we're creating the schemas.yaml file.it is nothing but the describe the columns name and their dat type.
        3. update params.yaml
        4. update the entity # we create data class or static class as       required based on yaml file parameters
        5. update the configuration manager in src config
        6. update the components
        7. update the pipeline
        8. update the main.py
        9. update the app.py


