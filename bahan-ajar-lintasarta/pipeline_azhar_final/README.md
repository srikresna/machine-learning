# a443-cc-pipeline
Ini adalah repositori untuk latihan pada kelas Machine Learning Operations (MLOps)

- Install CLI heroku ([tautan](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli))
- Login ke heroku melalui CLI dengan perintah berikut.
```
heroku login
```
- Login ke heroku container registry ([dokumentasi](https://devcenter.heroku.com/articles/container-registry-and-runtime#logging-in-to-the-registry:~:text=%24-,heroku%20container%3Alogin,-or%20directly%20via))

```
heroku container:login
```

- Push container ke heroku container registry

```
heroku container:push web -a cc-prediction
```

- Release model serving

```
heroku container:release web -a cc-prediction
```