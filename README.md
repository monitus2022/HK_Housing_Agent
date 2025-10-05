# HK_Housing_Agent

## Testing

This project includes comprehensive test coverage for both backend and frontend components.

### Backend Tests

The backend tests cover:
- API endpoints (`/health`, `/echo`, `/prompt`)
- LLM service logic with OpenAI integration mocking
- Error handling and edge cases

To run backend tests:
```bash
cd backend
pip install -r requirements.txt
pytest tests/ -v
```

### Frontend Tests

The frontend tests cover:
- Layout component (page configuration, title, description)
- Chatbox component (session management, user input, response generation)
- UI interaction logic

To run frontend tests:
```bash
cd frontend
pip install -r requirements.txt
pytest tests/ -v
```

### Test Coverage

- Backend: 13 test cases covering API endpoints and service logic
- Frontend: 13 test cases covering UI components and interactions

