import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    # Mock the settings to avoid requiring environment variables
    with patch('config.settings.settings') as mock_settings:
        mock_settings.app_name = "Test App"
        mock_settings.app_description = "Test Description"
        mock_settings.app_version = "1.0.0"
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        from main import app
        return TestClient(app)


class TestHealthEndpoint:
    """Tests for the /health endpoint."""
    
    def test_health_check_returns_ok(self, client):
        """Test that health check returns status ok."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestEchoEndpoint:
    """Tests for the /echo endpoint."""
    
    def test_echo_returns_message(self, client):
        """Test that echo endpoint returns the provided message."""
        test_message = "Hello, World!"
        response = client.get(f"/echo?message={test_message}")
        assert response.status_code == 200
        assert response.json() == {"message": test_message}
    
    def test_echo_with_special_characters(self, client):
        """Test echo endpoint with special characters."""
        from urllib.parse import quote
        test_message = "Test@123!#"
        encoded_message = quote(test_message)
        response = client.get(f"/echo?message={encoded_message}")
        assert response.status_code == 200
        assert response.json() == {"message": test_message}
    
    def test_echo_without_message_parameter(self, client):
        """Test echo endpoint without message parameter."""
        response = client.get("/echo")
        assert response.status_code == 422  # Unprocessable Entity


class TestPromptEndpoint:
    """Tests for the /prompt endpoint."""
    
    @patch('services.llm.LLMService.generate_text')
    def test_prompt_returns_response(self, mock_generate_text, client):
        """Test that prompt endpoint returns LLM response."""
        mock_generate_text.return_value = "This is a test response"
        test_prompt = "What is the weather?"
        
        response = client.get(f"/prompt?prompt={test_prompt}")
        assert response.status_code == 200
        assert response.json() == {"response": "This is a test response"}
        mock_generate_text.assert_called_once_with(test_prompt)
    
    @patch('services.llm.LLMService.generate_text')
    def test_prompt_handles_none_response(self, mock_generate_text, client):
        """Test that prompt endpoint handles None response from LLM."""
        mock_generate_text.return_value = None
        test_prompt = "Test prompt"
        
        response = client.get(f"/prompt?prompt={test_prompt}")
        assert response.status_code == 200
        assert response.json() == {"response": None}
    
    def test_prompt_without_prompt_parameter(self, client):
        """Test prompt endpoint without prompt parameter."""
        response = client.get("/prompt")
        assert response.status_code == 422  # Unprocessable Entity
