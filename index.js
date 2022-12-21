const highcharts = require('highcharts')
console.log(highcharts)

const button = document.getElementById("click")
button.addEventListener('click', GetJSON)

const text = document.getElementById("text")


async function GetJSON() {
    const response = await fetch('http://127.0.0.1:5000/test')
    const data = await response.json()
    console.log(data)
    data.responses.forEach(response => AppendResponseText(response))

}

const AppendResponseText = (responses) => {
    const p = document.createElement("p")
    p.innerText = JSON.stringify(responses.answers)
    text.appendChild(p)
}

