# ascend.client

Ascend Client module

The Client module of the Ascend SDK manages an API connection to
an Ascend environment.

## Client
```python
Client(self, environment_hostname, access_key=None, secret_key=None, verify=True)
```

Ascend SDK Client object.

The Client object maintains a connection to an Ascend host on behalf of
a Service Account defined in an Ascend Data Service. Authentication is
via Access Keys, generated by Ascend and linked to the Service Account.

Access Keys should be maintained in a secure location and not embedded
in the client script.
One method of managing keys is by using `configparser`.

```python
from ascend.client import Client
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.ascend/credentials"))

access_id = config.get("trial", "ascend_access_key_id")
secret_key = config.get("trial", "ascend_secret_access_key")

A = Client("trial.ascend.io", access_id, secret_key)
```

__Parameters__


- __environment_hostname (str)__:
    Hostname on which the Ascend environment you wish connect to is deployed
- __access_key (str)__:
    Access Key ID you wish to use to authenticate with Ascend
- __secret_key (str)__:
    Secret Access Key to use to authenticate with Ascend
- __verify (bool)__:
    Verify the server's SSL certificate
    (default is `True`)

### get_session
```python
Client.get_session(self)
```

Get the Session object which the Client uses to make API requests.

__Returns__

`ascend.session.Session`: the `Session` object

### list_data_services
```python
Client.list_data_services(self, raw=False)
```

List the Data Services which this Client may access.

__Returns__

`List<ascend.model.DataService>`:
    `DataService` objects, one for each accessible Data Service

__Raises__

- `HTTPError`: for errors returned by API

### get_data_service
```python
Client.get_data_service(self, data_service_id: str) -> ascend.model.DataService
```

Get a Data Service.

__Parameters__

- __data_service_id (str)__: the ID of the Data Service

__Returns__

`ascend.model.DataService`: the Data Service

__Raises__

- `HTTPError`: for errors returned by API

### get_dataflow
```python
Client.get_dataflow(self, data_service_id: str, dataflow_id: str) -> ascend.model.Dataflow
```

Get a Dataflow within a Data Service.

__Parameters__

- __dataservice_id (str)__: the ID of the Data Service
- __dataflow_id (str)__: the ID of the Dataflow

__Returns__

`ascend.model.Dataflow`: the Dataflow

__Raises__

- `HTTPError`: for errors returned by API

### get_component
```python
Client.get_component(self, data_service_id: str, dataflow_id: str, component_id: str) -> ascend.model.Component
```

Get a Component within a Dataflow.

__Parameters__

- __dataservice_id (str)__: the ID of the Data Service
- __dataflow_id (str)__: the ID of the Dataflow
- __component_id (str)__: the ID of the Component

__Returns__

`ascend.model.Component`: the Component

__Raises__

- `HTTPError`: for errors returned by API

### list_data_feeds
```python
Client.list_data_feeds(self, source_data_service_id=None, raw=False)
```

List the Data Feeds which are available to the Client's Service Account.

__Parameters__

- __source_data_service_id (str)__:
    the ID of a Data Service, which if given will limit the
    Data Feeds to those produced by the Data Service.
    (default is `None`)

__Returns__

`List<ascend.model.DataFeed>`: the Data Feeds

### get_data_feed
```python
Client.get_data_feed(self, data_service_id, data_feed_id, raw=False)
```

Get a Data Feed.

__Parameters__

- __data_service_id (str)__:
    the ID of the Data Service producing the Data Feed
- __data_feed_id (str)__:
    the ID of the Data Feed. Must be unique within Data Service.

__Returns__

`ascend.model.DataFeed`: the Data Feed

# ascend.session

Ascend Session module

The Session module encapsulates an HTTP session, and adds authentication.
All API requests pass through the Session.

## Session
```python
Session(self, environment_hostname, access_key, secret_key, verify=True)
```

Session implements an authenticated HTTP session to an Ascend host,
including handling token exchange.

__Parameters__

- __environment_hostname (str)__:
    hostname on which the Ascend environment you wish connect to is deployed
- __access_key (str)__:
    Access Key ID you wish to use to authenticate with Ascend
- __secret_key (str)__:
    Secret Access Key to use to authenticate with Ascend
- __verify (bool)__:
    verify the server's SSL certificate
    (default is `True`)

### delete
```python
Session.delete(self, endpoint)
```

Make a DELETE request

__Parameters__

- __endpoint (str)__:
    the partial URL of the request (does not include hostname or API prefix)

__Returns__

`int`: the HTTP response code status

### get
```python
Session.get(self, endpoint, query=None)
```

Make a GET request.

__Parameters__

- __endpoint (str)__:
    the partial URL of the request (does not include hostname or API prefix)
- __query (dict)__:
    query parameters to send with the request

__Returns__

`dict`: the parsed JSON response

### patch
```python
Session.patch(self, endpoint, data=None)
```

Make a PATCH request.

__Parameters__

- __endpoint (str)__:
    the partial URL of the request (does not include hostname or API prefix)
- __data (dict)__:
    JSON to send in the request body

__Returns__

`int`: the HTTP response status code

### post
```python
Session.post(self, endpoint, data=None)
```

Make a POST request.

__Parameters__

- __endpoint (str)__:
    the partial URL of the request (does not include hostname or API prefix)
- __data (dict)__:
    JSON to send in the request body

__Returns__

`int`: the HTTP response status code

### stream
```python
Session.stream(self, endpoint, query=None)
```

Make a GET request and process the results as a stream of JSON lines

__Parameters__

- __endpoint (str)__:
    the partial URL of the request (does not include hostname or API prefix)
- __query (dict)__:
    query parameters to send with the request

__Returns__

`Iterator<dict>`: an iterator over the parsed JSON lines

# ascend.auth

Ascend Auth module

The Auth module is responsible for authenticating Access Keys with the
Ascend environment, and negotiating the token exchange protocol.

The Access Keys and the token exchange algorithm conform to AWS V4 Auth,
but the keys used will be generated and authenticated by Ascend, not AWS.

