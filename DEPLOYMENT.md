# Deployment

There are a multitude of ways to deploy your app to the web. I am going to focus on two ways here: Using Heroku, and using PythonAnywhere.

# Heroku Deployment

Heroku is a very popular platform for web app deployment. It is simple to setup, and can continuously update the web app with every commit to a version control service (e.g. GitHub). 

## Outline

This outline assumes that you have your project already hosted on [GitHub], and that everything goes smoothly.

[GitHub]: https://github.com/

1. Sign up for an account at [Heroku].
1. Create a new project and note the URL that it will have.
1. Configure your project in the following ways:
    1. **Deployment method**: GitHub
    1. **App connected to GitHub**: Put in your project repository name.
    1. **Automatic deploys**: Select "master" as the branch to deploy from. 
1. Create your [procfile]. For more information, click the link to read more. If you only need a refresher, read the **Procfile** section below.
1. Push your app to GitHub, and wait for it to deploy on Heroku!

[Heroku]: https://www.heroku.com
[procfile]: https://devcenter.heroku.com/articles/procfile

## Procfile

Here's what the Procfile looks like for this project.

```
web: gunicorn app:app
```

This tells Heroku to tell `gunicorn` to execute my `app.py` file.
