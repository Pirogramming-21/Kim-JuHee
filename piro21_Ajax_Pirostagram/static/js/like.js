function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const requestLike = new XMLHttpRequest();

const onClickLike = (id, type) => {
    const url = '/posts/like_ajax/';
    requestLike.open("POST", url, true);
    requestLike.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    requestLike.setRequestHeader("X-CSRFToken", csrftoken);
    requestLike.send(JSON.stringify({ id: id, type: type }));
};

requestLike.onreadystatechange = () => {
    if (requestLike.readyState === XMLHttpRequest.DONE) {
        if (requestLike.status < 400) {
            try {
                const { id, type } = JSON.parse(requestLike.responseText);
                const element = document.querySelector(`.post-id-${id} .post__like-count`);
                
                if (element) {
                    const originHTML = element.innerHTML;
                    const [buttonType, num] = originHTML.split(" ");
                    const count = Number(num) + 1;
                    element.innerHTML = `${buttonType} ${count}`;
                } else {
                    console.error("Element not found for post-id:", id);
                }
            } catch (error) {
                console.error("JSON parsing error:", error);
            }
        }
    }
};
