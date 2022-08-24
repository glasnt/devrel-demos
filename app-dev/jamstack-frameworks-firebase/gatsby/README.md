# Running Gatsby on Firebase

To deploy a [Gatsby](https://www.gatsbyjs.com/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Gatsby template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Generate a new template application: 

    ```bash
    npm init gatsby
    # Use "helloworld" for the project, enter for all other defaults, don't install any extras.

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    npm run develop
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
    # Choose "public" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://www.gatsbyjs.com/docs/quick-start/
- https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting#additional
