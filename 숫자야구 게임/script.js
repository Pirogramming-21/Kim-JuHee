let targetNumbers = [];
let attemptsLeft = 9;

// 문서의 DOM 콘텐츠가 완전히 로드되었을 때 이벤트 발생
document.addEventListener("DOMContentLoaded", initializeGame);

function initializeGame() {
    attemptsLeft = 9;
    targetNumbers = generateRandomNumbers();
    clearInputs();
    clearResults();
    updateResultImage('');
    enableSubmitButton(true);
}

function generateRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const rand = Math.floor(Math.random() * 10);
        if (!numbers.includes(rand)) {
            numbers.push(rand);
        }
    }
    return numbers;
}

function clearInputs() {
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
}

function clearResults() {
    document.querySelector('.result-display').innerHTML = '';
}

function updateResultImage(src) {
    document.getElementById('game-result-img').src = src;
}

function enableSubmitButton(enable) {
    document.querySelector('.submit-button').disabled = !enable;
}

function check_numbers() {
    const num1 = document.getElementById('number1').value;
    const num2 = document.getElementById('number2').value;
    const num3 = document.getElementById('number3').value;

    if (num1 === '' || num2 === '' || num3 === '') {
        alert("Please enter all three numbers.");
        clearInputs();
        return;
    }

    const guess = [parseInt(num1), parseInt(num2), parseInt(num3)];
    const result = checkGuess(guess);

    displayResult(guess, result);

    attemptsLeft--;
    if (result.strikes === 3) {
        updateResultImage('success.png');
        enableSubmitButton(false);
    } else if (attemptsLeft === 0) {
        updateResultImage('fail.png');
        enableSubmitButton(false);
    }

    clearInputs();
}

function checkGuess(guess) {
    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === targetNumbers[i]) {
            strikes++;
        } else if (targetNumbers.includes(guess[i])) {
            balls++;
        }
    }

    if (strikes === 0 && balls === 0) {
        return { out: true, strikes: 0, balls: 0 };
    } else {
        return { out: false, strikes: strikes, balls: balls };
    }
}

function displayResult(guess, result) {
    // 결과를 표시할 부모 요소 선택
    const resultDisplay = document.querySelector('.result-display');

    // 결과를 표시할 새로운 'div' 요소 생성
    const resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';

    // 입력한 숫자를 표시할 'div' 생성
    const leftDiv = document.createElement('div');
    leftDiv.className = 'left';
    leftDiv.textContent = guess.join(' ');

    // 결과를 표시할 'div' 생성
    const rightDiv = document.createElement('div');
    rightDiv.className = 'right';

    // 아웃(스트라이크와 볼 모두 0)
    if (result.out) {
        const outDiv = document.createElement('div');
        outDiv.className = 'out num-result';
        outDiv.textContent = 'O';
        rightDiv.appendChild(outDiv);

    // 스트라이크와 볼 결과    
    } else {
        const strikesDiv = document.createElement('div');
        strikesDiv.className = 'strike num-result';
        strikesDiv.textContent = `${result.strikes} S`;

        const ballsDiv = document.createElement('div');
        ballsDiv.className = 'ball num-result';
        ballsDiv.textContent = `${result.balls} B`;

        rightDiv.appendChild(strikesDiv);
        rightDiv.appendChild(ballsDiv);
    }

    // 최종적으로 결과를 DOM에 추가
    resultDiv.appendChild(leftDiv);
    resultDiv.appendChild(rightDiv);
    resultDisplay.appendChild(resultDiv);
}
