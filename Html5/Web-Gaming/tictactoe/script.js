    (function(){
      const boardEl = document.getElementById('boardTTT');
      const turnEl = document.getElementById('turnTTT');
      const resetBtn = document.getElementById('resetTTT');
      let board = Array(9).fill('');
      let turn = 'X';
      let running = true;

      function renderTTT() {
        boardEl.innerHTML = '';
        for(let i = 0; i < 9; i++) {
          const cell = document.createElement('div');
          cell.style.display = 'flex';
          cell.style.alignItems = 'center';
          cell.style.justifyContent = 'center';
          cell.style.border = '1px solid rgba(255,255,255,0.06)';
          cell.style.fontSize = '44px';
          cell.style.cursor = 'pointer';
          cell.textContent = board[i];
          cell.addEventListener('click', () => onCell(i));
          boardEl.appendChild(cell);
        }
      }

      function onCell(i) {
        if(!running || board[i]) return;
        board[i] = turn;
        renderTTT();
        if(checkWinTTT(turn)) {
          running = false;
          setTimeout(() => alert(turn + ' gana!'), 50);
        } else if(board.every(c => c)) {
          running = false;
          setTimeout(() => alert('Empate'), 50);
        } else {
          turn = turn === 'X' ? 'O' : 'X';
          turnEl.textContent = turn;
        }
      }

      function checkWinTTT(p) {
        const wins = [
          [0,1,2], [3,4,5], [6,7,8], // filas
          [0,3,6], [1,4,7], [2,5,8], // columnas
          [0,4,8], [2,4,6]           // diagonales
        ];
        return wins.some(line => line.every(i => board[i] === p));
      }

      function resetTTT() {
        board = Array(9).fill('');
        turn = 'X';
        running = true;
        turnEl.textContent = turn;
        renderTTT();
      }

      resetBtn.addEventListener('click', resetTTT);
      renderTTT();
    })();