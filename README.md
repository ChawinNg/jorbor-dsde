## File structures

### `kafka`

Contains `docker-compose` for creating Kafka.

### `workers`

Python package dependencies

- python-dotenv
- python-kafka
- pymongo

  Contains `producer` and `consumer` codes.
  Make sure to properly set `.env` file by copying `.env.example`.
  Also, contains `Dockerfile` and `docker-compose` for starting worker nodes.

## Start up sequence

1. Go inside `kafka` and do

```bash
docker compose up -d
```

This will start kafka service

> **Note:** raw_data partitions might not be setup properly. Make sure it has the same number of partitions as the number of worker nodes.

2. Go inside `workers` and do

```bash
docker compose up -d
```

This will start worker nodes.
Their logs can be seen with the following commands

```bash
docker compose logs -f
```
