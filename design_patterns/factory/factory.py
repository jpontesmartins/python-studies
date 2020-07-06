
## classes to bem chosen by client

class FrenchTranslator:
    def __init__(self):
        self.translations = {
            "dog": "chien", 
            "cat": "chat",
            "parrot":"perroquet",
            "bear":"ourse"
        }

    def translate(self, word: str) -> str:
        return self.translations.get(word)

class PortugueseTranslator:
    def __init__(self):
        self.translations = {
            "dog": "cachorro", 
            "cat": "gato",
            "parrot": "papagaio",
            "bear": "urso"
        }

    def translate(self, word: str) -> str:
        return self.translations.get(word)

class EnglishTranslator:
    def translate(self, word: str) -> str:
        return word


## factory...

def get_translation_in(language: str = "English") -> object:
    translators = {
        "English": EnglishTranslator,
        "French": FrenchTranslator,
        "Portuguese": PortugueseTranslator
    }

    return translators[language]()


## main
def main():
    e = get_translation_in(language="English")
    g = get_translation_in(language="French")
    pt = get_translation_in(language="Portuguese")

    for word in "dog parrot cat bear".split():
        print(
            e.translate(word), 
            g.translate(word), 
            pt.translate(word))


if __name__ == "__main__":
    main()