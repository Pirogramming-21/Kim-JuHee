const appendTens = document.getElementById("tens");
const appendSeconds = document.getElementById("seconds");
const btnStart = document.getElementById("btn-Start");
const btnStop = document.getElementById("btn-Stop");
const btnReset = document.getElementById("btn-Reset");
const btnSelectAll = document.getElementById("btn-SelectAll");
const btnDelete = document.getElementById("btn-Delete");
const records = document.getElementById("records"); // 기록을 표시할 요소

let seconds = 0;
let tens = 0;
let Interval;
let selectedRecords = []; // 선택된 기록을 추적하는 배열

btnStart.onclick = function () {
    clearInterval(Interval);
    Interval = setInterval(startTimer, 10);
};

btnStop.onclick = function () {
    clearInterval(Interval);
    recordTime(); // 기록을 추가하는 함수 호출
};

btnReset.onclick = function () {
    clearInterval(Interval);
    seconds = 0;
    tens = 0;
    appendSeconds.innerHTML = "00";
    appendTens.innerHTML = "00";
};

btnSelectAll.onclick = function () {
    const recordElements = records.querySelectorAll('.record');
    if (recordElements.length === selectedRecords.length) {
        // 이미 모두 선택된 상태이면 선택 해제
        selectedRecords = [];
        recordElements.forEach(record => {
            record.querySelector("button").innerText = "Select";
        });
    } else {
        // 모두 선택
        selectedRecords = Array.from(recordElements);
        recordElements.forEach(record => {
            record.querySelector("button").innerText = "Selected";
        });
    }
};

btnDelete.onclick = function () {
    selectedRecords.forEach(record => {
        records.removeChild(record);
    });
    btnDelete.style.display = 'inline';
    selectedRecords = []; // 선택된 기록 초기화
};

function startTimer() {
    tens++;

    if (tens <= 9) {
        appendTens.innerHTML = "0" + tens;
    } else {
        appendTens.innerHTML = tens;
    }

    if (tens > 99) {
        seconds++;
        appendSeconds.innerHTML = seconds < 10 ? "0" + seconds : seconds;
        tens = 0;
        appendTens.innerHTML = "00";
    }
}

function recordTime() {
    const record = document.createElement("div");
    record.className = "record";
    record.innerHTML = `
        <button>Select</button>
        ${seconds < 10 ? "0" + seconds : seconds}:${tens < 10 ? "0" + tens : tens}
    `;
    const selectButton = record.querySelector("button");
    selectButton.onclick = function () {
        
        if (selectedRecords.includes(record)) {
            // 이미 선택된 경우 선택 해제
            selectedRecords = selectedRecords.filter(r => r !== record);
            selectButton.innerText = "Select";
        } else {
            // 선택되지 않은 경우 선택
            selectedRecords.push(record);
            selectButton.innerText = "Selected";
        }
    };
    records.appendChild(record);
}
