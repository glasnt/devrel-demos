# Running vuejs on Cloud Run

<!--- Generated 2022-08-24 05:21:43.335119 -->

To deploy a [vuejs](https://vuejs.org/) application to Cloud Run, you will need an application
based on this framework. This demo gets you to use the vuejs template to generate one. 

This requires , and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Install the framework:

    ```bash
    npm init vue@latest
    ```

* Create a new template application:

    ```bash
    # Use "helloworld" for the project name
    # Press Enter for all other defaults. 
    npm install

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    npm run dev
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.


## Configure for Cloud Run

Using [Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks), 
the base language is automatically identified.



For  applications, you have specify what you want the web process to run using a `Procfile`. 

* Create a new file called `Procfile` with the following contents: 

    ```
    web: npm run dev
    ```







## Deploy to Cloud Run

* Build and deploy the service to Cloud Run: 


    ```bash
    gcloud run deploy vuejs-helloworld \
        --source . \
        --allow-unauthenticated 
    ```

    Type "Y" for all suggested operations.


Your service will now be deployed at the URL in the deployment output.

![Example vuejs deployment](example.png)

## Learn more

Resources: 

- https://vuejs.org/guide/quick-start.html
- https://vuejs.org/guide/best-practices/production-deployment.html
