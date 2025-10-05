import pytest
from unittest.mock import patch, MagicMock


class TestChatbox:
    """Tests for the Chatbox class."""
    
    @patch('ui.chatbox.st')
    def test_chatbox_initialization(self, mock_st):
        """Test that Chatbox initializes correctly."""
        mock_st.session_state = MagicMock()
        mock_st.session_state.__contains__ = MagicMock(return_value=False)
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        
        # Verify session state was initialized
        assert hasattr(chatbox, '_init_session')
    
    @patch('ui.chatbox.st')
    def test_init_session_creates_messages(self, mock_st):
        """Test that _init_session creates initial messages."""
        mock_st.session_state = MagicMock()
        mock_st.session_state.__contains__ = MagicMock(return_value=False)
        mock_st.session_state.messages = []
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        chatbox._init_session()
        
        # Verify initial message was set
        assert len(mock_st.session_state.messages) > 0
        assert mock_st.session_state.messages[0]["role"] == "assistant"
        assert "rent, estates, or housing trends" in mock_st.session_state.messages[0]["content"]
    
    @patch('ui.chatbox.st')
    def test_init_session_does_not_override_existing(self, mock_st):
        """Test that _init_session doesn't override existing messages."""
        existing_messages = [{"role": "user", "content": "Existing message"}]
        mock_st.session_state = MagicMock()
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.session_state.messages = existing_messages
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        
        # Verify existing messages were not changed
        assert mock_st.session_state.messages == existing_messages
    
    @patch('ui.chatbox.st')
    def test_render_chat_history(self, mock_st):
        """Test render_chat_history displays all messages."""
        messages = [
            {"role": "assistant", "content": "Hello"},
            {"role": "user", "content": "Hi there"},
            {"role": "assistant", "content": "How can I help?"}
        ]
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = messages
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        
        mock_chat_message = MagicMock()
        mock_chat_message.return_value.markdown = MagicMock()
        mock_st.chat_message = mock_chat_message
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        chatbox.render_chat_history()
        
        # Verify chat_message was called for each message
        assert mock_st.chat_message.call_count == 3
    
    @patch('ui.chatbox.st')
    def test_get_user_input_with_input(self, mock_st):
        """Test get_user_input returns user input when provided."""
        test_input = "What is the rent in Central?"
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = []
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.chat_input = MagicMock(return_value=test_input)
        mock_st.chat_message = MagicMock(return_value=MagicMock())
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        result = chatbox.get_user_input()
        
        assert result == test_input
        # Verify message was added to session state
        assert len(mock_st.session_state.messages) == 1
        assert mock_st.session_state.messages[0]["role"] == "user"
        assert mock_st.session_state.messages[0]["content"] == test_input
    
    @patch('ui.chatbox.st')
    def test_get_user_input_without_input(self, mock_st):
        """Test get_user_input returns None when no input."""
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = []
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.chat_input = MagicMock(return_value=None)
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        result = chatbox.get_user_input()
        
        assert result is None
        # Verify no message was added
        assert len(mock_st.session_state.messages) == 0
    
    @patch('ui.chatbox.st')
    def test_generate_response(self, mock_st):
        """Test generate_response creates and stores response."""
        user_input = "Test question"
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = []
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.chat_message = MagicMock(return_value=MagicMock())
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        chatbox.generate_response(user_input)
        
        # Verify response was added to session state
        assert len(mock_st.session_state.messages) == 1
        assert mock_st.session_state.messages[0]["role"] == "assistant"
        assert f"You were saying: {user_input}" == mock_st.session_state.messages[0]["content"]
    
    @patch('ui.chatbox.st')
    def test_run_with_user_input(self, mock_st):
        """Test run method processes user input."""
        test_input = "Test message"
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = []
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.chat_input = MagicMock(return_value=test_input)
        mock_st.chat_message = MagicMock(return_value=MagicMock())
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        chatbox.run()
        
        # Verify messages were added (user + assistant response)
        assert len(mock_st.session_state.messages) == 2
    
    @patch('ui.chatbox.st')
    def test_run_without_user_input(self, mock_st):
        """Test run method without user input."""
        mock_st.session_state = MagicMock()
        mock_st.session_state.messages = []
        mock_st.session_state.__contains__ = MagicMock(return_value=True)
        mock_st.chat_input = MagicMock(return_value=None)
        mock_st.chat_message = MagicMock(return_value=MagicMock())
        
        from ui.chatbox import Chatbox
        
        chatbox = Chatbox()
        chatbox.run()
        
        # Verify no messages were added
        assert len(mock_st.session_state.messages) == 0
