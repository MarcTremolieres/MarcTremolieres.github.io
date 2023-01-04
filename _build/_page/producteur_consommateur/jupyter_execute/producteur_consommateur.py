#!/usr/bin/env python
# coding: utf-8

# # Terminale NSI : Le problème du producteur et du consommateur

# ## Introduction

# Dans ce problème classique de programmation concurrente on considère 3 éléments :
# - Un tampon de stockage (_buffer_) dans lequel on peut écrire, lire ou supprimer des données.
# - Un producteur, qui est un _thread_ qui écrit des données dans le tampon tant qu'il n'est pas plein.
# - Un consommateur, qui est un _thread_ qui lit et supprimme des données du tampon.

# Il est important de noter que le producteur et le consommateur sont des _threads_ et n'interviennent donc pas de façon synchronisée.<br>
# <br>
# 
# ![](producer-consumer.png)
# 
# <br>

# ## Modèle élémentaire

# ### Base
# - Le tampon est une liste python partagée comme variable globale.
# - Le producteur est une fonction qui écrit dans le tampon des nombres entiers aléatoires. Cette fonction admet un paramètre qui est la taille maximale du tampon. A chaque écriture le tampon est affiché
# - Le consommateur est une fonction qui supprimme et affiche le dernier élément du tampon, sauf si il est vide.

# In[1]:


from threading import Thread
from random import randint

def producteur(n):
    "A compléter"
    global tampon
    pass

def consommateur():
    "A compléter"
    global tampon
    pass

tampon = []
produit = Thread(target = producteur, args = [10])
consomme = Thread(target = consommateur)
produit.start()
consomme.start()


# ### Temporisation
# - Améliorer le résultat en ajoutant une pause ( _sleep_ ) dans chaque thread.
# - Étudier l'influence des temps de pause sur la taille du tampon
# - Simuler un situation plus réaliste avec des temps de pause aléatoires.

# ### Verrouillage en lecture-écriture
# Avec le programme actuel il est possible que les deux threads interviennent en même temps sur le tampon, provoquant un résultat incohérent.<br>
# Corriger ce problème en utilisant un verrou global _operation_ autour des opérations de lecture-écriture sur le tampon. 

# ## Synchronisation des threads

# ### Position du problème
# - Avec le programme actuel les deux threads exécutent une boucle infinie en vérifiant à chaque fois si il est possible d'écrire ou de lire sur le tampon.<br>
# - Si par exemple le tampon est plein le producteur utilise tout son temps de CPU à vérifier qu'il est toujours plein.<br>
# - C'est la situation d'attente active ( _busy-wait_).
# - L'inconvénient est de consommer du temps de CPU à la place d'être en sommeil.
# 

# ### Utilisation d'un verrou de synchronisation
# - On va utiliser un verrou _plein_ pour signifier que le tampon est plein.
# - Le producteur tentera d'abord d'acquérir le verrou _plein_. <br>
#     - Si il y parvient c'est que le tampon n'est pas plein. Il peut alors écrire et relâcher ou non le verrou ( selon que le tampon est plein ou pas ).
#     - Si il n'y parvient pas c'est que le tampon est plein et il reste en attente sans consommer de temps CPU.
# - Le consommateur testera le verrou _plein_ à chaque itération. Si il est verrouillé il sera alors relâché.

# Modifier le programme précédent pour implémenter cette technique.

# ### Perfectionnement
# Adapter la méthode précédente avec un verrou _vide_ pour éviter l'état d'attente active du consommateur lorsque le tampon est vide.

# ## Exercices

# ### Exercice 1

# - On suppose maintenant que le consommateur ne peut consommer que lorsque le tampon est plein.
# - Le consommateur vide alors entièrement le tampon.
# - Adapter le programme précédent en synchronisant 2 threads qui réalisent cette situation.

# ### Exercice 2

# - Un thread écrit les nombres entiers consécutifs dans une variable globale.
# - Un thread affiche en boucle la valeur de cette variable globale.
# - Synchroniser les deux threads pour que chaque nombre soit affiché une fois et une seule.
