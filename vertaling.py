from google_trans_new import google_translator

translator = google_translator()

f = open('C:\\Users\\emile\\Desktop\\python programs\\nl_experiment\\basiswoorden-gekeurd.txt','r')

for i in range(829):
    contents = ""
    for j in range(240):
        word = str(f.readline())
        contents = contents + word
    r = translator.translate(contents, lang_src='nl', lang_tgt='af')
    print(i)
    lizt = r.split('\n')
    with open("C:\\Users\\emile\\Desktop\\python programs\\nl_experiment\\basiswoorden-gekeurd-af.txt", "a") as file_object:
        for l in lizt:
            try:
                file_object.write(l + '\n')
            except:
                file_object.write('ERROR\n')