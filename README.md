Minimal skeleton for a Python server on Google App Engine

#Run locally
git clone https://github.com/ThomasJannaud/appengine_python_skeleton.git
python -m venv env
source env/bin/activate
pip install  -r requirements.txt
python main.py

#Deploy
yes | gcloud app deploy   --project PROJECTNAME
https://PROJECTNAME.appspot.com/