# dockerCommentApp01
A simple demo app with docker (python | postgresql)

# Steps
- read data from remote source (https://jsonplaceholder.typicode.com/comments)
- init db and tables (every json property is a column)
- put data into a postgres table
- group data by postId and save result on a file: storage/results.txt

# init dev
- create .env.app.dev like this one:

DB_HOST=db
DB_NAME=testdb
DB_USER=user
DB_PASSWORD=password
COMMENTS_URL="https://jsonplaceholder.typicode.com/comments"
RESULT_FILE="/storage/results.txt"

- create .env.db.dev like this one:

POSTGRES_DB=testdb
POSTGRES_USER=user
POSTGRES_PASSWORD=password

- just run: docker compose -f docker-compose.yml up --build


