# Deployment

There are a multitude of ways to deploy your app to the web. I am going to focus on two ways here:

- [Heroku]
- [PythonAnywhere]

[PythonAnywhere]: https://www.pythonanywhere.com/


# Heroku Deployment

Heroku is a very popular platform for web app deployment. It is simple to setup, and can continuously update the web app with every commit to a version control service (e.g. GitHub). 

**Advantages of Heroku**:

- Easy to setup; no need to fiddle with web server stuff.
- Free
- URL is http://`mydomain`.herokuapp.com/, which is not bad for branding. It's not tied to your username like PythonAnywhere.

**Disadvantages of Heroku**:

- No persistent disk storage, i.e. cannot store databases unless it's part of `git` repo (bad, bad, bad idea).
- Free tier goes to sleep after 30 min. of activity; first load can take some time.

## Project URL

This project's "display table" can be found online [here][minimaltable].

[minimaltable]: https://minimal-flask-table.herokuapp.com/

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
1. Run `git push heroku master` to deploy your app to the web!

## Other Configurations

You can do other configurations on your web [dashboard].

[dashboard]: https://dashboard.heroku.com/apps

### Deployment from GitHub

1. Open your project. 
1. Click on the `Deploy` tab.
1. Look for "Deployment method". Click on "GitHub".
1. If you haven't already connected GitHub to your Heroku account, do so now.
1. The bottom of the page will change to "Connect to GitHub". Type in the name of your repository name and click "Search".
1. When your repository name shows up, click "Connect" next to it.
1. The bottom of the page will now show, "Automatic deploys". Make sure the `master` branch is selected, and that you have clicked on "Enable Automatic Deploys".
1.  

Now, each time you git push to GitHub, Heroku will automatically pull in your GitHub repository and deploy it. No need to type a separate `git push heroku master` command anymore - laziness at its best!

[Heroku CLI]: https://devcenter.heroku.com/articles/getting-started-with-python#set-up
[Heroku]: https://www.heroku.com
[procfile]: https://devcenter.heroku.com/articles/procfile

## Procfile

Here's what the Procfile looks like for this project.

```
web: gunicorn app:app
```

This tells Heroku to tell `gunicorn` to execute my `app.py` file.

--------

# PythonAnywhere

PythonAnywhere is another service that is great for Python web app deployment.
**Advantages of PythonAnywhere**:

- Free
- Provides (limited) storage, so it's useful if your app needs to retrieve a database.
- Provides a console through which you can `git clone` and `git pull` updates to your app.

**Disadvantages of PythonAnywhere**:

- Not as many convenience functions provided as Heroku.
- Project URL is https://`myusername`.pythonanywhere.com. Not as good for branding.

## Project URL

This project can be found at: http://ericmjl.pythonanywhere.com/

## Outline

This outline is briefer, but it provides the set of instruction pages to follow in order.

1. Make sure your Python app is deployed to a version control system, i.e. GitHub.
1. Open a new `bash` console in PythonAnywhere.
1. `git clone` your repository using HTTPS (not SSH). For example, this project wouuld be cloned using `$ git clone https://github.com/ericmjl/minimal-flask-example`. 
1. Create a virtual environment using `$ mkvirtualenv --python=/usr/bin/python3.6 "myappname"`.
    1. If there's an issue with `mkvirtualenv`, follow the commands [here][mkvenv].
    1. In the future, if you want to activate the virtual environment, PythonAnywhere provides an alternate command to activate it: `$ workon my-virtualenv`.
1. Install all required packages: `$ pip install -r requirements.txt`.
1. Follow the instructions on the [Flask tutorial] page under the title, "Setting up the Web app using Manual configuration".
1. **Instructions to be continued live...**

[Flask tutorial]: https://help.pythonanywhere.com/pages/Flask/

[mkvenv]: https://help.pythonanywhere.com/pages/InstallingVirtualenvWrapper
