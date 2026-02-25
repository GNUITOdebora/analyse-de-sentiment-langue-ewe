# 🧠 Analyse de Sentiments du Langage Naturel — Langue EWE

> Projet de traitement automatique du langage naturel (NLP) appliqué à la **langue Ewe**, une langue africaine parlée au Togo, au Bénin et au Ghana.  
> **Élaboré par** : Gnuito Débora

---

## 📋 Table des matières

1. [Contexte et introduction](#contexte-et-introduction)
2. [La langue Ewe](#la-langue-ewe)
3. [Structure du projet](#structure-du-projet)
4. [Méthodologie](#méthodologie)
5. [Résultats](#résultats)
6. [Déploiement](#déploiement)
7. [Applications potentielles](#applications-potentielles)
8. [Perspectives futures](#perspectives-futures)

---

## 🌍 Contexte et introduction

Les défis de compréhension linguistique représentent l'un des domaines les plus complexes de l'intelligence artificielle. Le **Traitement du Langage Naturel (NLP)** est la branche de l'IA qui se concentre sur la capacité des machines à comprendre, interpréter et générer le langage humain.

Ce projet applique le NLP à l'**analyse de sentiment** — une tâche qui consiste à extraire et classifier les opinions (positif, négatif, neutre) dans un texte — dans le cas particulier de la langue **Ewe**, une langue peu dotée en ressources numériques.

---

## 🗣️ La langue Ewe

L'éwé est une langue nigéro-congolaise parlée au **Togo**, au **Bénin** et dans le sud-est du **Ghana** par environ **4,5 millions** de locuteurs natifs et un million d'autres comme deuxième langue.

### Défis spécifiques au NLP en Ewe

| Défi | Description |
|------|-------------|
| **Tonalité** | Langue tonale — la hauteur de la voix change le sens des mots |
| **Manque de ressources** | Peu de corpus annotés disponibles ; culture majoritairement orale |
| **Variation dialectale** | Plusieurs dialectes : Guin, Mina, Adja-Ewe, Watsi... |
| **Caractères spéciaux** | Alphabet de 35 lettres avec des caractères propres : ɣ, ɔ, ƒ, ɖ, ẽ, ɔ̃, ã... |

> ⚠️ Contrairement aux langues classiques, les **accents** et **caractères spéciaux** ne peuvent pas être supprimés lors du prétraitement car ils changent le sens des mots. De même, les **mots d'une seule lettre** doivent être conservés (ex. : `o` exprime la négation en Ewe).

---

## 📁 Structure du projet

```
.
├── Projet_analyse_de_sentiments.ipynb   # Notebook principal (exploration, prétraitement, ML)
├── Deploiement.py                       # Application Streamlit de démonstration
├── vectorizer.pickle                    # Vectoriseur TF-IDF sauvegardé
└── best_modelNLP.pickle                 # Meilleur modèle entraîné sauvegardé
```

---

## 🔬 Méthodologie

Le projet suit un pipeline en 6 étapes :

```
1. Collecte & annotation  →  2. Exploration  →  3. Prétraitement
        →  4. Machine Learning  →  5. Évaluation  →  6. Déploiement
```

### 1. Collecte et annotation des données

Le dataset combine deux sources :
- **Formulaires en ligne** : avis sur la gastronomie togolaise, le système éducatif, les habitudes culturelles.
- **Bases existantes** : données issues de différentes sources puis annotées manuellement.

**Caractéristiques du dataset :**
- 3 446 exemples, aucune valeur manquante
- 3 classes : `Positive`, `Negative`, `Neutre`
- 6 colonnes : `id`, `Traduction`, `Sentiment`, `Ewe`, `Auteur`, `Document`
- Répartition : Négatif 35.4% | Positif 35.1% | Neutre 29.5%

### 2. Prétraitement

**Nettoyage :**
- Suppression des nombres
- Suppression des espaces multiples
- Conversion en minuscules
- Élimination de la ponctuation
- Suppression des caractères n'existant pas dans l'alphabet Ewe (C, Q, J...)

**Word Embedding :** Vectorisation via **TF-IDF**

### 3. Machine Learning

Plusieurs modèles ont été entraînés et comparés :
`Naive Bayes`, `MLP Classifier`, `SGD SVM`, `Polynomial SVM`, `RBF SVM`, `Linear SVM`

---

## 📊 Résultats

### Comparaison des modèles

| Modèle | F1 Négative | F1 Neutre | F1 Positive |
|--------|------------|-----------|-------------|
| Naive Bayes | 0.54 | 0.46 | 0.47 |
| MLP Classifier | 0.63 | 0.51 | 0.66 |
| SGD SVM | 0.64 | 0.47 | 0.68 |
| Polynomial SVM | 0.66 | 0.46 | **0.70** |
| RBF SVM | 0.66 | 0.46 | 0.69 |
| **Linear SVM** | **0.64** | **0.48** | 0.68 |

> 🏆 Le **Polynomial SVM** obtient les meilleures performances globales, notamment sur la classe Positive (F1 = 0.70). Le modèle final est sauvegardé dans `best_modelNLP.pickle`.

---

## 🚀 Déploiement

L'application est déployée via **Streamlit**. Elle permet à un utilisateur de saisir un commentaire en langue Ewe et d'obtenir une prédiction de sentiment.

### Lancement

```bash
pip install streamlit scikit-learn nltk
streamlit run Deploiement.py
```

### Pipeline de prédiction dans l'app

```python
# 1. Nettoyage du texte saisi
tmp = re.sub(r'\d+', ' ', text)       # Supprime les nombres
tmp = re.sub(r'\s+', ' ', tmp)        # Supprime les espaces multiples
tmp = tmp.lower()                      # Minuscules
tmp = re.sub(r'[^\w\s]', '', tmp)     # Élimine la ponctuation

# 2. Vectorisation TF-IDF
X = vect.transform([tmp]).toarray()

# 3. Prédiction
pred = model.predict(X)               # → ['Positive'] / ['Negative'] / ['Neutre']
```

### Prérequis

```
streamlit
scikit-learn
nltk
pickle
```

---

## 💡 Applications potentielles

- **Marketing et Publicité** : Analyser les perceptions des consommateurs pour ajuster les stratégies.
- **Communication et Interaction** : Mieux comprendre les émotions dans les messages et commentaires.
- **Analyse de sondages** : Identifier les attitudes et opinions du public à grande échelle.

---

## 🔭 Perspectives futures

1. **Étendre la collecte de données** annotées dans différents domaines et registres de la langue Ewe pour améliorer la robustesse du modèle.
2. **Explorer des approches multilingues** intégrant d'autres langues africaines similaires pour tirer parti des similarités linguistiques.

---

## 👩‍💻 Auteure

| Nom | Institution |
|-----|-------------|
| Gnuito Débora | I3-FSS |

---

*Akpe na mi ɖe miaƒe ɖetsɔlemea ta 🙏*
