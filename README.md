# calendly_api

# path

  login in api 
  generate token for further use
  test your token 
  After you use further

# authentication
  After generating a token, you need to pass an Authorization header to the Github API. Just like the server sends us headers in response to our request, we can send the server headers when we make a request. Headers contain metadata about the request. With the requests library, we just make a dictionary of headers, and then pass it into the request when we make it
  
  {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}
  
# Endpoints and objects
  APIs are usually setup to let you retrieve information about specific objects in the database.

# status codes
The request we just made had a status code of 200. Status codes are returned with every request that is made to a web server. Status codes indicate information about what happened with a request. Here are some codes that are relevant to GET requests:

200 -- everything went okay, and the result has been returned (if any)</br>
301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.</br>
401 -- the server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).</br>
400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.</br>
403 -- the resource you're trying to access is forbidden -- you don't have the right permissions to see it.</br>
404 -- the resource you tried to access wasn't found on the server.</br>
  
# Get request Example
import requests
response = requests.get("url-here", headers=headers)
hello_world = response.json()
print("hello_world:", hello_world)

# Post Request
payload = {"name": "learning-about-apis"}
response = requests.post("url here", json=payload, headers=headers)
status = response.status_code
print("response.status_code:", response.status_code)

