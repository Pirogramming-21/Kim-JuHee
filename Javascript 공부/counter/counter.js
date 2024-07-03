const minusBtn = document.getElementById('minus');
const countText = document.getElementById('cnt')
const plusBtn = document.getElementById('plus')

minusBtn.addEventListener('click', () => {
    countText.innerText = Number(countText.innerText) - 1;
})

plusBtn.addEventListener('click', () => {
    countText.innerText = Number(countText.innerText) + 1;
})