# flask

Requirements

```
pip install flask
```

Tutorials resources:


* [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis) : Complete Series in flask development

---

Repository topics guide :

1. [flask-rest-api](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis) : [Source Code](1-flask-rest-api/)

    To test these urls Use CURL commands:
    ```
    curl -i http://127.0.0.1:5000/restapi
    curl -i -H "Content-Type: application/json" -X POST -d '{"task_id":2}' http://  127.0.0.1:5000/restapi/create
    ```

---

Questions and More features:

1. [Custom Error Message](https://stackoverflow.com/questions/21294889/how-to-get-access-to-error-message-from-abort-command-when-using-custom-error-ha)

2. [Flask HTTP methods](https://www.tutorialspoint.com/flask/flask_http_methods.htm)
