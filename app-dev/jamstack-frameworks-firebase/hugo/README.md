# Running Hugo on Firebase

<!--- Generated 2022-08-24 06:28:16.950219 -->

To deploy a [Hugo](https://gohugo.io) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Hugo template to generate one. 

This requires [go](https://cloud.google.com/go/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Install the framework:

    ```bash
    # https://gohugo.io/getting-started/installing

    ```

* Create a new template application:

    ```bash
    hugo new site helloworld
    hugo new posts/hello.md
    git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
    echo theme = \"ananke\" >> config.toml
    sed -i "" "s/true/false/g" content/posts/hello.md

    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    hugo serve -D
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    hugo -D
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

- https://gohugo.io/getting-started/quick-start/
