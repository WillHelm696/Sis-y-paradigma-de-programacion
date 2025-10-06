    // Maze generator: Recursive Backtracker (depth-first search)
    class Cell {
      constructor(r,c){
        this.r=r; this.c=c;
        // walls: top, right, bottom, left
        this.walls=[true,true,true,true];
        this.visited=false;
      }
    }

    class Maze {
      constructor(rows,cols){
        this.rows=rows; this.cols=cols;
        this.grid=[];
        for(let r=0;r<rows;r++){const row=[]; for(let c=0;c<cols;c++) row.push(new Cell(r,c)); this.grid.push(row);} 
      }
      cellAt(r,c){ if(r<0||c<0||r>=this.rows||c>=this.cols) return null; return this.grid[r][c]; }

      generate(){
        // iterative stack version to avoid recursion limits
        const start=this.cellAt(0,0);
        start.visited=true;
        const stack=[start];
        while(stack.length){
          const current=stack[stack.length-1];
          const neighbors=[];
          const {r,c}=current;
          const check = [ [r-1,c,0,2], [r,c+1,1,3], [r+1,c,2,0], [r,c-1,3,1] ];
          for(const [nr,nc,wallIdx,oppIdx] of check){
            const n=this.cellAt(nr,nc);
            if(n && !n.visited) neighbors.push({n,wallIdx,oppIdx});
          }
          if(neighbors.length){
            const pick = neighbors[Math.floor(Math.random()*neighbors.length)];
            // remove wall between current and pick.n
            current.walls[pick.wallIdx]=false;
            pick.n.walls[pick.oppIdx]=false;
            pick.n.visited=true;
            stack.push(pick.n);
          } else {
            stack.pop();
          }
        }
      }
    }

    // --- Rendering & Game logic ---
    const canvas=document.getElementById('mazeCanvas');
    const ctx=canvas.getContext('2d');
    let maze, cellW, cellH, cellSizePx;
    let player={r:0,c:0};
    let exitCell={r:0,c:0};

    function resizeCanvasToDisplay(){
      // keep CSS size but scale drawing resolution for crispness
      const rect=canvas.getBoundingClientRect();
      const ratio=window.devicePixelRatio||1;
      canvas.width=Math.floor(rect.width*ratio);
      canvas.height=Math.floor(rect.height*ratio);
      ctx.setTransform(ratio,0,0,ratio,0,0);
    }

    function draw(){
      resizeCanvasToDisplay();
      const W=canvas.clientWidth; const H=canvas.clientHeight;
      ctx.clearRect(0,0,W,H);
      cellW = W/maze.cols; cellH = H/maze.rows; cellSizePx = Math.min(cellW, cellH);
      document.getElementById('cellSize').textContent = Math.floor(cellSizePx);
      document.getElementById('cellCount').textContent = `${maze.rows*maze.cols} (${maze.rows}×${maze.cols})`;

      ctx.lineWidth = Math.max(1, cellSizePx*0.06);
      ctx.strokeStyle = 'rgba(255,255,255,0.12)';
      // draw walls
      for(let r=0;r<maze.rows;r++){
        for(let c=0;c<maze.cols;c++){
          const cell = maze.cellAt(r,c);
          const x = c*cellW; const y = r*cellH;
          // top
          if(cell.walls[0]) { ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(x+cellW,y); ctx.stroke(); }
          // right
          if(cell.walls[1]) { ctx.beginPath(); ctx.moveTo(x+cellW,y); ctx.lineTo(x+cellW,y+cellH); ctx.stroke(); }
          // bottom
          if(cell.walls[2]) { ctx.beginPath(); ctx.moveTo(x+cellW,y+cellH); ctx.lineTo(x,y+cellH); ctx.stroke(); }
          // left
          if(cell.walls[3]) { ctx.beginPath(); ctx.moveTo(x,y+cellH); ctx.lineTo(x,y); ctx.stroke(); }
        }
      }

      // draw start
      drawCircleCenter(0,0, cellSizePx*0.24, '#4cc0ff');
      // draw exit
      drawCircleCenter(exitCell.r, exitCell.c, cellSizePx*0.24, '#ffd166');

      // draw player
      drawCircleCenter(player.r, player.c, cellSizePx*0.28, '#00d084');
    }

    function drawCircleCenter(r,c,rad,color){
      const x = c*cellW + cellW/2; const y = r*cellH + cellH/2;
      ctx.beginPath(); ctx.fillStyle=color; ctx.arc(x,y,rad,0,Math.PI*2); ctx.fill();
    }

    function canMove(fromR,fromC,dir){
      // dir: 'up' 'right' 'down' 'left'
      const cell = maze.cellAt(fromR,fromC);
      if(!cell) return false;
      const map = {up:0,right:1,down:2,left:3};
      if(cell.walls[map[dir]]) return false; // wall blocking
      // check bounds
      const delta = {up:[-1,0],right:[0,1],down:[1,0],left:[0,-1]}[dir];
      const nr = fromR+delta[0], nc = fromC+delta[1];
      return maze.cellAt(nr,nc) != null;
    }

    function movePlayer(dir){
      if(canMove(player.r,player.c,dir)){
        const delta = {up:[-1,0],right:[0,1],down:[1,0],left:[0,-1]}[dir];
        player.r += delta[0]; player.c += delta[1];
        draw();
        checkWin();
      }
    }

    function checkWin(){
      if(player.r===exitCell.r && player.c===exitCell.c){
        setTimeout(()=>{ alert('¡Has llegado a la salida!'); }, 100);
      }
    }

    // generate maze with chosen rows/cols
    function createAndDraw(rows,cols){
      maze = new Maze(rows,cols);
      maze.generate();
      // reset player and exit
      player={r:0,c:0};
      exitCell = {r: rows-1, c: cols-1};
      draw();
    }

    // UI wiring
    const regenerateBtn = document.getElementById('regenerate');
    regenerateBtn.addEventListener('click', ()=>{
      const rows = parseInt(document.getElementById('rowsRange').value,10);
      const cols = parseInt(document.getElementById('colsRange').value,10);
      createAndDraw(rows,cols);
    });

    document.getElementById('colsRange').addEventListener('input', (e)=>{ document.getElementById('colsVal').textContent = e.target.value; });
    document.getElementById('rowsRange').addEventListener('input', (e)=>{ document.getElementById('rowsVal').textContent = e.target.value; });

    document.getElementById('shuffle-size').addEventListener('click', ()=>{
      // randomize rows/cols within ranges
      const colsEl = document.getElementById('colsRange'); const rowsEl = document.getElementById('rowsRange');
      colsEl.value = Math.floor(Math.random()*(parseInt(colsEl.max)-parseInt(colsEl.min))+parseInt(colsEl.min));
      rowsEl.value = Math.floor(Math.random()*(parseInt(rowsEl.max)-parseInt(rowsEl.min))+parseInt(rowsEl.min));
      document.getElementById('colsVal').textContent = colsEl.value;
      document.getElementById('rowsVal').textContent = rowsEl.value;
      createAndDraw(parseInt(rowsEl.value), parseInt(colsEl.value));
    });

    document.getElementById('resetPlayer').addEventListener('click', ()=>{ player={r:0,c:0}; draw(); });

    window.addEventListener('keydown', (e)=>{
      const k=e.key.toLowerCase();
      if(['arrowup','w'].includes(k) || k==='w') movePlayer('up');
      else if(['arrowdown','s'].includes(k) || k==='s') movePlayer('down');
      else if(['arrowleft','a'].includes(k) || k==='a') movePlayer('left');
      else if(['arrowright','d'].includes(k) || k==='d') movePlayer('right');
    });

    // regenerate on resize to keep things proportional
    let resizeTimer=null;
    window.addEventListener('resize', ()=>{ clearTimeout(resizeTimer); resizeTimer=setTimeout(draw,120); });

    // initial load: read ranges and generate
    document.addEventListener('DOMContentLoaded', ()=>{
      // make canvas aspect ratio friendly
      const cols = parseInt(document.getElementById('colsRange').value,10);
      const rows = parseInt(document.getElementById('rowsRange').value,10);
      document.getElementById('colsVal').textContent = cols;
      document.getElementById('rowsVal').textContent = rows;
      // set a comfortable CSS size for canvas
      canvas.style.height = Math.max(240, Math.min(720, Math.floor(window.innerHeight * 0.65))) + 'px';
      createAndDraw(rows,cols);
    });
