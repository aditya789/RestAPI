# RestAPI
 
Steps to install the project in local machines

-- create virtutal environment using below command
python -m venv env   

-- activate the env using below command
source env/bin/activate

-- install packages using pip by below

pip install -r requirements.txt

-- do the following migrations and the run server
python manage.py migrate
python manage.py runserver 


--- Test the end points by pasting them in browser
Samples -
http://localhost:8000/api/v1/location/
http://localhost:8000/api/v1/sku/match/
