const generateButton = document.getElementById("generateBtn")
const clearButton = document.getElementById("clearBtn")
const colorInput = document.getElementById('colorCount')
const palette = document.getElementById("palette")
const message = document.getElementById("message")
const countHeading = document.getElementById("countHeading")
const copyFormat = document.getElementById("copyFormat")

const gradientBtn = document.getElementById("gradientBtn")
const gradientPreview = document.getElementById("gradientPreview")
const gradientCode = document.getElementById("gradientCode")

let selectedGradientBoxes = []

let messageTimeout;


function selectForGradient(event) {
    const box = event.currentTarget

    if (box.classList.contains("gradient-selected")) {
        box.classList.remove("gradient-selected")
        selectedGradientBoxes = selectedGradientBoxes.filter(item => item !== box)
        return;
    }
    if (selectedGradientBoxes.length < 2) {
        box.classList.add("gradient-selected")
        selectedGradientBoxes.push(box)
    }
    else {
        selectedGradientBoxes[0].classList.remove("gradient-selected")
        selectedGradientBoxes.shift()
        box.classList.add("gradient-selected")
        selectedGradientBoxes.push(box)
    }
}

// #f6f4f8
function hexToRgb(hex) {
    const red = parseInt(hex.slice(1, 3), 16)
    const green = parseInt(hex.slice(3, 5), 16)
    const blue = parseInt(hex.slice(5, 7), 16)
    // '' `` template literals
    return `rgb(${red}, ${green}, ${blue})`
}

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

function showMessage(text) {
    clearTimeout(messageTimeout)
    message.innerText = text
    messageTimeout = setTimeout(function () {
        message.innerText = "";
    }, 2000);
}

function copyColor(event) {
    // const colorText = event.currentTarget.querySelector("span").innerText
    // navigator.clipboard.writeText(colorText)
    // showMessage(colorText + " copied to clipboard!")

    const hexColor = event.currentTarget.querySelector("span").innerText
    let copiedValue = hexColor

    if (copyFormat.value === 'rgb') {
        copiedValue = hexToRgb(hexColor)
    }
    navigator.clipboard.writeText(copiedValue)
    showMessage(copiedValue + " copied to clipboard!")
}

function toggleLock(event) {
    event.stopPropagation()

    const box = event.currentTarget.parentElement
    const isLocked = box.dataset.locked === 'true'

    if (isLocked) {
        box.dataset.locked = 'false'
        box.classList.remove('locked')
        event.currentTarget.innerText = '🔓'
    } else {
        box.dataset.locked = 'true'
        box.classList.add('locked')
        event.currentTarget.innerText = '🔒'
    }
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

        box.dataset.locked = 'false'
        const lockBtn = document.createElement("button")
        // lockBtn.innerText = 'Lock' Windows Key + .
        lockBtn.innerText = '🔓'
        lockBtn.classList.add("lock-btn")

        lockBtn.addEventListener("click", toggleLock)

        box.appendChild(span)
        box.appendChild(lockBtn)
        palette.appendChild(box)

        box.addEventListener("click", copyColor)
        box.addEventListener("dblclick", selectForGradient)
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
        showMessage("Maximum limit is 20 colours")
    } else {
        clearMessage()
    }
    //createBoxes(number) //OLD CODE
    const boxes = document.querySelectorAll(".color-box")

    if (boxes.length == 0) {
        createBoxes(number)
    } else {
        boxes.forEach(box => {
            if (box.dataset.locked !== 'true') {
                const newColor = generateColor()
                box.style.backgroundColor = newColor
                box.querySelector("span").innerText = newColor
            }
        });
    }
}
function clearMessage() {
    message.innerText = ""
}
function handleKeyPress(event) {
    if (event.key === 'g' || event.key === 'G') {
        generatePalette()
    }
}

function generateGradient() {
    if (selectedGradientBoxes.length !== 2) {
        showMessage("Please select at least 2 colours for the gradient")
        return;
    }
    const color1 = selectedGradientBoxes[0].querySelector('span').innerText
    const color2 = selectedGradientBoxes[1].querySelector('span').innerText

    const gradientCss = `linear-gradient(to right, ${color1}, ${color2})`
    gradientPreview.style.background = gradientCss
    gradientCode.innerText = `background:${gradientCss}`

}


generateButton.addEventListener("click", generatePalette)
clearButton.addEventListener("click", clearMessage)
document.addEventListener("keydown", handleKeyPress)
gradientBtn.addEventListener("click", generateGradient)

colorInput.value = 4
generatePalette()