# Basic Python crawler

This is a basic Python crawler using multiple libraries such as `requests` and `bs4`(Beautiful Soup).
It is not intended for production use and is just a simple example.

# Running with Docker

Only required prerequisite - a working insstallation of Docker.

To start the project run:

```bash
docker-compose up
```

Once up you should just see logs from the different containers that just started.
In another termminal execute into the running container:

```bash
docker exec -it  basic-crawler-python_app-1 bash
```

Once in the container you can run the crawler:

```bash
pipenv run python main.py
```

Check your logs location for the outcome of each run. Have fun debugging.

There are also some example env variables `.env.example`.
So if you use them there is another url to scrape and Selenium is disabled.

Try yourself by running:
```bash
cp .env.example .env && source .env
```
```bash
pipenv run python main.py
```

# Build and publish a Docker image using GitHub Actions

We are building and pushing our image to DockerHub.

See detailed how to: https://docs.github.com/en/actions/publishing-packages/publishing-docker-images