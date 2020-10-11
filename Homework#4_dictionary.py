
vene=["оно","собака","кот","окно","часы","телефон","цветок","волейбол","университет","лёд","пчела","биология","школа","зоопарк","выбор","обезьяна","слон","гепард","мышь","олень","лошадь","волк","заяц","индюк","курица","медваедь","бобр","петух","кролик","овца","корова","лев","барсук","лось","поросёнок","лиса","крыса","свинья","ёж","ягнёнок","тигр","жеребёнок","теленок"]
inglise=["it","dog","cat","window","watch","phone","flower","volleyball","university","ice","bee","biology","school","zoo","choice","monkey","elephant","cheetah","mouse","deer","horse","wolf","hare","turkey","hen","bear","beaver","cock","rabbit","sheep","cow","lion","badger","elk","piglet","fox","rat","pig","hedgehong","lamb","tiger","foal","calf"]


def dicionary(vene,inglise):
    print("Welcome to Rus-Eng and Eng-Rus dictionary!")
    while True:
        language=input("Please select from what language you want to translate (eng/rus): ")
        if language=='rus':
            sona=input("Введи слово на русском для перевода: ")
            if sona in vene:
                nr=vene.index(sona)
                translation=inglise[nr]
                print("Your translation of '"+sona+"'","is '"+translation+"'")
            if sona not in vene:
                print("There is no such word in my vocabulary")
        elif language=='eng':
            sona=input("Enter the word for translation: ")
            if sona in inglise:
                nr=inglise.index(sona)
                translation=vene[nr]
                print("Your translation of '"+sona+"'","is '"+translation+"'")
            if sona not in inglise:
                print("There is no such word in my vocabulary")
        else:
            break
dicionary(vene,inglise)

