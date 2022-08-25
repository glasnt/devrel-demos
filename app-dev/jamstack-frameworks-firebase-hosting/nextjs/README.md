# Running NextJS on Firebase

To deploy a [NextJS](https://nextjs.org/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the NextJS template to generate one. 

This requires [node, npm](https://cloud.google.com/nodejs/docs/setup), and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).



To complete this demo, you will need a Firebase project.
You can [create a new one](https://console.firebase.google.com/u/0/?pli=1), or connect an existing [Google Cloud project](https://cloud.google.com/firestore/docs/client/get-firebase). You can also 


### Create template application


* Generate a new template application: 

    ```bash
    npx create-next-app@latest helloworld
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
    ```

    * Select the Google Cloud project you configured earlier.
    * Choose "." for the "public directory".
    * Chosoe the default for all other options.

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```

Your service will now be deployed at the URL in the output under "Hosting URL".

![Example NextJS deployment](example.png)



## Learn more

Resources: 

- https://nextjs.org/learn/basics/create-nextjs-app/setup
- https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore
