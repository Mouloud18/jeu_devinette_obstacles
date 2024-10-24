from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret-key-devinette'

# Fonction pour initialiser la partie
def initialiser_partie():
    session['nombre_a_deviner'] = random.randint(1, 100)
    session['nombre_essais'] = 0
    session['max_essais'] = 10
    session['pieges'] = [3, 7]  # Tentatives où des pièges sont activés
    session['devine'] = False
    session['message'] = "Bienvenue dans le jeu de devinette ! Entrez un nombre entre 1 et 100."
    session['jeu_termine'] = False
    
@app.route('/about')
def about():
    return "À propos -2: Ceci est une application Flask avec Git."

@app.route('/about')
def about():
    return "À propos-3 : Ceci est une application Flask avec Git."

@app.route('/', methods=['GET', 'POST'])
def index():
    # Si la partie est terminée ou que la session n'existe pas encore, on initialise
    if 'nombre_a_deviner' not in session or session.get('jeu_termine', False):
        initialiser_partie()

    if request.method == 'POST':
        try:
            # Récupération du nombre entré par l'utilisateur
            joueur_choix = int(request.form['nombre'])

            # Incrémenter le nombre d'essais
            session['nombre_essais'] += 1

            # Pièges : indices erronés à certaines tentatives
            if session['nombre_essais'] in session['pieges']:
                session['message'] = "Attention, vous avez activé un piège !"
                if random.choice([True, False]):
                    session['message'] += " L'indice est : Le nombre est plus grand que ce que vous avez deviné."
                else:
                    session['message'] += " L'indice est : Le nombre est plus petit que ce que vous avez deviné."
            else:
                # Comparaison du nombre entré avec le nombre à deviner
                if joueur_choix < session['nombre_a_deviner']:
                    session['message'] = "Trop petit !"
                elif joueur_choix > session['nombre_a_deviner']:
                    session['message'] = "Trop grand !"
                else:
                    session['message'] = f"Bravo ! Vous avez deviné le nombre {session['nombre_a_deviner']} en {session['nombre_essais']} essais."
                    session['jeu_termine'] = True

            # Vérification du nombre d'essais restants
            if session['nombre_essais'] >= session['max_essais']:
                session['message'] = f"Vous avez épuisé vos {session['max_essais']} essais. Le nombre à deviner était {session['nombre_a_deviner']}."
                session['jeu_termine'] = True

        except ValueError:
            session['message'] = "Veuillez entrer un nombre valide."

    return render_template('index.html', message=session['message'], nombre_essais=session['nombre_essais'], jeu_termine=session['jeu_termine'])

@app.route('/recommencer')
def recommencer():
    initialiser_partie()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
