# Conf·ident·ify client for Python

This project provides a Python client for the [Conf·ident·ify](https://confidentify.com) APIs. 

[![Build Status: Linux](https://travis-ci.org/confidentify/confidentify-client-python.svg?branch=master)](https://travis-ci.org/confidentify/confidentify-client-python)

## Using the client

First, add the project as a Maven dependency in your project:

```
pip install confidentify-client-python
```

Next, start coding against the packages `confidentify_client`, `confidentify_client.api` and `confidentify_client.models`.

Here's an example which assumes you have your account username/password in variables with corresponding names:

```python
from confidentify_client import ApiClient
from confidentify_client.api import AuthApi, ProcessApi
from confidentify_client.models import AuthRequest, PersonNameRequest, PersonNameRequestRecord

with ApiClient() as api_client:
    # Authenticate
    auth_response = AuthApi(api_client).auth_post(AuthRequest(username, password))
    access_token = auth_response.access_token
    api_client.configuration.access_token = access_token

    # Use the 'process' API
    process_api = ProcessApi(api_client)
```

## Testing

The tests in this project are integration tests, that require credentials. Provide the credentials using these environment variables:

 * `CONFIDENTIFY_USERNAME`
 * `CONFIDENTIFY_PASSWORD`
