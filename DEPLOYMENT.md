# Deployment

There are a multitude of ways to deploy your app to the web. I am going to focus on two ways here: Using Heroku, and using PythonAnywhere.

# Heroku Deployment

Heroku is a very popular platform for web app deployment. It is simple to setup, and can continuously update the web app with every commit to a version control service (e.g. GitHub). 

## Outline

This outline assumes that you have your project already hosted on [GitHub], and that everything goes smoothly.

[GitHub]: https://github.com/

1. Sign up for an account at [Heroku].
1. Install the [Heroku CLI], and then login.
1. `cd` into your project directory.
1. Make sure that you have a `requirements.txt` file, which specifies the versions of Python packages that you are using.
    1. You can use `pipreqs`, a Python package for automatically determining your Python package requirements, to create the `requirements.txt` file. 
1. Be sure to add `gunicorn` to `requirements.txt`. 
1. Run the command `heroku create "myprojectname"`, to create a new Heroku project based off your current project directory, with the project name being "`myprojectname`".
1. Confirm that there is a `heroku` remote by running the command `$ git remote -v`.
1. Create your [procfile]. For more information, click the link to read more. If you only need a refresher, read the **Procfile** section below.
1. Create a `runtime.txt` file, which specifies the Python version for Heroku to use.
1. Run `git push heroku master` 


1. Configure your project in the following ways:
    1. **Deployment method**: GitHub
    1. **App connected to GitHub**: Put in your project repository name.
    1. **Automatic deploys**: Select "master" as the branch to deploy from. 
1. Push your app to GitHub, and wait for it to deploy on Heroku!

[Heroku CLI]: https://devcenter.heroku.com/articles/getting-started-with-python#set-up
[Heroku]: https://www.heroku.com
[procfile]: https://devcenter.heroku.com/articles/procfile

## Procfile

Here's what the Procfile looks like for this project.

```
web: gunicorn app:app
```

This tells Heroku to tell `gunicorn` to execute my `app.py` file.
