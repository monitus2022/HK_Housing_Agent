import sys
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

# Add the src directory to the Python path
backend_src = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(backend_src))

# Set required environment variables for testing
os.environ["OPENROUTER_API_URL"] = "https://test.openrouter.ai"
os.environ["OPENROUTER_API_KEY"] = "test_api_key"
