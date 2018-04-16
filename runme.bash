source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv mycelial-mural
workon mycelial-mural
pip install -r requirements.txt
pip install -e mural

gunicorn -w 3 -b 0.0.0.0:4000 mycelial:app
