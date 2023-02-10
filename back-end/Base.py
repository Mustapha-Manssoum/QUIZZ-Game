# ce fichier gere la communication dans la V1 qu'on a abondonné 
# ce fichier decrit  la gestion de la communication avec sa base de donnees
# rédiger par zouine safouane
import sqlite3

x = print("---------------------------------------------")


class Base:
    def __init__(self):
        self.path = "../base.db"
        self.requetteTableUser = """ CREATE TABLE IF NOT EXISTS user(
                            pseudo text PRIMARY KEY NOT NULL,
                            mdp text NOT NULL,
                            score int NOT NULL);"""
        self.requetteTableQuestion = """ CREATE TABLE IF NOT EXISTS question(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Text text  NOT NULL,
                                    nb_rep int NOT NULL,
                                    reponse text NOT NULL,
                                    rep_correcte text NOT NULL,
                                    cetegorie text NOT NULL);"""
        self.db = sqlite3.connect(self.path)
        if self.db:
            print("---------------------------------------------")
            print(" --> start ")
            print(" --> etablissement de connexion")
            print(" --> connexion reussi")
    def __creation_table__(self):
            
            print(" --> creation de table user")
            self.__create_table_user__()
            print(" --> creation reussie")
            print(" --> creation de table question")
            self.__create_table_question__()
            print(" --> creation reussie")

    def __create_table_user__(self):
        self.db.execute(self.requetteTableUser)
    def __create_table_question__(self):
        self.db.execute(self.requetteTableQuestion)

    def __get_user__(self,pseudo):
        print(" --> req : get user name = {}".format(pseudo))
        req = " SELECT * FROM user WHERE pseudo = '{}'".format(pseudo)
        liste = []
        try:
            rep = self.db.execute(req)

            for r in rep:
                print(" --> rep : ", r)
                liste.append(r)

        except :
            print(" --> user introuvable ")
        return liste
    def __get_question__(self,id):
        print(" --> req : get question  id = {}".format(id))
        req = " SELECT * FROM question WHERE id = {}".format(id)
        rep = ""
        try :
            repo = self.db.execute(req)
            for r in repo:
                print(" --> rep : ", r)
                rep = r
        except :
            print(" --> question introuvable ")
        return rep
    def __add_user__(self,psd,mdp):
        print("---------------------------------------------")
        print(" --> req : add user  name = {} , mpt de passe  = {} ".format(psd, mdp))
        requette = " INSERT INTO  user(pseudo,mdp,score) VALUES('{}','{}','0')".format(psd,mdp)
        try :
            rep = self.db.execute(requette)
            print(" --> execution reussie ")
        except sqlite3.IntegrityError as e:
            print(" --> erreur req add user : le pseudo '{}'  est occupé par un autre user".format(psd))

    def __add_question__(self,qst,lst_rep):
        print("---------------------------------------------")
        reponse = ""
        for s in lst_rep :
            reponse += "{};".format(s)
        print(" --> req :  add question  text = '{}' ,nombre reponse  = '{}', reponse = '{}' ".format(qst, len(lst_rep),
                                                                                                      reponse))
        requette = " INSERT INTO  question(Text,reponse) VALUES('{}','{}')".format(qst,reponse)
        try:
            rep = self.db.execute(requette)
            print(" --> execution reussie ")
        except sqlite3.IntegrityError as e:
            print(" --> erreur req add question : la question  '{}' existe deja ".format(qst))
    def __delObject__(self,nomTable,parametre_identification):
        print("---------------------------------------------")
        curseur = self.db.cursor()
        if nomTable == 'user' :
            req = "DELETE FROM user WHERE pseudo = ?"
            curseur.execute(req,(parametre_identification,))
            print(" --> suppression  user  '{}' avec succes".format(parametre_identification))
        elif nomTable == 'question' :
            req = "DELETE FROM question WHERE  Text =?"
            curseur.execute(req,(parametre_identification,))
            print(" --> suppression  de la question '{}' avec succes".format(parametre_identification))
        else :
            print(" --> Table '{}' non existante dans la base de donnes".format(nomTable))
    def __delTable__(self,name):
        print("---------------------------------------------")
        if name == "user" :
            req = "DROP TABLE IF EXISTS user"
        elif name == "question" :
            req = "DROP TABLE IF EXISTS  question"
        elif name == "all" :
            req = "DROP TABLE IF EXISTS user"
            self.db.execute(req)
            req = "DROP TABLE IF EXISTS  question"
        self.db.execute(req)
        print(" --> suppression  des tables {} avec succes".format(name))
    def __getAllUser__(self):
        print("---------------------------------------------")
        print(" --> req get all user")
        req = "SELECT * FROM user;"
        users = self.db.execute(req)
        liste = []
        for user in users:
            name_ = user[0]
            mdp_ = user[1]
            score = user[2]
            utilissateur = User(name_, mdp_)
            utilissateur.__setScore__(score)
            liste.append(utilissateur)
        return liste
    def __getAllQuestion__(self):
        print("---------------------------------------------")
        print(" --> req get all question")
        req = "SELECT * FROM question;"
        questions = self.db.execute(req)
        liste = []
        for question in questions:
            id = question[0]
            qst = question[1]
            reponses = question[2]
            qst = Question(qst, reponses)
            liste.append(qst)
        return liste
    def commit(self):
        self.db.commit()
    def verificationConnexion(self,name,mdp):
        print("---------------------------------------------")
        print(" --> req : demande  d'authetification : pseudo = '{}', mdp = '{}' ".format(name,mdp))
        users = self.__get_user__(name)
        name_ = ""
        mdp_ = ""
        for user in users :
            name_ = user[1]
            mdp_ = user[2]
            print(" --> connexion user reussie ? --> ", name_ == name and mdp_ == mdp)
            return (name_ == name and mdp_ == mdp)
            break
    def __getUser__(self,nom):
        users  = self.__get_user__(pseudo=nom)
        name_ = ""
        mdp_ = ""
        for user in users :
            name_ = user[0]
            mdp_ = user[1]
            score = user[2]
        utilissateur = User(name_,mdp_)
        utilissateur.__setScore__(score)
        return utilissateur
    def __getQuestion__(self,text):
        question  = self.__get_question__(text)
        qst_ = ""
        reponses = ""
        for qst in question :
            qst_ = qst[0]
            reponses = qst[1]
        qst = Question(qst_,reponses)
        return qst

class User:
    def __init__(self,user_p,user_mdp):
        self.pseudo = user_p
        self.mdp_ = user_mdp
        self.score = 0
    def __get__(self,obj,objtype=None):
        return [self.pseudo,self.mdp_,self.score]
    def __setScore__(self,score):
        self.score = score

class Question:
    def __init__(self,qst,liste_rep):
        self.qst_ = qst
        self.liste_rep_ = liste_rep
        self.reponse_correcte = ""
    def __get__(self):
        return [self.qst_,self.liste_rep_,self.reponse_correcte]
b = Base()
b.__creation_table__()
print(b.__add_question__("est ?",["a","b"]))
s = b.__getAllQuestion__()
for ss in s :
    print(ss.qst_)
b.commit()
