// I click on a wrong answer - red
// I click on a right answer - green
// the remaining wrong answers stay neutral
// all buttons are becoming disabled.

const questions = [
    {
        question: "What does HTML stand for?",
        answers: [
            { text: "Hyper Text Markup Language", correct: true },
            { text: "Home Tool Markup Language", correct: false },
            { text: "High Tech Main Language", correct: false }
        ]
    },
    {
        question: "Which language is used to style webpages?",
        answers: [
            { text: "CSS", correct: true },
            { text: "HTML", correct: false },
            { text: "Python", correct: false }
        ]
    },
    {
        question: "Which language adds interactivity to webpages?",
        answers: [
            { text: "JavaScript", correct: true },
            { text: "CSS", correct: false },
            { text: "HTML", correct: false }
        ]
    },
    {
        question: "Which JavaScript keyword is used to create a variable?",
        answers: [
            { text: "let", correct: true },
            { text: "button", correct: false },
            { text: "style", correct: false }
        ]
    },
    {
        question: "Which method is used to select an element by ID?",
        answers: [
            { text: "document.getElementById()", correct: true },
            { text: "document.makeElement()", correct: false },
            { text: "document.styleElement()", correct: false }
        ]
    }
];

// DOM - Document Object Model
// Events - event listeners
const questionEl = document.getElementById("question")
const answersEl = document.getElementById("answers")
const scoreEl = document.getElementById("score")
const progressEl = document.getElementById("progress")
const feedbackEl = document.getElementById("feedback")
const finalScoreEl = document.getElementById("final-score")
const resultBox = document.getElementById("result-box")
const quizArea = document.getElementById("quiz-area")
const themeBtn = document.getElementById("theme-btn")
const nextBtn = document.getElementById("next-btn")
const restartBtn = document.getElementById("restart-btn")

let currentQuestionIndex = 0
let score = 0

function startQuiz() {
    currentQuestionIndex = 0
    score = 0
    scoreEl.textContent = "Score: 0"
    quizArea.style.display = 'block'
    resultBox.style.display = 'none'
    showQuestion()
}
function showQuestion() {
    answersEl.innerHTML = ""
    feedbackEl.textContent = ""

    const currentQuestion = questions[currentQuestionIndex]
    questionEl.textContent = currentQuestion.question
    progressEl.textContent = "Question " + (currentQuestionIndex + 1) + " of " + questions.length

    currentQuestion.answers.forEach(function (answer) {
        const button = document.createElement("button")
        button.textContent = answer.text
        button.classList.add("answer-btn")

        if (answer.correct) {
            button.dataset.correct = "true"
        }
        button.addEventListener("click", selectAnswer)
        answersEl.appendChild(button)
    });
}
// = == (values) === (values and the data type)
function selectAnswer(event) {
    // current Target - element the event listener is attached to
    const selectedButton = event.currentTarget
    const isCorrect = selectedButton.dataset.correct === 'true'

    if (isCorrect) {
        selectedButton.classList.add("correct")
        feedbackEl.textContent = "Correct!"
        score++
        scoreEl.textContent = "Score: " + score
    }
    else {
        selectedButton.classList.add("wrong")
        feedbackEl.textContent = "Wrong!"
    }

    const allButtons = answersEl.querySelectorAll("button")

    // If the user clicks the right option, 
    // correct -> green; incorrect -> red
    // If the user clicks the wrong option, 
    // correct -> green; incorrect -> red
    allButtons.forEach(function (button) {
        if (button.dataset.correct === 'true') {
            button.classList.add("correct")
        }
        else {
            button.classList.add("wrong")
        }
        button.disabled = true
    });
}

function goToNextQuestion() {
    currentQuestionIndex++

    if (currentQuestionIndex < questions.length) {
        showQuestion()
    } else {
        showResult()
    }
}

function showResult() {
    quizArea.style.display = 'none'
    resultBox.style.display = 'block'
    finalScoreEl.textContent = "You scored " + score + " out of " + questions.length + "."
}

nextBtn.addEventListener("click", goToNextQuestion)
restartBtn.addEventListener("click", startQuiz)

themeBtn.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode")
});


startQuiz()