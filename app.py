from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def anasayfa():
                    
    baslik = 'Anasayfa'                
    return render_template('home-personal.html',title = baslik )


app.run(debug = True)
