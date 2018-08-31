# BriteCore Test

A small SPA project developed for britecore, consists of an API developed in `python` with a `front end` based on javascript.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

To initialize the development and testing server you need:

[Install Docker and Docker-compose](https://docs.docker.com/compose/install/#install-compose)

For the development of the front end you need:

[Install Nodejs](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04) 

### Initializing Local Settings


Then just run:

```
- docker-compose up
- sh setup_docker.sh
```

then just go to `http://localhost:8000`

Endpoints requested:
 1. `http://localhost:8000/risk/`
 2. `http://localhost:8000/risk/<id>/`

For the development of the front end, please navigate to the 
folder `/static/assets/js/` in the root of the project and then:
```
- npm install
- npm run watch
```

to deploy `js`:
```
docker-compose exec app python manage.py collectstatic
```

## Deployment

Zappa to deployment:

```
pip install virtualenv
virtualenv -p python3 britecore_env
source ~/britecore_env/bin/activate
pip install -r requirements.txt
```

Before proceeding with the code deployment it is necessary to 
configure the aws keys by creating the `~/.aws/credentials` file:

```
[default] 
aws_access_key_id = key
aws_secret_access_key = secret_key
```

To deploy the code just:
```
- zappa deploy dev
```

Hosted app:
 1) https://rffuzq4a5k.execute-api.us-west-2.amazonaws.com/dev/

Hosted endpoints:
 1) https://rffuzq4a5k.execute-api.us-west-2.amazonaws.com/dev/risk/
 2) https://rffuzq4a5k.execute-api.us-west-2.amazonaws.com/dev/risk/{id}
## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The back end framework used
* [Webpack](https://webpack.js.org/) - Module Js Bundler
* [VueJs](https://vuejs.org/) - Front Js Framework


## Authors

* **Geolffrey Mena** - 
[Linkedin](https://www.linkedin.com/in/geolffrey-mena-43188365)

## License

This project is licensed under the MIT License.

