import pytest
from unittest.mock import patch, MagicMock
from services.llm import LLMService


class TestLLMService:
    """Tests for the LLMService class."""
    
    @patch('services.llm.settings')
    def test_init_with_valid_api_key(self, mock_settings):
        """Test LLMService initialization with valid API key."""
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        with patch('services.llm.OpenAI') as mock_openai:
            service = LLMService()
            assert service.api_key == "test_api_key"
            mock_openai.assert_called_once_with(
                base_url="https://test.com",
                api_key="test_api_key"
            )
    
    @patch('services.llm.settings')
    def test_init_without_api_key_raises_error(self, mock_settings):
        """Test LLMService initialization without API key raises ValueError."""
        mock_settings.openrouter_api_key = None
        
        with pytest.raises(ValueError, match="OpenRouter API key is required"):
            LLMService()
    
    @patch('services.llm.settings')
    @patch('services.llm.OpenAI')
    def test_generate_text_success(self, mock_openai_class, mock_settings):
        """Test generate_text returns content successfully."""
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        # Mock the OpenAI client and response
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_message = MagicMock()
        mock_message.content = "Generated response text"
        mock_choice = MagicMock()
        mock_choice.message = mock_message
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        
        mock_client.chat.completions.create.return_value = mock_response
        
        service = LLMService()
        result = service.generate_text("Test prompt")
        
        assert result == "Generated response text"
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('services.llm.settings')
    @patch('services.llm.OpenAI')
    def test_generate_text_no_choices(self, mock_openai_class, mock_settings):
        """Test generate_text returns None when no choices in response."""
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        # Mock the OpenAI client with empty response
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_response = MagicMock()
        mock_response.choices = []
        
        mock_client.chat.completions.create.return_value = mock_response
        
        service = LLMService()
        result = service.generate_text("Test prompt")
        
        assert result is None
    
    @patch('services.llm.settings')
    @patch('services.llm.OpenAI')
    def test_generate_text_no_message(self, mock_openai_class, mock_settings):
        """Test generate_text returns None when no message in response."""
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        # Mock the OpenAI client with choice but no message
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_choice = MagicMock()
        mock_choice.message = None
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        
        mock_client.chat.completions.create.return_value = mock_response
        
        service = LLMService()
        result = service.generate_text("Test prompt")
        
        assert result is None
    
    @patch('services.llm.settings')
    @patch('services.llm.OpenAI')
    def test_generate_text_with_correct_prompt_format(self, mock_openai_class, mock_settings):
        """Test that generate_text formats the prompt correctly."""
        mock_settings.openrouter_api_key = "test_api_key"
        mock_settings.openrouter_api_url = "https://test.com"
        mock_settings.openrouter_model = "test-model"
        
        # Mock the OpenAI client
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        mock_message = MagicMock()
        mock_message.content = "Response"
        mock_choice = MagicMock()
        mock_choice.message = mock_message
        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        
        mock_client.chat.completions.create.return_value = mock_response
        
        service = LLMService()
        test_prompt = "What is Hong Kong housing?"
        service.generate_text(test_prompt)
        
        # Verify the call was made with correct parameters
        call_args = mock_client.chat.completions.create.call_args
        assert call_args[1]['model'] == "test-model"
        assert call_args[1]['messages'] == [
            {"role": "user", "content": test_prompt}
        ]
