def on_forever():
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(196, music.beat(BeatFraction.WHOLE))
    music.play_tone(196, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)

