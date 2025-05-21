# The following tips can help in requests performance

1. Timeout control
   > by default requests waits untill the response comes back and this can take forever, so using timeout function and specifying the amount of time could improve perfomance and user experience

  eg. requests.get("www.google.com",timeout = 1) time of one seconds

  > also can specify the connection timeout and read timeout by passing timeout as turple
   eg. requests.get("www.google.com",timeout = (connection_timeout,read_timeout)) Note: this can be interger or float

   If the there is timeout, requests will raise a timeout error
   so, from requests.exceptions import Timeout

2. Handling sessions
   Lets say you want to persist same authentication across multiple requests, then sessions could be used here

   example:
   with requests.Session() as session:
        session.auth = auth(token)
        // requests 
         session.get(url)

    // using with(context manager ) ensures sessions releases resourse when requests are done  

3. Max Retries
   This defines how many times the request can retry after failing to connect, The easier way of setting this is by using Transport Adapters

   eg. we can specify the request to retry 2times before raising RetryError
        import requests
        from requests.adapters import HTTPAdapter
        from requests.exceptions import RetryError
        github_adapter = HTTPAdapter(max_retries=2)
        session = requests.Session()
        session.mount("https://api.github.com", github_adapter)

        > the code above retries 2 for given github url
