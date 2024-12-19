from flask import Flask, request, render_template

app = Flask(__name__)


sozluk = {
    "baklava": "Şerbetli hamur tatlısı.",
    "kadayıf": "Tel kadayıf ve şerbet.",
    "künefe": "Peynirli kadayıf tatlısı.",
    "revani": "İrmikli şerbetli tatlı.",
    "sütlaç": "Sütlü pirinç tatlısı.",
    "tulumba": "Şerbetli kızarmış hamur.",
    "kek": "Fırında yapılan tatlı.",
    "profiterol": "Kremalı hamur tatlısı.",
    "puding": "Sütlü soğuk tatlı.",
    "lokma": "Şerbetli hamur topları.",
    "macaron": "Badem unu ve krema tatlısı.",
    "cheesecake": "Peynirli tatlı.",
    "tiramisu": "Kahveli İtalyan tatlısı.",
    "aşure": "Buğdaylı ve bakliyatlı tatlı.",
    "helva": "Tereyağlı irmik tatlısı.",
    "çörek": "Tarçınlı tatlı çörek.",
    "dondurma": "Soğuk tatlı.",
    "meyveli tart": "Meyve ve kremalı tatlı.",
    "kabak tatlısı": "Şekerli kabak tatlısı.",
    "ballı cevizli kurabiye": "Cevizli tatlı kurabiye.",
    "lokum": "Yumuşak şekerli tatlı."
}


@app.route('/')
def index():
    return render_template('sozluk.html')

@app.route('/arama', methods=['GET'])
def arama():
    kelime = request.args.get('kelime', '').lower() 
    if kelime:
        sonuc = sozluk.get(kelime)
        if sonuc:
            return render_template('sozluk.html', result=sonuc)  
        else:
            return render_template('sozluk.html', error="Kelime bulunamadı!")  
    else:
        return render_template('sozluk.html', error="Aranacak kelimeyi belirtin.")  



if __name__ == '__main__':
    app.run(debug=True)