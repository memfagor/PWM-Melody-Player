
from time import sleep_ms

class SoundsPlayer:
    def __init__(self, emmiter, tempo = 1000, vol = 5):
        self.emmiter = emmiter
        self.limit = 90
        if vol > self.limit:
            self.volume = self.limit
        else:
            self.volume = vol
        self.sounds = {
            '_' : 0,
            'c' : 262,
            'd' : 294,
            'e' : 330,
            'f' : 349,
            'g' : 392,
            'a' : 440,
            'h' : 494
        }
        
    def playSound(self, note):
        tm = self.notes.get(note[:-1], 0)
        fq = self.sounds.get(note[-1], 0)
        if fq > 0:
            self.emmiter.freq(fq)
            self.emmiter.duty(self.volume)
        sleep_ms(tm)
        self.emmiter.duty(0)
    
    def playMelody(self, melody, tempo = 1000):
        self.notes = { str(i) : tempo // i for i in (1, 2, 4, 8, 16, 32, 64) }
        for note in melody.split(','):
            self.playSound(note)
    
    def changeVolume(self, volume):
        if volume > self.limit:
            self.volume = self.limit
        else:
            self.volume = volume
            