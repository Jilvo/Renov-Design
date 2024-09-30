from stockage_service.domains.stockage.models.prompt import Prompt
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

    def read_prompt(self, prompt_id: int) -> Prompt:
        raise NotImplementedError

    def update_prompt(self, prompt: Prompt) -> Prompt:
        raise NotImplementedError

    def delete_prompt(self, prompt_id: int) -> None:
        """
        Deletes a prompt from the stockage repository.

        Args:
            prompt_id (int): The ID of the prompt to be deleted.

        Returns:
            None
        """
        pass

    def delete_prompts_by_user_id(self, user_id: str) -> None:
        """
        Deletes all prompts associated with a given user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            None
        """
        pass
        pass

    def get_prompt_by_id(self, prompt_id: int) -> Prompt:
        """
        Retrieves a prompt by its ID.

        Args:
            prompt_id (int): The ID of the prompt.

        Returns:
            Prompt: The prompt object.

        """
        pass

    def get_all_prompts(self) -> List[Prompt]:
        """
        Retrieves all prompts from the stockage repository.

        Returns:
            A list of Prompt objects representing all prompts in the repository.
        """
        pass

    def get_all_prompts_by_tag(self, tag: str) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_status(self, status: str) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_generation_origin(
        self, generation_origin: str
    ) -> List[Prompt]:
        raise NotImplementedError

    def get_all_prompts_by_user_id(self, user_id: str) -> List[Prompt]:
        """
        Retrieves all prompts associated with a given user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            List[Prompt]: A list of Prompt objects associated with the user ID.
        """
        pass
