# MongoDB example with docker and python

## Run MongoDB using docker compose

1. In the `docker` folder is available a docker compose witch run two services: `mongo` and `mongo-express` ( a simple tool for exploring the resources in a mongo database)

```bash
cd docker
```

2. Run the services using docker compose

```bash
docker compose up
```

## Run the python example

In the `src` folder an example for connecting to MongoDB using python.

1. Install the requirements

```bash
pip install -r requirements.txt
```

2. move into the src directory

```bash
cd src
```

3. run the python file

```bash
python example.py
```