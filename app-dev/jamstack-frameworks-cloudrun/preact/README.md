# Running preact on Cloud Run

<!--- Generated 2022-08-24 05:21:43.322305 -->

To deploy a [preact](https://preactjs.com/) application to Cloud Run, you will need an application
based on this framework. This demo gets you to use the preact template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Generate a new template application: 

    ```bash
    npx preact-cli create default helloworld
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


For Node applications, it will automatically run `npm start` as the entrypoint if no other command is defined. 



You can override this using a `Procfile`. 

* Create a new file called `Procfile` with the following contents: 

    ```
    web: npm run dev
    ```







## Deploy to Cloud Run

* Build and deploy the service to Cloud Run: 


    ```bash
    gcloud run deploy preact-helloworld \
        --source . \
        --allow-unauthenticated 
    ```

    Type "Y" for all suggested operations.


Your service will now be deployed at the URL in the deployment output.

![Example preact deployment](example.png)

## Learn more

Resources: 

- h
- t
- t
- p
- s
- :
- /
- /
- p
- r
- e
- a
- c
- t
- j
- s
- .
- c
- o
- m
- /
- g
- u
- i
- d
- e
- /
- v
- 1
- 0
- /
- g
- e
- t
- t
- i
- n
- g
- -
- s
- t
- a
- r
- t
- e
- d
