const generateButton = document.getElementById("generateBtn")
const clearButton = document.getElementById("clearBtn")
const colorInput = document.getElementById('colorCount')
const palette = document.getElementById("palette")
const message = document.getElementById("message")
const countHeading = document.getElementById("countHeading")

function generateColor() {
    const letters = "0123456789ABCDEF"
    let color = "#"
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
    }
    return color

}
function updateColorCount(number) {
    countHeading.innerText = number + " colours on screen"
}
// Create boxes
function createBoxes(number) {
    palette.innerHTML = ""
    for (let i = 0; i < number; i++) {
        const box = document.createElement("div")
        box.classList.add("color-box")

        const span = document.createElement("span")
        const newColor = generateColor()

        box.style.backgroundColor = newColor
        span.innerText = newColor

        box.appendChild(span)
        palette.appendChild(box)

        // box.addEventListener("click", copyColor)
    }
    updateColorCount(number)
}

function generatePalette() {
    let number = parseInt(colorInput.value)

    if (!number || number < 1) {
        number = 5
    }
    if (number > 20) {
        number = 20
        colorInput.value = 20
        // showMessage("Maximum limit is 20 colours")
    } else {
        clearMessage()
    }
    createBoxes(number)
}
function clearMessage() {
    message.innerText = ""
}
function handleKeyPress(event) {
    if (event.key === 'g' || event.key === 'G') {
        generatePalette()
    }
}

generateButton.addEventListener("click", generatePalette)
clearButton.addEventListener("click", clearMessage)
document.addEventListener("keydown", handleKeyPress)
