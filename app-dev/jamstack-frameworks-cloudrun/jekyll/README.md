# Running Jekyll on Cloud Run

To deploy a [Jekyll](https://jekyllrb.com/) application to Cloud Run, you will need an application
based on this framework. This demo gets you to use the Jekyll template to generate one. 

This requires [ruby](https://cloud.google.com/ruby/docs/setup), and [gcloud](https://cloud.google.com/sdk/docs/install).



To complete this demo, you will need a [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project). 


### Create template application


* Install the framework:

    ```bash
    gem install bundler jekyll
    ```

    
    

* Create a new template application:

    ```bash
    jekyll new helloworld
    cd helloworld
    echo "gem 'webrick'" >> Gemfile
    bundle install

    ```




* Run the application locally:

    ```bash
    bundle exec jekyll serve
    ```

    

    Enter `Ctrl+C` or `CMD+C` to stop the process.


## Configure for Cloud Run

Using [Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks), 
the base language is automatically identified.



For ruby applications, you can specify what you want the web process to run using a `Procfile`. 

* Create a new file called `Procfile` with the following contents: 

    ```
    web: bundle exec jekyll serve
    ```






## Deploy to Cloud Run

* Set the project you created earlier in `gcloud`: 

    ```bash
    gcloud config set project MYPROJECT
    ```

* Build and deploy the service to Cloud Run: 

    ```bash
    gcloud run deploy jekyll-helloworld \
        --source . \
        --allow-unauthenticated 
    ```

    Type "Y" for all suggested operations.


Your service will now be deployed at the URL in the deployment output.

![Example Jekyll deployment](example.png)





## Learn more

Resources: 

- https://jekyllrb.com/docs/
- https://jekyllrb.com/docs/usage/
