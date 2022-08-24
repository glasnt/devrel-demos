# Running Preact on Firebase

<!--- Generated 2022-08-24 06:43:53.362368 -->

To deploy a [Preact](https://preactjs.com/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Preact template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


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




## Deploy to Firebase

* Generate the application: 

    ```bash
    npm run build
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "build" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://preactjs.com/guide/v10/getting-started
