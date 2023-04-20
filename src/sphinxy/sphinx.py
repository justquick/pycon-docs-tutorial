from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    ...


class Sphinx:
    def __init__(self, name: str):
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """
        The function returns a string introducing a mythical character named after the value of the
        `_name` attribute.

        Returns:
          A string that introduces the speaker as a guardian of Thebes who has posed riddles to those
        who approach them. The string includes the speaker's name, which is stored in the `_name`
        attribute.
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """
        This function updates the riddle and returns a message asking if the user is ready to solve it.

        Args:
          riddle (Riddle): Riddle object that contains the updated riddle information.

        Returns:
          a string that says "I have updated my riddle. Are you ready to solve it?"
        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """
        This Python function poses a riddle and optionally includes a hint.

        Args:
          include_hint (bool): include_hint is a boolean parameter that determines whether or not to
        include a hint in the returned tuple. If it is set to True, a hint will be included in the
        tuple. If it is set to False, the hint will be None. Defaults to False

        Returns:
          A tuple containing a string (the riddle question) and either a string (the hint) or None,
        depending on the value of the include_hint parameter.
        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """
        This function checks if a riddle answer is correct and returns a message with a hint if the
        answer is wrong and the hint flag is set to True, otherwise it raises an exception.

        Args:
          answer (str): The answer provided by the user to the riddle question.
          return_hint (bool): return_hint is a boolean parameter that determines whether or not to
        return a hint if the answer is incorrect. If set to True, the function will return a hint along
        with the message "Your answer was wrong." If set to False, the function will raise an exception
        with the message "Your answer was. Defaults to False

        Returns:
          a string. If the answer is correct, it returns "Your answer was correct. You may pass." If the
        answer is wrong and the parameter return_hint is True, it returns a hint about the answer.
        Otherwise, it raises an IncorrectAnswer exception with the message "Your answer was wrong. You
        shall not pass."
        """
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")
