var greetings = [
    "こんにちは",        // Japanese
    "안녕하세요",        // Korean
    "Bonjour",        // French
    "Привіт",         // Ukrainian
    "Hello",          // English
    "Hallo",          // German
    "Salut",          // Romanian
    "Olá",            // Portuguese
];

function changeGreeting() {
    var randomIndex = Math.floor(Math.random() * greetings.length);
    var randomGreeting = greetings[randomIndex];
    document.getElementById("greeting").textContent = randomGreeting;
}

changeGreeting();
