# Running Angular on Firebase

<!--- Generated 2022-08-24 06:26:55.773589 -->

To deploy a [Angular](https://angular.io/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Angular template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Install the framework:

    ```bash
    npm install -g @angular/cli
    ```

* Create a new template application:

    ```bash
    ng new helloworld
    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    ng serve --open
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    ng build
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "dist/helloworld" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://angular.io/tutorial/toh-pt0
- https://angular.io/start/start-deployment
