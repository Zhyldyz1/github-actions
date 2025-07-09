## Run App Locally


1. Change Directory to app folder 


```
cd app
```


2. Create a virtual environment named 'app-venv'


```
python3 -m venv app-venv
```


3. Activate the virtual environment


```
source app-venv/bin/activate
```


4. Install dependencies


```
pip install -r requirements.txt
```


5. Run application


```
python main.py
```


6. Run Pytest


```
pytest
```


7. Quit App - Press CTRL+C to quit


8. Deactivate the Virtual Environment 


```
deactivate
```


9. Delete the virtual environment folder 'app-venv'


```
rm -rf app-venv
rm -rf .pytest_cache
rm -rf ../.pytest_cache
```