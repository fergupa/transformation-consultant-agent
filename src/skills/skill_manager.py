"""
Skill manager for loading and caching skill prompts and domain knowledge.

This module provides utilities for working with SKILL.md files and their
associated domain knowledge files.
"""

from pathlib import Path
from typing import List, Dict


class SkillManager:
    """Manages loading and caching of skill prompts and domain knowledge."""

    def __init__(self, skills_root: Path = None):
        """
        Initialize skill manager.

        Args:
            skills_root: Root directory containing skills/ folder.
                        Defaults to project root/skills
        """
        if skills_root is None:
            # Default to project root/skills
            skills_root = Path(__file__).parent.parent.parent / "skills"
        self.skills_root = Path(skills_root)
        self._cache: Dict[str, str] = {}

    def load_skill_prompt(self, skill_name: str) -> str:
        """
        Load SKILL.md content for a given skill.

        Args:
            skill_name: Name of skill directory (e.g., 'transcript-analysis')

        Returns:
            Content of SKILL.md file

        Raises:
            FileNotFoundError: If SKILL.md not found
        """
        cache_key = f"{skill_name}_prompt"
        if cache_key not in self._cache:
            skill_path = self.skills_root / skill_name / "SKILL.md"
            if not skill_path.exists():
                raise FileNotFoundError(f"SKILL.md not found at {skill_path}")
            self._cache[cache_key] = skill_path.read_text(encoding='utf-8')
        return self._cache[cache_key]

    def load_domain_knowledge(self, skill_name: str, filename: str) -> str:
        """
        Load domain knowledge file for a skill.

        Args:
            skill_name: Name of skill directory
            filename: Name of file in domain-knowledge/ folder

        Returns:
            Content of domain knowledge file

        Raises:
            FileNotFoundError: If domain knowledge file not found
        """
        cache_key = f"{skill_name}_dk_{filename}"
        if cache_key not in self._cache:
            dk_path = self.skills_root / skill_name / "domain-knowledge" / filename
            if not dk_path.exists():
                raise FileNotFoundError(f"Domain knowledge file not found at {dk_path}")
            self._cache[cache_key] = dk_path.read_text(encoding='utf-8')
        return self._cache[cache_key]

    def list_domain_knowledge_files(self, skill_name: str) -> List[str]:
        """
        List all domain knowledge files for a skill.

        Args:
            skill_name: Name of skill directory

        Returns:
            List of filenames in domain-knowledge/ directory
        """
        dk_dir = self.skills_root / skill_name / "domain-knowledge"
        if not dk_dir.exists():
            return []
        return [f.name for f in dk_dir.glob("*.md") if f.is_file()]

    def clear_cache(self):
        """Clear the prompt cache."""
        self._cache.clear()
