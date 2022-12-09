const button = document.getElementById("click")
button.addEventListener('click', GetJSON)

async function GetJSON() {
    const response = await fetch('http://127.0.0.1:5000/test')
    const data = await response.json()
    console.log(data)
}