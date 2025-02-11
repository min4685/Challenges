(function() {
    console.log("hint : show");
 
    let foundX = function() {
        fetch('/get-p1-clue')
            .then(response => response.json())
            .then(data => {
                alert(data.clue1);
            })
            .catch(error => {
                console.error('단서를 가져오는 중 오류 발생:', error);
                alert('단서를 불러올 수 없습니다.');
            });
    };
 
    window.showX = function(input) {
        console.log("Ernql be abg, urer V pbzr!");
        fetch(`/verify/${input}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let button = document.getElementById('hiddenX');
                    
                    // 랜덤 위치 설정
                    const randomTop = Math.floor(Math.random() * (window.innerHeight - 50)) + 'px';
                    const randomLeft = Math.floor(Math.random() * (window.innerWidth - 50)) + 'px';
                    
                    button.style.position = 'fixed';
                    button.style.top = randomTop;
                    button.style.left = randomLeft;
                    button.style.display = 'block';
                    button.onclick = foundX;
                    
                    console.log("찾았다!");
                } else {
                    console.log("여기가 아닌가?");
                }
            });
    };
 })();