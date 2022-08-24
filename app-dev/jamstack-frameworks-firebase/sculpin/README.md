# Running Sculpin on Firebase

<!--- Generated 2022-08-24 06:26:55.800786 -->

To deploy a [Sculpin](https://sculpin.io) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Sculpin template to generate one. 

This requires [php](https://www.php.net/manual/en/install.php), and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Generate a new template application: 

    ```bash
    brew install composer
    composer create-project sculpin/blog-skeleton helloworld

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    vendor/bin/sculpin generate --watch --server
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    vendor/bin/sculpin generate
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "output_dev" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://sculpin.io/getstarted/
