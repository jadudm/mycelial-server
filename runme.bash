workon mycelial-mural
pip install -r requirements.txt
pip install -e mural

gunicorn mycelial:app