class Songs:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

ChristmasSong = Songs(["I wish you a merry Christmas",
"I wish you a merry Christmas",
"I wish you a merry Christmas",
"And a happy New Year",
"Glad tidings I bring",
"To you and your kin",
"Glad tidings for Christmas",
"And a happy New Year"])

ChristmasSong.sing_me_a_song()
