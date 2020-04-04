# Google AppEngine: Minimal skeleton of a Python server
A minimal Flask server serving static HTML pages that deploys seamlessly to Google AppEngine, no troubleshooting needed. It also boasts a minimal HTML template skeleton in [Jinja](https://jinja.palletsprojects.com/).

As of April 2020, GAE runs your server for free as long as you are under a million visits a day or so. You only need to purchase the domain name, and that's optional if you can be content with PROJECTNAME.appspot.com. This github repo doesn't cover this, GAE's instruction are pretty complete for that.

# Instructions

Run your server locally. When you are happy with the result, deploy to Google AppEngine (you will need to setup that account) and your website will be on internet.

## Install

Install part, one time only.

```
git clone https://github.com/ThomasJannaud/appengine_python_skeleton.git
python -m venv env
source env/bin/activate
pip install  -r requirements.txt  # Re-run this if you add libraries
```

## Run your website locally

Most of this skeleton consists of a minimal Flask server for you to customize.  
Edit the webpages in the `Templates/` folder and style them in the `static/` folder.  
Change the logic in `page_handler.py` to serve more urls or in `main.py` to serve anything else than static pages.  


To run, you only need:
```
python main.py
```

The server is now running on localhost:8080. Just navigate to either one of:
- localhost:8080
- localhost:8080?name=Thomas
- localhost:8080/contact

The nice thing about Flask is that you can update your HTML templates or your Python code and Flask should take the changes into account without restarting the server.


## Deploy

You need to have a [GAE account](https://cloud.google.com/appengine) and create a project there.
Your website will be hosted on https://PROJECTNAME.appspot.com but if you own a domain you can point it to this host.

Follow the instructions as you install gcloud to validate your credentials. Then run

`gcloud app deploy --project PROJECTNAME`

to deploy. The setup might take time but once it is ready one command line is enough.