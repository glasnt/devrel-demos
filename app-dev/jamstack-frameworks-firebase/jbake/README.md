# Running JBake on Firebase

<!--- Generated 2022-08-24 06:43:53.346741 -->

To deploy a [JBake](https://jbake.org/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the JBake template to generate one. 

This requires `java`
, and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Install the framework:

    ```bash
    curl -s "https://get.sdkman.io" | bash
    sdk install jbake

    ```

* Create a new template application:

    ```bash
    mkdir helloworld && cd helloworld
    jbake -i

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    jbake -b -s
    ```

    

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    jbake -b
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

- https://jbake.org/
