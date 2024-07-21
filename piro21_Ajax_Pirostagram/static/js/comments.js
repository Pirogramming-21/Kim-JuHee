document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('commentForm');
    const commentList = document.getElementById('commentList');
    const csrfToken = document.querySelector('meta[name="csrfmiddlewaretoken"]').content;

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const content = document.getElementById('commentContent').value;

        const xhr = new XMLHttpRequest();
        xhr.open('POST', commentForm.action);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                if (data.success) {
                    const newComment = document.createElement('div');
                    newComment.id = `comment-${data.comment.id}`;
                    newComment.innerHTML = `
                        <p>${data.comment.id}. ${data.comment.content}</p>
                        <form class="deleteForm" action="/posts/${data.comment.post}/comment/${data.comment.id}/delete/" method="post">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                            <input type="submit" value="삭제">
                        </form>
                    `;
                    commentList.appendChild(newComment);
                    document.getElementById('commentContent').value = ''; 
                }
            }
        };
        xhr.send(JSON.stringify({ content: content }));
    });

    commentList.addEventListener('submit', function(event) {
        if (event.target.classList.contains('deleteForm')) {
            event.preventDefault();
            const deleteForm = event.target;

            const xhr = new XMLHttpRequest();
            xhr.open('POST', deleteForm.action);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const data = JSON.parse(xhr.responseText);
                    if (data.success) {
                        const commentDiv = document.getElementById(`comment-${data.comment.id}`);
                        commentDiv.remove();
                    }
                }
            };
            xhr.send();
        }
    });
});
