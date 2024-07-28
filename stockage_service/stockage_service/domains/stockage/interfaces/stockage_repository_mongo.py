from domains.stockage.models.prompt import Prompt
from typing import List


class StockageRepository:
    def __init__(self):
        """
        Initializes a new repository for managing prompts.
        """
        pass

    def create_prompt(self, prompt: Prompt) -> Prompt:
        """
        Creates a new prompt in the stockage repository.

        Args:
            prompt (Prompt): The prompt object to be created.

        Returns:
            Prompt: The created prompt object.
        """
        pass

    def read_prompt(self, prompt_id: str) -> Prompt:
        raise NotImplementedError

    def update_prompt(self, prompt: Prompt) -> Prompt:
        raise NotImplementedError

    def delete_prompt(self, prompt_id: str) -> None:
        raise NotImplementedError

    def get_prompt_by_id(self, prompt_id: str) -> Prompt:
        raise NotImplementedError

    def get_all_prompts(self) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_tag(self, tag: str) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_status(self, status: str) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_generation_origin(
        self, generation_origin: str
    ) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_user_id(self, user_id: str) -> List[Prompt]:
        raise NotImplementedError
