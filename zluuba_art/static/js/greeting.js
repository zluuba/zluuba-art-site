var greetings = [
    { greeting: "こんにちは", weight: 7 },     // Japanese
    { greeting: "안녕하세요", weight: 2 },     // Korean
    { greeting: "Bonjour", weight: 1 },     // French
    { greeting: "Привіт", weight: 1 },      // Ukrainian
    { greeting: "Hello", weight: 1 },       // English
    { greeting: "Hallo", weight: 1 },       // German
    { greeting: "Salut", weight: 1 },       // Romanian
    { greeting: "Olá", weight: 1 },         // Portuguese
];

function changeGreeting() {
    var totalWeight = greetings.reduce((acc, curr) => acc + curr.weight, 0);
    var randomWeight = Math.random() * totalWeight;

    var chosenGreeting;
    var accumulatedWeight = 0;

    greetings.some(function(greetingObj) {
        accumulatedWeight += greetingObj.weight;
        if (randomWeight < accumulatedWeight) {
            chosenGreeting = greetingObj.greeting;
            return true;
        }
    });

    if (chosenGreeting.length) {
        document.getElementById("greeting").textContent = chosenGreeting;
    }
}

changeGreeting();
