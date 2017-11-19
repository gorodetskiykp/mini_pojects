import pygame.midi
import time


def go(note, duration, player):
    player.note_on(note, 127)
    time.sleep(duration)
    player.note_off(note, 127)


def chord(notes, player, base=50):
    duration = 1/8
    for note in notes:
        if note < 0:
            time.sleep(duration)
        else:
            go(note+base, duration, player)


def make_chord_list(symbols):
    chord_list = []
    for sign in ' '.join(symbols.split()):
        if ord(sign) > 1071:
            chord_list.append(ord(sign) - 1072)
        elif sign == '.' or sign == ' ':
            chord_list.append(-1)
    return chord_list


def play(symbols):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)
    chord(make_chord_list(symbols), player)
    del player
    pygame.midi.quit()


if __name__ == "__main__":
    words = """
        Я вас любил: любовь еще, быть может 
        В душе моей угасла не совсем; 
        Но пусть она вас больше не тревожит; 
        Я не хочу печалить вас ничем.
        Я вас любил безмолвно, безнадежно, 
        То робостью, то ревностью томим; 
        Я вас любил так искренно, так нежно, 
        Как дай вам бог любимой быть другим.
        """

    play(words)
