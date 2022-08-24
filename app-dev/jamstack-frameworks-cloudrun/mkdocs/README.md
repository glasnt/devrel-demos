# Running MKDocs on Cloud Run

To deploy a [MKDocs](https://www.mkdocs.org/) application to Cloud Run, you will need an application
based on this framework. This demo gets you to use the MKDocs template to generate one. 

This requires [python3](https://cloud.google.com/python/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install).


### Create template application


* Install the framework:

    ```bash
    pip install mkdocs
    ```

* Create a new template application:

    ```bash
    mkdocs new helloworld
    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    mkdocs serve
    ```

    

    Enter `Ctrl+C` or `CMD+C` to stop the process.


## Configure for Cloud Run

Using [Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks), 
the base language is automatically identified.



For python applications, you can specify what you want the web process to run using a `Procfile`. 

* Create a new file called `Procfile` with the following contents: 

    ```
    web: mkdocs serve
    ```






## Deploy to Cloud Run

* Build and deploy the service to Cloud Run: 


    ```bash
    gcloud run deploy mkdocs-helloworld \
        --source . \
        --allow-unauthenticated 
    ```

    Type "Y" for all suggested operations.


Your service will now be deployed at the URL in the deployment output.

![Example MKDocs deployment](example.png)





## Learn more

Resources: 

- https://www.mkdocs.org/getting-started/
