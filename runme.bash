source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv mycelial-mural
workon mycelial-mural
pip install --user -r requirements.txt
pip install --user -e mural

gunicorn -w 3 -b 0.0.0.0:8080 mycelial:app
