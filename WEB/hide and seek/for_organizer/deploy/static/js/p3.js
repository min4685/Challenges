(function() {
    window.submitAnswer = function() {
        const answer = document.getElementById('answer').value;
        
        fetch('/3/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ answer: answer })
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert(data.message);
            } else {
                alert("내가 아는 것과 다른데?");
            }
        });
    };
})();