# Poll Service

```
docker network create polls-network   # once, shared by both services
cp .env.example .env
docker-compose up --build
```
Swagger: http://localhost:8002/docs

| Method | Path | Description |
|---|---|---|
| POST | /questions | Create question |
| GET | /questions/{id} | Get question |
| PUT | /questions/{id} | Update question |
| DELETE | /questions/{id} | Delete question |
| POST | /answers | Answer a question (once per user per question) |
| PUT | /answers | Update an existing answer |
| DELETE | /answers/user/{user_id} | Delete all answers of a user (used by user service) |
| GET | /stats/questions/{id}/options | Votes per option for a question |
| GET | /stats/questions/{id}/total | Total answers for a question |
| GET | /stats/users/{id}/answers | All answers of a user |
| GET | /stats/users/{id}/total | Number of questions a user answered |
| GET | /stats/questions | All questions with votes per option |

`selected_option` is 1-4 (first to fourth option).
