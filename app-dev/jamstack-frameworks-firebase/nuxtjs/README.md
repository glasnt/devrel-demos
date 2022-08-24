# Running Nuxtjs on Firebase

<!--- Generated 2022-08-24 06:42:26.216936 -->

To deploy a [Nuxtjs](https://nuxtjs.org/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Nuxtjs template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Generate a new template application: 

    ```bash
    npx create-nuxt-app helloworld
    # Choose defaults for all options, including "Deployment Target" (which will be "Server (Node.js hosting)")

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
    # Choose "." for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://nuxtjs.org/docs/get-started/installation
- https://nuxtjs.org/docs/get-started/commands
