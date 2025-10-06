    (function(){
      const canvas = document.getElementById('snakeCanvas');
      const ctx = canvas.getContext('2d');
      const cw = canvas.width;
      const ch = canvas.height;
      const grid = 16;
      let snake, dir, food, gameInterval;

      function startSnake() {
        stopSnake();
        snake = [{x:8, y:8}];
        dir = {x:1, y:0};
        spawnFood();
        gameInterval = setInterval(gameStep, 120);
      }

      function stopSnake() {
        if (gameInterval) clearInterval(gameInterval);
        gameInterval = null;
      }

      function spawnFood() {
        food = {
          x: Math.floor(Math.random() * (cw / grid)),
          y: Math.floor(Math.random() * (ch / grid))
        };
      }

      function gameStep() {
        const head = {x: snake[0].x + dir.x, y: snake[0].y + dir.y};
        head.x = (head.x + cw/grid) % (cw/grid);
        head.y = (head.y + ch/grid) % (ch/grid);
        if (snake.some(s => s.x === head.x && s.y === head.y)) {
          stopSnake();
          alert('Game Over - recarga la página para jugar otra vez');
          return;
        }
        snake.unshift(head);
        if (head.x === food.x && head.y === food.y) {
          spawnFood();
        } else {
          snake.pop();
        }
        drawSnake();
      }

      function drawSnake() {
        ctx.clearRect(0, 0, cw, ch);
        ctx.fillStyle = 'orange';
        ctx.fillRect(food.x * grid, food.y * grid, grid-1, grid-1);
        ctx.fillStyle = 'lime';
        snake.forEach(s => {
          ctx.fillRect(s.x * grid, s.y * grid, grid-1, grid-1);
        });
      }

      document.addEventListener('keydown', (e) => {
        if (!gameInterval) return;
        if (e.key === 'ArrowUp' && dir.y === 0) dir = {x:0, y:-1};
        if (e.key === 'ArrowDown' && dir.y === 0) dir = {x:0, y:1};
        if (e.key === 'ArrowLeft' && dir.x === 0) dir = {x:-1, y:0};
        if (e.key === 'ArrowRight' && dir.x === 0) dir = {x:1, y:0};
      });

      startSnake();
    })();