fetch("https://api.github.com/users/Matthew-Luk")
    .then(response => response.json() )
    .then(coderData => console.log(coderData) )
    .catch(err => console.log(err) )

async function getCoderData() {
    var response = await fetch("https://api.github.com/users/Matthew-Luk");
    var coderData = await response.json();
    return coderData;
}

console.log(getCoderData());

var data = getCoderData()