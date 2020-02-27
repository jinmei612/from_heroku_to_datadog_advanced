# Distributed Tracing

You should have one heroku webapp running after this exercise: https://github.com/jinmei612/from_heroku_to_datadog

Now, let's create another heroku webapp using the files in this repo. (Change the URL [here](https://github.com/jinmei612/from_heroku_to_datadog_advanced/blob/master/app.py#L13) to your own heroku webapp)

You know what to do, if not, revisit https://github.com/jinmei612/from_heroku_to_datadog/blob/master/README.md

Run `heroku config` to check your env var 
Run `heroku config:add DD_<envvar>=<value>` to set env var

```
DD_API_KEY:                xxx
DD_APM_ENV:                heroku
DD_DYNO_HOST:              true
DD_TAGS:                   env:heroku
```

# View Heroku Logs in Datadog
To send all heroku logs to Datadog, run: 
`heroku drains:add 'https://http-intake.logs.datadoghq.com/v1/input/<DD_API_KEY>?ddsource=heroku&service=<SERVICE>&host=<HOST>' -a <APPLICATION_NAME>`


https://docs.datadoghq.com/logs/guide/collect-heroku-logs/?tab=ussite
