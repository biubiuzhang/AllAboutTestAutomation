## API Testing with Python

```
import requests

base_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(base_url)
response.json() # return a dictonary with responses
response.text # return a string with responses
response.status_code # return status code like 200
response.headers # return a dictonary with headers
```
