# Running Flutter on Firebase

To deploy a [Flutter](https://flutter.dev/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Flutter template to generate one. 

This requires Flutter, and [firebase](https://cloud.google.com/firestore/docs/client/get-firebase).


### Create template application


* Install the framework:

    ```bash
    # https://docs.flutter.dev/get-started/install

    ```

* Create a new template application:

    ```bash
    flutter create helloworld
    cd helloworld
    flutter devices

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    flutter run
    ```

    

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    flutter build web
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "build/web" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://docs.flutter.dev/get-started/web
