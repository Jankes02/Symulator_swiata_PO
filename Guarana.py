from Roslina import *


class Guarana(Roslina):
    def __init__(self, pole, swiat):
        super().__init__(pole, swiat)

    def umiera(self, zabojca):
        zabojca.set_sila(zabojca.get_sila() + 3)
        self.usmierc(zabojca)
