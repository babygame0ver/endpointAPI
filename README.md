# flask

Requirements

```
pip install flask
```

---

## Tutorials / Resources / Projects :

* Flask Mega Tutorial : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis

* Flask CheatSheet : https://github.com/detailyang/awesome-cheatsheet#back-end-development

* JWT Authentication with Python and Flask : polyglot.ninja/jwt-authentication-python-flask/

* JWT authorization in Flask : https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb

* project-based-learning : https://github.com/tuvtran/project-based-learning#python

* RESTful Authentication with Flask : https://blog.miguelgrinberg.com/post/restful-authentication-with-flask

* Scalable web Applications : https://www.youtube.com/playlist?list=PLdqn_b7Fi_PSKAeO5F8wmA3YmXOtL5wAA

* Securing REST APIs: Basic HTTP Authentication with Python / Flask : http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/

* Understanding JSON web tokens : polyglot.ninja/understanding-jwt-json-web-tokens/

---

## My Projects :

1. [flask-rest-api](1-flask-rest-api/)

    Link : http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


    To test these urls Use CURL commands:
    ```
    curl -i http://127.0.0.1:5000/restapi
    curl -i -H "Content-Type: application/json" -X POST -d '{"task_id":2}' http://127.0.0.1:5000/restapi/create
    ```

---

## Concepts :

* Custom Error Message with error handler in flask : https://stackoverflow.com/questions/21294889/how-to-get-access-to-error-message-from-abort-command-when-using-custom-error-ha

* Flask HTTP methods : https://www.tutorialspoint.com/flask/flask_http_methods.htm

* How to get http headers in flask? : https://stackoverflow.com/questions/29386995/how-to-get-http-headers-in-flask

---
