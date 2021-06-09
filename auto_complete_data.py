from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    line: int
    offset: int
    score: int

    def __str__(self):
        return self.completed_sentence + " (" + self.source_text + " " + str(self.line) + " " + str(self.offset) + ')' \
               + " score: " + str(self.score)

    def __repr__(self):
        return "\ncompleted_sentence: " + self.completed_sentence + "source_text: " + \
        self.source_text + "\noffset: " + str(self.offset) + "\nscore: " + str(self.score)