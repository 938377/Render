<!-- Paste this full updated HTML in your index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Future Toppers</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
  <style>
  #noticeSection {
  max-width: 800px;
  margin: 1rem auto 2rem;
  background: rgba(0, 240, 255, 0.1);
  padding: 1.5rem 2rem;
  border-left: 4px solid #00f0ff;
  border-radius: 16px;
  box-shadow: 0 0 12px #00f0ff44;
  backdrop-filter: blur(10px);
  color: white;
}

#noticeSection h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #00f0ff;
  text-shadow: 0 0 8px #00f0ff88;
}

#noticeSection ul {
  list-style-type: none;
  padding-left: 0;
}

#noticeSection li {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Poppins', sans-serif;
      background: #0f0f1a;
      overflow-x: hidden;
      color: white;
    }

    canvas#bg {
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      z-index: -1;
    }

    header {
      text-align: center;
      padding: 2rem 1rem 1rem;
    }

    header h1 {
      font-size: 2.2rem;
      color: #00f0ff;
      text-shadow: 0 0 15px #00f0ff55;
    }

    #searchInput {
      margin-top: 1rem;
      padding: 0.6rem 1rem;
      font-size: 1rem;
      border-radius: 12px;
      border: none;
      background: rgba(255,255,255,0.1);
      color: white;
      outline: none;
      box-shadow: 0 0 12px #00f0ff33;
    }

    .grid {
      max-width: 1100px;
      margin: 2rem auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      padding: 0 1rem 2rem;
    }

    .card {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 20px;
      padding: 2rem;
      text-align: center;
      backdrop-filter: blur(14px);
      color: white;
      font-weight: 600;
      text-decoration: none;
      box-shadow: 0 0 15px rgba(0,255,255,0.1);
      transition: all 0.4s ease;
    }

    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 25px #00f0ffcc;
    }

    .card span {
      display: block;
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
    }

    footer {
      text-align: center;
      padding: 2rem;
      font-size: 0.9rem;
      color: #aaa;
    }
  </style>
</head>
<body>

  <!-- Glowing background -->
  <canvas id="bg"></canvas>

  <header>
    <h1>📚 Future Toppers</h1>
    <input type="text" id="searchInput" placeholder="Search subject...">
<section id="noticeSection">
  <h2>📢 Notice</h2>
  <ul>
    <li><strong>Today's Lecture:</strong></li>
    <li>🧪 Science – 5 PM</li>
    <li>🌍 SST – 8 PM</li>
  </ul>
</section>
  </header>

  <div class="grid" id="subjectGrid">
    <a class="card" href="https://futuretoppersmaths.netlify.app/"><span>➗</span>Maths</a>
    <a class="card" href="https://futuretoppersscience89.netlify.app/"><span>🧪</span>Science</a>
    <a class="card" href="https://futuretopperssst68.netlify.app/"><span>🌍</span>SST</a>
    <a class="card" href="https://futuretoppershindi.netlify.app/"><span>📝</span>Hindi</a>
    <a class="card" href="https://futuretoppersenglish89.netlify.app/"><span>📘</span>English</a>
    <a class="card" href="https://futureyopperssanskrit.netlify.app/"><span>📜</span>Sanskrit</a>
    <a class="card" href="https://futuretoppersitai89.netlify.app/"><span>💻</span>AI / IT</a>
    <a class="card" href="https://futuretoppersdppvault.netlify.app/"><span>🔐</span>DPP Vault</a>
  </div>

  <footer>
    Made with 💙 by Future Toppers
  </footer>

  <script>
    const input = document.getElementById('searchInput');
    const cards = document.querySelectorAll('.card');
    input.addEventListener('input', () => {
      const val = input.value.toLowerCase();
      cards.forEach(card => {
        const text = card.innerText.toLowerCase();
        card.style.display = text.includes(val) ? 'block' : 'none';
      });
    });
  </script>

  <!-- Particle background animation -->
  <script>
    const canvas = document.getElementById("bg");
    const ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];
    for (let i = 0; i < 100; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2 + 1,
        dx: (Math.random() - 0.5) * 0.8,
        dy: (Math.random() - 0.5) * 0.8
      });
    }

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let p of particles) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = "#00f0ff88";
        ctx.fill();
        p.x += p.dx;
        p.y += p.dy;
        if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
      }
      requestAnimationFrame(animate);
    }

    animate();

    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    });
  </script>

</body>
</html>
