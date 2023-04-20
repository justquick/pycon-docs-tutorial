from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """
        The function checks if a given answer matches a stored answer, ignoring case sensitivity.

        Args:
          answer (str): The answer parameter is a string that represents the user's answer to a
        question.

        Returns:
          The function `check_answer` takes in a string `answer` and returns a boolean value indicating
        whether the lowercase version of `answer` is equal to the lowercase version of the answer stored
        in the object's `answer` attribute.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """
        This function returns an iterator that yields each character in a given answer.
        """
        yield from iter(self.answer)
