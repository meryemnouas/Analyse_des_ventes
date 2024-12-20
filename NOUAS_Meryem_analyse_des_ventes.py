# -*- coding: utf-8 -*-
"""NOUAS_Meryem_Analyse_des_ventes.ipynb

Automatically generated by Colab.


# **Analyse des ventes**


Ce mini-projet illustre comment utiliser Pandas pour charger, manipuler et analyser des données, ainsi que Matplotlib pour créer des visualisations pertinentes permettant de mieux comprendre les tendances et les motifs présents dans les ventes mensuelles d'une entreprise.

Supposons que vous avez un ensemble de données contenant des ventes pour une entreprise.


Ce code génère des données de ventes mensuelles fictives pour une année (2022 dans cet exemple) avec des montants aléatoires compris entre 10 000 et 50 000. Les données sont ensuite enregistrées dans un fichier CSV nommé "ventes_mensuelles.csv".

Vous pouvez utiliser ce jeu de données CSV généré pour ce  projet d'analyse des ventes mensuelles à l'aide de Pandas et Matplotlib.

vous pouvez toujours génèré  des données au cas de besoin (commes les clients, la marque...).
"""

import pandas as pd
import numpy as np
import calendar
import random

# Génération de données factices pour les ventes mensuelles avec catégorie, région, tendance saisonnière et annuelle
np.random.seed(42)  # Pour la reproductibilité des résultats

# Générer des dates pour chaque mois de l'année
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='MS')

# Création d'un ensemble de catégories et de régions fictives
categories = ['Electronique', 'Mode', 'Maison', 'Jouets']
regions = ['Nord', 'Sud', 'Est', 'Ouest']
products = ['Ordinateur', 'T-shirt', 'Canapé', 'Peluche']

# Générer des ventes mensuelles aléatoires pour chaque catégorie et région :
data = []

for month in dates:
      for category in categories:
            for product in products:
                    for region in regions:
                            for year in dates :
                                  vente = np.random.randint(1000, 10000)
                                  client = np.random.randint(1, 100)
                                  data.append([month, category, product, region, vente, client,year])


# Création du DataFrame :
df = pd.DataFrame(data, columns=['Date', 'Catégorie', 'Produit', 'Région', 'Ventes', 'Client', 'Année'])

# Convertir la colonne 'Date' en type datetime :
df['Date'] = pd.to_datetime(df['Date'])

# Ajoute de colonnes pour la tendance saisonnière et annuelle :
df['Tendance_saisonnière'] = df.groupby(df['Date'].dt.month)['Ventes'].transform('mean')
df['Tendance_annuelle'] = df.groupby('Catégorie')['Ventes'].transform('mean')


# Enregistrer les données dans un fichier CSV :
df.to_csv('ventes_mensuelles_cat_reg_tendance_date.csv', index=False)

"""
1. Charger les données avec Pandas :"""

import pandas as pd
import matplotlib.pyplot as plt


# Charger les données à partir du fichier CSV :
data = pd.read_csv('ventes_mensuelles_cat_reg_tendance_date.csv')
data

"""2. Analyse exploratoire :

Explorez les données pour comprendre leur structure et leurs caractéristiques. Vous pouvez utiliser des méthodes telles que info(), describe(), et value_counts() pour obtenir des informations sur les données.
"""

# Afficher les premières lignes du DataFrame :

data.head()

# Informations générales sur les données :

data.info()

# Description statistique des données numériques :

data.describe(include='all')

# Renvoier les types de données de chaque colonne :

data.dtypes

# Nombre de valeurs uniques dans chaque colonne :

data.nunique()

# Nombre de ventes par catégorie :

data['Catégorie'].value_counts()

# Nombre de ventes par région :

data['Région'].value_counts()

# Nombre de ventes par date :

data['Date'].value_counts()

# Afficher les dernières lignes du DataFrame :

data.tail()

# Identifier les valeurs nulles dans le DataFrame:

data.isnull()

# Obtenir le nombre total de valeurs nulles dans chaque colonne :

data.isnull().sum()

# Obtenir le nombre total de lignes en double :

data.duplicated().sum()

# Calculee la moyenne des ventes à partir de la colonne "Ventes" :

mean = data["Ventes"].mean()

# création de 'df_low' qui contient uniquement les lignes où les ventes sont inférieures à la moyenne calculée :

df_low = data[data["Ventes"]<mean]
df_low

# Calculer la moyenne des ventes à partir de la colonne "Ventes" :

mean = data["Ventes"].mean()

# création de 'df_high' qui contient uniquement les lignes où les ventes sont supérieurs à la moyenne calculée :

df_high = data[data["Ventes"]>=mean]
df_high

"""
3. Visualisation avec Matplotlib :

Utilisez Matplotlib pour créer des graphiques qui représentent les tendances et les informations importantes."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visualisation de la tendance des ventes au fil du temps :

plt.figure(figsize=(12, 6))
sns.barplot(data, x='Date', y='Ventes', palette='viridis')
plt.title('Tendance des ventes au fil du temps')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.tight_layout()
plt.show()

# Visualisation des ventes par catégorie :
plt.figure(figsize=(12, 6))
data.groupby('Catégorie')['Ventes'].sum().plot(kind='bar',color="Purple")
plt.title('Les ventes par catégorie')
plt.xlabel('catégorie')
plt.ylabel('Ventes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualisation des ventes par région :
plt.figure(figsize=(10, 6))
data.groupby('Région')['Ventes'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Répartition des ventes par région')
plt.ylabel('')
plt.tight_layout()
plt.show()

"""
4. Autres analyses :

    Comparaison des ventes par produit ou catégorie.
    Visualisation des variations de ventes au fil du temps (tendance saisonnière, tendance annuelle, etc.).
    Analyse des ventes par région ou client, si ces données sont disponibles"""

# Définir une palette de couleurs pour les barres :
palette_couleurs = sns.color_palette("husl", len("Produit"))

# Visualisation des ventes par produit :
plt.figure(figsize=(10, 6))
data.groupby('Produit')['Ventes'].sum().plot(kind='bar', color=palette_couleurs)
plt.title('Comparaison des ventes par produit en 2022')
plt.xlabel('Produit')
plt.ylabel('Ventes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data['Date'] = pd.to_datetime(data['Date'])
# Convertir la colonne 'Date' en datetime :
data['Mois'] = data['Date'].dt.month
# Extraire l'année à partir de la colonne 'Date' :
data['Année'] = data['Date'].dt.year

# Visualisation de la tendance saisonnière :
plt.figure(figsize=(10, 6))
data.groupby(data['Mois'])['Ventes'].sum().plot(marker='o', linestyle='-', color='green')
plt.title('Tendance saisonnière des ventes en 2022')
plt.xlabel('Mois')
plt.ylabel('Ventes moyennes')
plt.xticks(range(1, 13), calendar.month_name[1:13], rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualisation de la tendance annuelle :
plt.figure(figsize=(10, 6))
data.groupby('Année')['Ventes'].sum().plot(kind='bar',color="purple")

plt.title('Tendance annuelle des ventes')
plt.xlabel('Année')
plt.ylabel('Les ventes')
plt.xticks(rotation=360)
plt.tight_layout()
plt.show()

# Analyse des ventes par client :
ventes_par_client = data.groupby('Client')['Ventes'].sum().reset_index()

# Trier les clients par montant de vente :
ventes_par_client = ventes_par_client.sort_values(by='Ventes', ascending=False)

# Afficher les 10 meilleurs clients :
top_clients = ventes_par_client.head(10)
print(top_clients)

# Visualisation des ventes par client :
plt.figure(figsize=(12,6))
plt.bar(top_clients['Client'], top_clients['Ventes'], color='purple')
plt.xlabel('Clients')
plt.ylabel('Montant des ventes')
plt.title('Top 10 des clients par montant de vente')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Comparaison de ventes par rapport à chaque produit et par date :
# Regrouper les ventes par produit et par date :
pivot = data.pivot_table(index='Date', columns='Produit', values='Ventes', aggfunc='sum')

# Créer une nouvelle figure et des sous-graphiques avec la taille spécifiée :
fig, ax = plt.subplots(figsize=(12, 6))

# Tracer un graphique à barres pour les ventes mensuelles par produit :
pivot.plot(kind='bar', ax=ax)
ax.set_title('Ventes mensuelles par produit')
ax.set_xlabel('Date')
ax.set_ylabel('Ventes')
ax.legend(title='Produit', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.tick_params(axis='x', rotation=45)

# Formater les étiquettes de l'axe x pour supprimer le temps et afficher uniquement la date :
ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in pivot.index])

plt.tight_layout()
plt.show()

"""Interpretation :

Les ventes varient d'un produit à l'autre, avec le produit "Ordinateur" de la catégorie "Électronique" ayant les ventes les plus élevées et le produit "Peluche" de la catégorie "Jouets" ayant les ventes les plus basses.Les chiffres des ventes pour les mois restants sont également fournis, indiquant une augmentation constante des ventes pour tous les produits.
"""