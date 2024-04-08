# Food Delivery Service Management Software Testing

steps to run the code

- download the code
- create and activate virtual environment using

```
python -m venv venv
# on linux and mac
source ./venv/bin/activate
# on windows
./venv/Scripts/activate
```

- Install requirements using

```
pip install -r requirements.txt
```

- Add .env file with following variables
  - MONGOURI
  - TEST_DB_NAME
  - BACKEND_API_URL
- Create the directory add_data/test_data

- Run the tests as

```
python main.py
```
