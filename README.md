# Google AppEngine: Minimal skeleton of a Python server

Most of this skeleton consists in a minimal Flask server for you to customize.  
Edit the webpages in the Templates/ folder and style them in the static/ folder.  
Change the logic in page_handler.py to serve more urls.

## Run locally

git clone https://github.com/ThomasJannaud/appengine_python_skeleton.git
python -m venv env
source env/bin/activate
pip install  -r requirements.txt
python main.py

The server is now running on localhost:8080. Just navigate to either one of:
- localhost:8080
- localhost:8080?name=Thomas
- localhost:8080/contact


## Deploy

You need to have a GAE account and create a project there.
Your website will be hosted on https://PROJECTNAME.appspot.com but if you own a domain you can point it to this host.

yes | gcloud app deploy --project PROJECTNAME
