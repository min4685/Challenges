(function() {
    window.submitClues = function() {
        const clue1 = document.getElementById('clue1').value;
        const clue2 = document.getElementById('clue2').value;
        const clue3 = document.getElementById('clue3').value;
        
        fetch(`/check-flags`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                clue1: clue1,
                clue2: clue2,
                clue3: clue3
            })
        })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert(data.flag);
            } else {
                alert("그쪽이 아냐!");
            }
        });
    };
})();