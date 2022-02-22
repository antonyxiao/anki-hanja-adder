from anki.collection import Collection
from hanjatagger import Hanjaro
col = Collection("/home/antonyxiao/Downloads/Anki/Korean_Grammar_Sentences_by_Evita/collection.anki2")

deck = col.find_notes("deck:Korean_Grammar_Sentences_by_Evita")
for note_id in deck:
    note = col.getNote(note_id)
    korean = note['Korean']
    translation = note['Translation']
    translation = translation.replace('<br>', '<br><br>')
    note['Translation'] = translation
    # try:
        # with Hanjaro() as hjr:
            # hanja = hjr.query(korean)
    # except AssertionError as e:
        # print(e)
    # if (hanja != korean):
        # result = (hanja + '\n' + note['Translation'])
        # note['Translation'] = result
    col.update_note(note)
        # print(result)

col.close()
