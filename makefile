build:
	docker build --tag=faker_etl .

run:
	docker compose up -d
	sleep 10
	docker compose down