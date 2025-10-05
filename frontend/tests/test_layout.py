import pytest
from unittest.mock import patch, MagicMock
from ui.layout import Layout


class TestLayout:
    """Tests for the Layout class."""
    
    @patch('ui.layout.st.set_page_config')
    @patch('ui.layout.st.title')
    @patch('ui.layout.st.markdown')
    def test_layout_initialization(self, mock_markdown, mock_title, mock_set_page_config):
        """Test that Layout initializes and calls all setup methods."""
        layout = Layout()
        
        # Verify set_page_config was called with correct parameters
        mock_set_page_config.assert_called_once_with(
            page_title="Housing Chatbot",
            layout="wide"
        )
        
        # Verify title was called
        mock_title.assert_called_once_with("🏠 Hong Kong Housing Chatbot")
        
        # Verify markdown was called for description
        mock_markdown.assert_called_once()
        call_args = mock_markdown.call_args[0][0]
        assert "rent, estates, and housing trends" in call_args
    
    @patch('ui.layout.st.set_page_config')
    @patch('ui.layout.st.title')
    @patch('ui.layout.st.markdown')
    def test_set_page_config(self, mock_markdown, mock_title, mock_set_page_config):
        """Test set_page_config method."""
        Layout.set_page_config()
        
        mock_set_page_config.assert_called_once_with(
            page_title="Housing Chatbot",
            layout="wide"
        )
    
    @patch('ui.layout.st.set_page_config')
    @patch('ui.layout.st.title')
    @patch('ui.layout.st.markdown')
    def test_render_title(self, mock_markdown, mock_title, mock_set_page_config):
        """Test render_title method."""
        Layout.render_title()
        
        mock_title.assert_called_once_with("🏠 Hong Kong Housing Chatbot")
    
    @patch('ui.layout.st.set_page_config')
    @patch('ui.layout.st.title')
    @patch('ui.layout.st.markdown')
    def test_description(self, mock_markdown, mock_title, mock_set_page_config):
        """Test description method."""
        Layout.description()
        
        mock_markdown.assert_called_once()
        call_args = mock_markdown.call_args[0][0]
        assert "rent, estates, and housing trends" in call_args
        assert "Hong Kong" in call_args
        assert "Ask me anything!" in call_args
