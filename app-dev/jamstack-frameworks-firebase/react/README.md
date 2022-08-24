# Running React on Firebase

<!--- Generated 2022-08-24 06:43:53.364306 -->

To deploy a [React](https://reactjs.org/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the React template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Generate a new template application: 

    ```bash
    npx create-react-app helloworld
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

- https://create-react-app.dev/docs/getting-started
- https://create-react-app.dev/docs/deployment
