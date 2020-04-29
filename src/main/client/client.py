import requests
requests.post("http://localhost:5000/todo", 
                  json={"Title":"my first todo", 
                        "Description":"my first todo"})