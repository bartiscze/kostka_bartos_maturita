import random
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session 

app = Flask(__name__)
app.secret_key = "adafwfge gegegegee"
app.debug = False

@app.route('/')
def hod_kostkou():
    hod = random.randint(1,6)
    hod1 = random.randint(1,6)
  
    if not 'pc' in session:
        session['pc'] = 0
    if not 'hrac' in session:
        session['hrac'] = 0

    if hod > hod1:
        vysledek = "VYHRAL JSI"
        session['hrac'] = session['hrac'] + 1
    elif hod1 > hod:
        vysledek = "PROHRAL JSI"
        session['pc'] = session['pc'] + 1 
        
    elif hod1 == hod:
        vysledek = "REMIZA"
    
    return render_template ('index.html', text=hod, text1=hod1, text2=vysledek, text3=session['hrac'], text4 = session['pc'])




if __name__ == '__main__':
    app.run()