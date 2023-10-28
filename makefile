build:
	docker build --tag=faker_etl .

run:
	docker compose up -d
	sleep 8
	docker compose down