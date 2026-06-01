Docker usage

Build and run both the Flask app and MySQL with Docker Compose:

```bash
# Build images and start services
docker compose up --build

# Run in background
docker compose up -d --build

# Stop and remove
docker compose down
```

Environment variables

- `API_KEY` (required by the app)
- `MYSQL_DB` (default: `stocks`)
- `MYSQL_USER` (default: `root`)
- `MYSQL_PASSWORD` (required to connect to local MySQL)

Notes

- The app container connects to your local MySQL instance using `host.docker.internal`.
- This assumes MySQL is already running on the host machine and accessible on port `3306`.
- Do not use the DB service in Docker Compose; the container relies on your local MySQL installation.
