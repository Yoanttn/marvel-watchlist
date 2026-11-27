set -a 
[ -f .env ] && . ./.env
set +a

sqlite3 "$DBPATH" < schema.sql