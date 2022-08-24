# Running MKDocs on Firebase

<!--- Generated 2022-08-24 06:28:16.961124 -->

To deploy a [MKDocs](https://www.mkdocs.org/) application to Firebase, you will need an application
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




## Deploy to Firebase

* Generate the application: 

    ```bash
    mkdocs build
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "site" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://www.mkdocs.org/getting-started/
