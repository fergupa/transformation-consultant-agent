"""
Base component interface for transformation consultant agent.

This module defines the abstract base class that all components must implement,
as well as the standard result format returned by component execution.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class ComponentResult:
    """Standard result format from component execution."""

    success: bool
    data: Any
    metadata: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        """Set timestamp if not provided."""
        if self.timestamp is None:
            self.timestamp = datetime.now()


class BaseComponent(ABC):
    """
    Base interface for all transformation consultant components.

    All components must implement this interface to ensure consistency
    in how they validate input, process data, and return results.
    """

    def __init__(self,
                 api_key: str,
                 model: str = "claude-sonnet-4-5-20250929",
                 config: Optional[Dict[str, Any]] = None):
        """
        Initialize component.

        Args:
            api_key: Anthropic API key
            model: Claude model to use
            config: Component-specific configuration
        """
        self.api_key = api_key
        self.model = model
        self.config = config or {}
        self._client = None  # Lazy initialization

    @property
    @abstractmethod
    def component_name(self) -> str:
        """Return human-readable component name."""
        pass

    @property
    @abstractmethod
    def skill_path(self) -> Path:
        """Return path to SKILL.md file for this component."""
        pass

    @abstractmethod
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input data before processing.

        Args:
            input_data: Input to validate

        Returns:
            True if valid

        Raises:
            ValueError: If input is invalid
        """
        pass

    @abstractmethod
    def process(self, input_data: Any, **kwargs) -> ComponentResult:
        """
        Execute the component's main processing logic.

        Args:
            input_data: Input data (type varies by component)
            **kwargs: Additional component-specific parameters

        Returns:
            ComponentResult with success status, data, and metadata
        """
        pass

    def _get_client(self):
        """Lazy initialization of Anthropic client."""
        if self._client is None:
            from anthropic import Anthropic
            self._client = Anthropic(api_key=self.api_key)
        return self._client

    def _load_skill_prompt(self) -> str:
        """Load SKILL.md content."""
        return self.skill_path.read_text(encoding='utf-8')

    def _call_claude(self,
                     user_message: str,
                     system_messages: list,
                     max_tokens: int = 16000,
                     temperature: float = 0) -> tuple[str, dict]:
        """
        Call Claude API with standard error handling.

        Args:
            user_message: User message content
            system_messages: List of system message dicts
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature

        Returns:
            Tuple of (response_text, usage_metadata)

        Raises:
            RuntimeError: If API call fails
        """
        try:
            client = self._get_client()
            response = client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_messages,
                messages=[{"role": "user", "content": user_message}]
            )

            metadata = {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "model": self.model
            }

            return response.content[0].text, metadata

        except Exception as e:
            raise RuntimeError(f"Claude API call failed: {str(e)}")
