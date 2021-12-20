```sql
--
SELECT *
FROM "get_fit_now_check_in"
--
SELECT *
FROM "get_fit_now_check_in"
WHERE "check_in_date"=20180115
-- La je réalise que ce n'est pas ce qu'il faut chercher
SELECT *
FROM "crime_scene_report"
--
SELECT *
FROM "crime_scene_report"
WHERE "date"=20180115 AND "city"='SQL City' AND "type"='murder'
--
/*
Security footage shows
that there were 2 witnesses.
The first witness lives at the
last house on "Northwestern Dr".
The second witness, named Annabel,
lives somewhere on "Franklin Ave".
*/
--
SELECT *
FROM "person"
WHERE "address_street_name"='Northwestern Dr'
--
SELECT MAX(address_number)
FROM "person"
WHERE "address_street_name"='Northwestern Dr'
--
SELECT *
FROM "person"
WHERE "address_street_name"='Northwestern Dr' AND "address_number"=4919
-- Firt witness found
SELECT *
FROM "person"
WHERE "address_street_name"='Franklin Ave' 
-- Second witness found
-- Je regarde si l'un des deux va a la salle (ce que je suppose être une salle de sport)
SELECT *
FROM "get_fit_now_member"
WHERE "person_id"=16371 OR "person_id"=14887
-- Annabel est inscrite
SELECT *
FROM "get_fit_now_check_in"
WHERE "membership_id"=90081
-- La je viens de regarder si Annabel est déjà allé a la salle
-- Je regarde si l'un d'eux a eu une interview
SELECT *
FROM "interview"
WHERE "person_id"=16371 OR "person_id"=14887
-- Morty dit qu'il a vu une personne avec un sac get_fit que seuls les golds peuvent avoir alors je vais regarder ça
SELECT *
FROM "get_fit_now_member"
WHERE "membership_status"='gold' AND CHARINDEX('48Z', id) > 0
-- J'obtient deux noms alors je vais regarder par rapport a la plaque d'immatriculation
SELECT * 
FROM "person"
WHERE "name" = 'Joe Germuska' OR "name" = 'Jeremy Bowers'
-- La j'obtient les numéros de license
SELECT * 
FROM "drivers_license"
WHERE "id" = 173289 OR "id" = 423327
-- J'ai trouvé Jeremy Bowers
SELECT * 
FROM "get_fit_now_check_in"
WHERE "check_in_date"=20180109 AND "membership_id"='48Z55'
-- Jeremy est allé au même moment que le deuxième témoin
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
        
        SELECT value FROM solution;
-- J'ai trouvé le meurtrier c'était Jeremy mais apparemment quelqu'un d'encore plus méchant est a trouver (Je l'ai trouvé lui parce que tout coller avec les témoignages)
```

First witness: ![[Pasted image 20211223214630.png]]
Second witess: ![[Pasted image 20211223215706.png]]
Annabel membre salle sport: ![[Pasted image 20211223221100.png]]
Elle est allée a la salle une seule fois pendant 1h avant le meurtre (15 janv. 2018) :![[Pasted image 20211223221230.png]]
Résultat des interviews:![[Pasted image 20211223221618.png]]
Résultats recherche gold et morceau de sac: ![[Pasted image 20211223222455.png]]
Résultats pour numéros de license: ![[Pasted image 20211223222736.png]]
J'arrive a trouver Jemery Bowers et la plaque d'immatriculation colle avec le témoignage: ![[Pasted image 20211223223016.png]]
Jeremy temps ou il y est allé: ![[Pasted image 20211223223750.png]]
Une fois la fin entrée: ![[Pasted image 20211223224407.png]]