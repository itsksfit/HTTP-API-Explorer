# HTTP API Explorer

A simple command-line HTTP client built with Python to understand how APIs work. This project sends HTTP requests, measures response time, parses JSON responses, and displays response headers.

## Features

- ✅ GET Requests
- ✅ POST Requests
- ✅ PUT Requests
- ✅ DELETE Requests
- ✅ Response Time
- ✅ Pretty JSON Output
- ✅ Response Headers
- ✅ Error Handling
- 🚧 Request History

## Tech Stack

- Python 3.11
- Requests
- uv

## Project Structure

```text
HTTP-API-Explorer/
│
├── api/
│   └── client.py
├── history/
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## Installation

```bash
git clone https://github.com/itsksfit/HTTP-API-Explorer.git
cd HTTP-API-Explorer

uv venv
source .venv/bin/activate

uv sync
```

## Run

```bash
uv run main.py
```

## Current Progress

- HTTP GET requests
- Response status codes
- Response time measurement
- JSON response parsing
- HTTP response headers
- Basic exception handling

## Future Improvements

- POST, PUT and DELETE requests
- Pretty JSON formatting
- Save request history
- Interactive menu
- Export responses