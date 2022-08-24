# Running Lektor on Firebase

<!--- Generated 2022-08-24 06:38:12.328752 -->

To deploy a [Lektor](https://www.getlektor.com) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Lektor template to generate one. 

This requires [python3](https://cloud.google.com/python/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Install the framework:

    ```bash
    pip install lektor
    ```

* Create a new template application:

    ```bash
    lektor quickstart
    # enter "helloworld" for project name, and accept all other defaults. 

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    lektor server
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    lektor build -O output
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "output" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://www.getlektor.com/docs/quickstart/
