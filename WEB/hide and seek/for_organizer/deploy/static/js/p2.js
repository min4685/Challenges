function submitMessage() {
    let textarea = document.querySelector('textarea');
    let message = textarea.value.trim(); 
    
    if (!message) {
        alert("내용을 입력해주세요.");
        return;
    }
    
    fetch('/2/submit', {
        method: 'POST',
        headers: {
            'X-P2-Header1': 'What day is it today?',
            'X-P2-Header2': 'input secret header!',
            'X-P2-Header3': 'yyyy-mm-dd',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        textarea.value = '';
        alert(data.message || data.flag);
    });
}