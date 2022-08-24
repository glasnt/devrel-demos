# Running Express on Firebase

<!--- Generated 2022-08-24 06:28:16.941323 -->

To deploy a [Express](https://expressjs.com/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Express template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Generate a new template application: 

    ```bash
    npx express-generator helloworld
    cd helloworld
    npm install

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    npm start
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://expressjs.com/en/starter/generator.html
