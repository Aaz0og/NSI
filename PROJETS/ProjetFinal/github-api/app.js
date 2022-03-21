import XMLHttpRequest from 'xmlhttprequest';

function requestUserRepos(username){
    // Créer un object de requête XMLHttpRequest
    const xhr = new XMLHttpRequest();
    // Définir le End point pour GitHub, en mettant un username dynamique
    const url = `https://api.github.com/users/${username}/repos`;
    // Ouvrir une nouvelle connexion, En utilisant une requête GET via un point de fin URL
    // En donnant 3 arguments (GET/POST, L'URL, Async True/False)
    xhr.open('GET', url, true);

    // Quand la requête est recue 
    // La gérer ici
    xhr.onload = function() {
        // Données API en Json 
        const data = JSON.parse(this.response);

        // Faire un log
        console.log(data);

    }

    // Envoyer la requête au serveur
    xhr.send();
}

// Appeller la fonction avec le pseudo choisi
requestUserRepos('Aaz0og');
