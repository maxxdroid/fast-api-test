# FastAPI Image Analysis API

A simple backend service that allows a mobile app to:

1. Upload an image
2. Perform mock AI-style analysis
3. Return structured JSON results

Built with **FastAPI** and **Python**, containerized with **Docker**.

---

## How to Run the Service

### 1. Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
uvicorn main:app --reload
```

3. Access the API documentation:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc UI: http://127.0.0.1:8000/redoc

### 2. Run with Docker

1. Build the Docker image:

```bash
docker build -t fastapi-image-ai .
```

2. Run the container with persistent image storage:

```bash
docker run -d -p 8000:8000 -v $(pwd)/images:/app/images fastapi-image-ai
```

---

## API Security

All endpoints require an API key in the request header:

```
X-API-KEY: maxSecretApiKey
```

Requests without a valid API key will return `403 Forbidden`.

---

## Available Endpoints

| Method | Endpoint             | Description                                                                                          |
| ------ | -------------------- | ---------------------------------------------------------------------------------------------------- |
| POST   | `/upload`            | Upload a JPEG or PNG image (max 5MB). Returns `image_id`.                                            |
| POST   | `/analyze`           | Analyze an uploaded image using `image_id`. Returns mock skin type, detected issues, and confidence. |
| GET    | `/images/{image_id}` | Serve the uploaded image so it can be viewed in a browser.                                           |

### Example Upload Response:

```json
{
  "image_id": "e3f2c5a0-9b84-4d3b-8f88-1f7fcdabc123"
}
```

### Example Analysis Response:

```json
{
  "image_id": "e3f2c5a0-9b84-4d3b-8f88-1f7fcdabc123",
  "skin_type": "Oily",
  "issues": ["Hyperpigmentation"],
  "confidence": 0.87
}
```

---

## Assumptions

- AI analysis is mocked using random values.
- Images are stored locally in the `images/` folder.
- API key is hardcoded (`mysecretapikey123`) for simplicity.
- Maximum file size: 5MB; allowed types: JPEG/PNG.

---

## Production Improvements

- **Persistent storage:** Move images to cloud storage (S3, GCS).
- **Real AI/ML model:** Replace mock analysis with an actual AI model.
- **API key management:** Use environment variables or a secure key vault; support multiple keys per user.
- **Authentication & rate limiting:** Add JWT/OAuth2 auth and request throttling.
- **Logging & monitoring:** Integrate proper logging, metrics, and error reporting.
- **Validation & error handling:** Add stricter input validation and edge-case handling.
- **Deployment:** Use Docker Compose or Kubernetes for scalable deployments.

---

## Contact / Notes

This is a demo / prototype backend. Works end-to-end with mobile apps, Postman, or cURL.
