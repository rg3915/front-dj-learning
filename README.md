# front-dj-learning

Test Ajax and others Front End functions in Django Project.


## How to contribute?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/front-dj-learning.git
cd front-dj-learning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```