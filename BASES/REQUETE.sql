INSERT INTO "Classes"("idClasse","nomClasse","profPrincipal") VALUES (26,'TG07',10)

-- REQUETES DE MANIPULATION DONNEES
-- 5 
DELETE
FROM "Eleves"
WHERE 'idEleve' = 701 OR 'idEleve' = 702

-- REQUETES DINTERROGATION
-- 1
SELECT "nom","prenom"
FROM "Eleves"

-- 2
SELECT "nom","prenom"
FROM "Eleves"
WHERE "nom" = 'Wolf'

-- 3
SELECT "profPrincipal" AS IdProfPrincipal
FROM "Classes"
WHERE "nomClasse" = 'TG02'

-- 4
SELECT "nom","prenom"
FROM "Eleves"
WHERE "tuteur" IS NOT NULL

-- 5
SELECT COUNT("note") 
FROM "Notes"
WHERE "note" >12

-- 6
SELECT COUNT("note") 
FROM "Notes"
WHERE "note" =1

-- 7
SELECT COUNT("note") 
FROM "Notes"
WHERE "note">=10 AND "note" <= 20

-- 8
SELECT AVG("note")
FROM "Notes"

-- 9
SELECT *
FROM "Eleves"
ORDER BY "nom","prenom"

-- 10
SELECT "nom","prenom"
FROM "Classes"
JOIN "Professeurs" ON Classes.profPrincipal = Professeurs.idProfesseur
WHERE "nomClasse"='TG05' 

-- 11
SELECT "nom","prenom"
FROM "Professeurs"
ORDER BY "nom"
--TODO A COMPLETER

-- 12
SELECT COUNT("matiere")
FROM "Classes"
JOIN "Cours" ON Classes.idClasse = Cours.classe
WHERE "nomClasse"= 'TG03'

-- 13
SELECT COUNT(*)
FROM "Matieres"
JOIN "Cours" ON Matieres.idMatiere = Cours.matiere
WHERE "idMatiere" = 4

-- 14
SELECT COUNT(*)
FROM "Professeurs"
JOIN "Cours" ON Professeurs.idProfesseur = Cours.professeur
WHERE "nom" = 'Ramos' AND "prenom" = 'Tarik'

-- 15
SELECT DISTINCT "nom","prenom"
FROM "Cours"
JOIN "Professeurs" ON Cours.professeur = Professeurs.idProfesseur
JOIN "Classes" ON Cours.classe = Classes.idClasse
WHERE "nomClasse" = 'TG03'

-- 16
SELECT "nomClasse" 
FROM "Classes"
JOIN "Cours" ON Classes.idClasse = Cours.classe
JOIN "Professeurs" ON Cours.professeur = Professeurs.idProfesseur
JOIN "Matieres" ON Cours.matiere = Matieres.idMatiere
WHERE "nom" = 'Pearson' AND "prenom" = 'Jelani' AND "nomMatiere" = 'NSI'

-- 17 
SELECT DISTINCT Eleves.idEleve,Eleves.nom,Eleves.prenom
FROM "Eleves"
JOIN "Cours" ON Eleves.classe = Cours.classe
JOIN "Professeurs" ON Cours.professeur = Professeurs.idProfesseur
WHERE Professeurs.nom = 'Moreno' AND Professeurs.prenom = 'Jameson'
-- 18
SELECT DISTINCT "nom","prenom"
FROM "Matieres"
JOIN "Cours" ON Matieres.idMatiere = Cours.matiere
JOIN "Professeurs" ON Cours.professeur = Professeurs.idProfesseur
WHERE "nomMatiere" = 'Mathematiques' OR "nomMatiere" = 'NSI'
-- 19
SELECT DISTINCT "nomMatiere"
FROM "Classes"
JOIN "Cours" ON Classes.idClasse = Cours.classe
JOIN "Professeurs" ON Cours.professeur = Professeurs.idProfesseur
JOIN "Matieres" ON Cours.matiere = Matieres.idMatiere
WHERE "idProfesseur" = 2
ORDER BY "nomMatiere" DESC
-- 20
SELECT DISTINCT "nom","prenom"
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
WHERE "nomMatiere" = 'NSI' AND "note" IS NOT NULL
-- 21
SELECT COUNT(*)
FROM "Notes"
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
WHERE "nomMatiere" = 'NSI' AND "note" IS NOT NULL
-- 22
SELECT DISTINCT "nom","prenom"
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
WHERE "nomMatiere" = 'SVT' AND "note" < 10
-- 23 
SELECT DISTINCT "nom","prenom"
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE "note" > 10 AND ("nomMatiere" = 'SVT' OR "nomMatiere" = 'NSI') AND "nomClasse"='TG03'
-- 24 
SELECT MIN("note")
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE "nomMatiere" = 'NSI' AND "nomClasse" = 'TG01'
-- 25 
SELECT AVG("note")
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE ("nom" = 'Dillon' AND "prenom" = 'Porter') 
-- 26
SELECT AVG("note")
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE "nomMatiere" = 'Allemand' AND ("nom" = 'Dillon' AND "prenom" = 'Porter') 
-- 27
SELECT AVG("note")
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE "nomClasse" = 'TG02'
-- 28 
SELECT AVG("note")
FROM "Eleves"
JOIN "Notes" ON Eleves.idEleve = Notes.eleve
JOIN "Matieres" ON Notes.matiere = Matieres.idMatiere
JOIN "Classes" ON Eleves.classe = Classes.idClasse
WHERE "nomClasse" = 'TG02' AND "nomMatiere" = 'NSI'
-- 29 
SELECT DISTINCT E2.nom,E2.prenom
FROM "Eleves" E1
JOIN "Eleves" E2 ON E1.tuteur = E2.idEleve
WHERE E1.tuteur IS NOT NULL 
ORDER BY "nom"
-- 30 
SELECT DISTINCT E1.nom,E1.prenom
FROM "Eleves" E1
JOIN "Eleves" E2 ON E1.tuteur = E2.idEleve
WHERE (E2.nom = 'Cooke' AND E2.prenom = 'Charlotte') 
ORDER BY "nom"