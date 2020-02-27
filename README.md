
You should have one heroku webapp running after this exercise: https://github.com/jinmei612/from_heroku_to_datadog

Now, let's create another heroku webapp that calls the webapp we created earlier

You know what to do, if not, revisit https://github.com/jinmei612/from_heroku_to_datadog/blob/master/README.md

Run `heroku config` to check your env var 
Run `heroku config:add DD_<envvar>=<value>` to set env var

```
DD_API_KEY:                xxx
DD_APM_ENV:                heroku
DD_DYNO_HOST:              true
DD_TAGS:                   env:heroku
```
