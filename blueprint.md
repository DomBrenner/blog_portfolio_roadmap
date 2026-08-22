1. Flask setup — venv, install, one test route, confirm server runs
2. One hardcoded route — GET /posts returns a fixed Python list as JSON, no DB. Confirms routing + JSON response works
3. DB schema design — posts table: id, title, content, category, tags, createdAt, updatedAt. Tags as comma-separated string for simplicity
4. Connect Flask to SQLite — get a connection, create the table
5. POST /posts — validate, insert, return 201
6. GET /posts/:id — fetch one, 200 or 404
7. GET /posts (real, from DB now) — replace the hardcoded version
8. PUT /posts/:id — validate, update, 200 or 404
9. DELETE /posts/:id — 204 or 404
10. Search filter — ?term= wildcadrd on title/content/category
11. Manual test pass — every endpoint against the spec's exact status codes