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
    note: we read all the "yaml" file into the __init__ file inside the constant folder

    steps:

    1. data ingestion
    2. data validation
    3. data transformation
    4. Model Training
    5. model evaluation

    workflow: for each step we follow te below workflow

        1. update config.yaml # here we provide all the path related configuration

        2. update schema.yaml : while doing the data validation into the config.yaml, we'll require the validate the schema. hence, we're creating the schemas.yaml file.it is nothing but the describe the columns name and their dat type.

        3. update params.yaml

        4. update the entity # we create data class or static class as       required based on yaml file parameters

        5. update the configuration manager in src config
            #above folder we create a class which call the entity and __init__ file both

        6. update the components
            # above folder we'll creating  class which require for the 
                final purpose of the pipelines

        7. update the pipeline # in this file we call the function created in above files

        8. update the main.py # to run the pipeline file we call the class into main.py file

        9. update the app.py

            note: after create all the pipeline i,1 data ingestion, data validation,data transformation,model trainer, model evaluation, we'll update the code in app.py.
            in app.py we'll create an FAST API post request where we pass all the variables for the prediction.

step 6:
    deployement:
        for deployement, need to create a main.yaml file within the "github/workflow" path. here , we'll delete the existing ".gitkeep" file and create yaml file.
        in yaml file, write all the github action to aws deployement steps should be mentioned.
        "this yaml file steps we can get from the github to aws website.
        url: "https://github.com/sujeetkumae132/End-To-end-Machine-Learning-Project/actions/new"


step: 7

    ## MLflow

        [Documentation](https://mlflow.org/docs/latest/index.html)

        ##### cmd
        - mlflow ui

        ### dagshub
        [dagshub](https://dagshub.com/)

        MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
        MLFLOW_TRACKING_USERNAME=entbappy \
        MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
        python script.py

        Run this to export as env variables:

        ```bash

        export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

        export MLFLOW_TRACKING_USERNAME=entbappy 

        export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

        ```

step: 8

    # AWS-CICD-Deployment-with-Github-Actions

    ## 1. Login to AWS console.

    ## 2. Create IAM user for deployment

        #with specific access

        1. EC2 access : It is virtual machine

        2. ECR: Elastic Container registry to save your docker image in aws


        #Description: About the deployment

        1. Build docker image of the source code

        2. Push your docker image to ECR

        3. Launch Your EC2 

        4. Pull Your image from ECR in EC2

        5. Lauch your docker image in EC2

        #Policy:

        1. AmazonEC2ContainerRegistryFullAccess

        2. AmazonEC2FullAccess

        
    ## 3. Create ECR repo to store/save docker image
        - Save the URI: 010438509078.dkr.ecr.us-east-1.amazonaws.com/mlprojects

        
    ## 4. Create EC2 machine (Ubuntu) 

    ## 5. Open EC2 and Install docker in EC2 Machine:
        
        
        # setup for amazon linux based machine 

        a. update the package repository

            [sudo apt-get update -y] for debian 
                or
            [sudo yum update -y] for linux and other

        
        #required

        b. Install Docker
            
             sudo yum install docker -y

        c. Start the Docker service

            sudo service docker start

        d. Enable Docker to start on boot

            sudo systemctl enable docker

        e. Add your user to the Docker group (optional)
        
            sudo usermod -aG docker ec2-user


        f. verify Docker installation

            docker --version

        
    # 6. Configure EC2 as self-hosted runner:
        setting>actions>runner>new self hosted runner> choose os> then run command one by one


    # 7. Setup github secrets:

        AWS_ACCESS_KEY_ID=

        AWS_SECRET_ACCESS_KEY=

        AWS_REGION = us-east-1

        AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

        ECR_REPOSITORY_NAME = simple-app




    ## About MLflow 
    MLflow

    - Its Production Grade
    - Trace all of your expriements
    - Logging & tagging your model





