# Running Jekyll on Firebase

<!--- Generated 2022-08-24 06:26:55.784592 -->

To deploy a [Jekyll](https://jekyllrb.com/) application to Firebase, you will need an application
based on this framework. This demo gets you to use the Jekyll template to generate one. 

This requires , and [gcloud](https://cloud.google.com/sdk/docs/install). 

### Create template application


* Install the framework:

    ```bash
    gem install bundler jekyll
    ```

* Create a new template application:

    ```bash
    jekyll new helloworld
    ```




* Navigate to the created project:

    ```bash
    cd helloworld/
    ```

* Run the application locally:

    ```bash
    bundle exec jekyll serve
    ```

    Enter `Ctrl+C` or `CMD+C` to stop the process.




## Deploy to Firebase

* Generate the application: 

    ```bash
    bundle exec jekyll build
    ```

* Setup Firebase: 

    ```bash
    firebase init hosting
    # Choose "_site" for the "public directory".
    ```

* Deploy to Firebase: 

    ```bash
    firebase deploy --only hosting
    ```



## Learn more

Resources: 

- https://jekyllrb.com/docs/
- https://jekyllrb.com/docs/usage/
