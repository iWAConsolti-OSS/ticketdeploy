

# Requirements

1. python 2.7
    Note:  If you have problems  with python 2.7 you can use python 3 instead
2. you will need an Atlassian token to be able to make calls to the Atlassian API

https://confluence.atlassian.com/cloud/api-tokens-938839638.html?_ga=2.81595986.490835099.1581793170-669039767.1560669643

# Installation and use

1. Create the following environment variables in your system

``` sh
    ATLASSSIAN_BASE_URI=https://myaccount.atlassian.net
    ATLASSIAN_USER=user
    ATLASSIAN_API_KEY=apiKey
    TICKETS_TO_DEPLOY=query
```

2. Install the required components

``` sh
    pip install -r requirements.txt
``` 

3. run 

``` sh
    python main.py
``` 


# Bitbucket API

``` sh
    curl -u user:passw \
        -i -X GET https://api.bitbucket.org/internal/repositories/{org}/{repo}/environment_summaries/

    curl -u user:passw \
        -i -X GET https://api.bitbucket.org/internal/repositories/{org}/{repo}/jira-issues?exclude=29983d7&include=f3a53b9&fields=-type


    curl -u user:passw \
        -i -X GET https://api.bitbucket.org/2.0/repositories/
```
