
# MAIN APP

```python
python3 -m uvicorn integrated.app.main:app
```


# CLIENT

```python
python3 -m integrated.scripts.camera_client
```


# CONTAINER DEPLOYMENT

## Build Docker

```bash
docker-compose build
```

## Run Docker

```bash
docker-compose up
```
## Stop Docker

```bash
docker-compose down
```

```bash
docker rmi integrated-api-services
```