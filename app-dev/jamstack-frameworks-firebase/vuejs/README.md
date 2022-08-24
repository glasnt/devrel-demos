# Running VueJS on Firebase

<!--- Generated 2022-08-24 06:52:10.100687 -->

To deploy a [VueJS](https://vuejs.org/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the VueJS template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


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




## Deploy to Firebase

* Generate the application: 

    ```bash
    npm run build
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "dist/" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://vuejs.org/guide/quick-start.html
- https://vuejs.org/guide/best-practices/production-deployment.html
