# Running Gatsby on Cloud Run

To deploy a [Gatsby](https://www.gatsbyjs.com/) application to Cloud Run, you will need an application
based on this framework. This demo gets you to use the Gatsby template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install).


### Create template application


* Generate a new template application: 

    ```bash
    npm init gatsby
    # Use "helloworld" for the project, enter for all other defaults, don't install any extras.

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    npm run develop
    ```

    

    Enter `Ctrl+C` or `CMD+C` to stop the process.


## Configure for Cloud Run

Using [Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks), 
the base language is automatically identified.


For Node applications, it will automatically run `npm start` as the entrypoint if no other command is defined. 



You can override this using a `Procfile`. 

* Create a new file called `Procfile` with the following contents: 

    ```
    web: npm run develop
    ```






## Deploy to Cloud Run

* Build and deploy the service to Cloud Run: 


    ```bash
    gcloud run deploy gatsby-helloworld \
        --source . \
        --allow-unauthenticated 
    ```

    Type "Y" for all suggested operations.


Your service will now be deployed at the URL in the deployment output.

![Example Gatsby deployment](example.png)





## Learn more

Resources: 

- https://www.gatsbyjs.com/docs/quick-start/
- https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting#additional
