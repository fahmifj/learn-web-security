.PHONY: labs clean postgres adminer db

labs: postgres adminer

clean: 
	docker stop adminer pgsql

postgres:
	docker run -d --name pgsql -p 5432:5432 --rm -e POSTGRES_PASSWORD=secret postgres 

adminer:
	docker run -d --name adminer -p 4000:8080 --rm adminer
db:
	migrate -source file://00-sqli-lab/migrations \
			-database postgres://postgres:secret@$(wslip)/postgres?sslmode=disable up
db-down:
	migrate -source file://00-sqli-lab/migrations \
			-database postgres://postgres:secret@$(wslip)/postgres?sslmode=disable down