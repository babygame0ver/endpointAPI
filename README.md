# flask

Requirements

```
pip install flask
```

---

## Tutorials List :

* Flask Mega Tutorial : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis

## Concepts : 

* Custom Error Message with error handler in flask : https://stackoverflow.com/questions/21294889/how-to-get-access-to-error-message-from-abort-command-when-using-custom-error-ha

* Flask HTTP methods : https://www.tutorialspoint.com/flask/flask_http_methods.htm

---

Repository topics guide :

1. [flask-rest-api](1-flask-rest-api/)
    
    Link : http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    
    [include](1-flask-respt-api/1-flask-rest-api/1-flask-hello-world.py)
    
    To test these urls Use CURL commands:
    ```
    curl -i http://127.0.0.1:5000/restapi
    curl -i -H "Content-Type: application/json" -X POST -d '{"task_id":2}' http://127.0.0.1:5000/restapi/create
    ```


