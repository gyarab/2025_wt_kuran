const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game states and elements
let bird = {
    x: 50,
    y: 150,
    width: 30,
    height: 30,
    gravity: 0.25,
    velocity: 0,
    jump: -5,
    image: new Image()
};

const pipe = {
    width: 50,
    gap: 100,
    velocity: 2
};

let pipes = [];
let score = 0;
let gameStarted = false;
let gameOver = false;

// Load bird image
bird.image.src = '../logo.png'; // Reference to logo.png in the parent directory
bird.image.onload = startGame; // Start game after image loads

// Game screens
const startScreen = document.getElementById('start-screen');
const gameOverScreen = document.getElementById('game-over-screen');
const startButton = document.getElementById('startButton');
const restartButton = document.getElementById('restartButton');
const finalScoreSpan = document.getElementById('finalScore');

// Event Listeners
document.addEventListener('keydown', handleInput);
document.addEventListener('click', handleInput);
startButton.addEventListener('click', startGame);
restartButton.addEventListener('click', resetGame);

function handleInput(e) {
    if (gameOver) return;

    if (e.code === 'Space' || e.type === 'click') {
        if (!gameStarted) {
            startGame();
        }
        bird.velocity = bird.jump;
    }
}

function startGame() {
    startScreen.style.display = 'none';
    gameOverScreen.style.display = 'none';
    if (!gameStarted) { // Only reset if truly starting new game, not just flapping
        resetGame();
    }
    gameStarted = true;
    gameOver = false;
    loop();
}

function resetGame() {
    bird.y = 150;
    bird.velocity = 0;
    pipes = [];
    score = 0;
    gameOver = false;
    // Don't set gameStarted to false here, as startGame() will do it
}


// Game Loop
function loop() {
    if (gameOver) return;

    update();
    draw();

    requestAnimationFrame(loop);
}

function update() {
    // Bird physics
    bird.velocity += bird.gravity;
    bird.y += bird.velocity;

    // Ground collision
    if (bird.y + bird.height > canvas.height) {
        bird.y = canvas.height - bird.height;
        endGame();
    }
    if (bird.y < 0) { // Ceiling collision
        bird.y = 0;
        bird.velocity = 0;
    }


    // Pipe generation
    if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
        const pipeHeight = Math.floor(Math.random() * (canvas.height - 300)) + 50;
        pipes.push({
            x: canvas.width,
            y: 0, // Top pipe starting at the top
            height: pipeHeight,
            passed: false
        });
        pipes.push({
            x: canvas.width,
            y: pipeHeight + pipe.gap, // Bottom pipe starts after the gap
            height: canvas.height - pipeHeight - pipe.gap,
            passed: false
        });
    }

    // Pipe movement and collision
    for (let i = 0; i < pipes.length; i += 2) { // Process pipes in pairs
        const p1 = pipes[i]; // Top pipe
        const p2 = pipes[i + 1]; // Bottom pipe

        p1.x -= pipe.velocity;
        p2.x -= pipe.velocity;

        // Collision detection
        if (
            bird.x < p1.x + pipe.width &&
            bird.x + bird.width > p1.x &&
            (bird.y < p1.height || bird.y + bird.height > p2.y)
        ) {
            endGame();
        }

        // Score
        if (p1.x + pipe.width < bird.x && !p1.passed) {
            score++;
            p1.passed = true;
            p2.passed = true; // Mark both pipes in the pair as passed
        }
    }

    // Remove off-screen pipes
    if (pipes.length > 0 && pipes[0].x + pipe.width < 0) {
        pipes.shift(); // Remove top pipe
        pipes.shift(); // Remove bottom pipe
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas

    // Draw pipes
    for (let i = 0; i < pipes.length; i++) {
        const p = pipes[i];
        ctx.fillStyle = '#4e811eff'; // Green pipe color
        ctx.fillRect(p.x, p.y, pipe.width, p.height);
    }

    // Draw bird
    ctx.drawImage(bird.image, bird.x, bird.y, bird.width, bird.height);

    // Draw score
    ctx.fillStyle = '#000';
    ctx.font = '20px Arial';
    ctx.fillText('Score: ' + score, 10, 30);
}

function endGame() {
    gameOver = true;
    gameStarted = false;
    finalScoreSpan.textContent = score;
    gameOverScreen.style.display = 'flex';
}

// Initial state (show start screen)
startScreen.style.display = 'flex';
