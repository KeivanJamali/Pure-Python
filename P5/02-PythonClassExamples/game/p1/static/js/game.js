/* Game Enhancements: modal, confetti, animated progress */
(function(){
  const modal = document.getElementById('winnerModal');
  const titleEl = modal?.querySelector('.modal-title');
  const bodyEl = modal?.querySelector('.modal-body');

  function showWinner(title, body){
    if(!modal) return;
    titleEl.textContent = title || 'Winner';
    bodyEl.textContent = body || 'Match completed!';
    modal.classList.remove('hidden');
    launchConfetti(120);
  }
  function hideModal(){ modal?.classList.add('hidden'); }
  modal?.addEventListener('click', e=>{ if(e.target === modal || e.target.hasAttribute('data-close')) hideModal(); });
  document.addEventListener('keydown', e=>{ if(e.key==='Escape') hideModal(); });

  // Inject winner popup if template variable exists
  const winnerPopup = window.__winnerPopup;
  if(winnerPopup){
    setTimeout(()=> showWinner('🏆 ' + winnerPopup + ' Wins!', 'First to 3 points achieved. Play again?'), 380);
  }

  // Confetti
  function launchConfetti(count=80){
    const tpl = document.getElementById('confettiPiece');
    if(!tpl) return;
    for(let i=0;i<count;i++){
      const node = tpl.content.firstElementChild.cloneNode(true);
      const delay = (Math.random()*40).toFixed(2)+'ms';
      const left = (Math.random()*100).toFixed(2)+'%';
      const hue = Math.floor(Math.random()*360);
      const size = 8 + Math.random()*18;
      node.style.left = left;
      node.style.animationDelay = delay;
      node.style.background = `linear-gradient(135deg,hsl(${hue} 90% 65%),hsl(${(hue+40)%360} 90% 55%))`;
      node.style.width = node.style.height = size+'px';
      node.style.setProperty('--x-move', (Math.random()*180-90)+'px');
      document.body.appendChild(node);
      setTimeout(()=> node.remove(), 3400);
    }
  }

  // Animate scoreboard progress (first to 3)
  const scoreBoxes = document.querySelectorAll('.score-box');
  if(scoreBoxes.length){
    scoreBoxes.forEach(box=>{
      const score = parseInt(box.querySelector('.score')?.textContent||'0',10);
      const bar = document.createElement('div');
      bar.className='mini-progress';
      const inner = document.createElement('span');
      inner.style.setProperty('--pct', Math.min(score/3*100,100)+'%');
      bar.appendChild(inner);
      box.appendChild(bar);
      requestAnimationFrame(()=> inner.style.width = inner.style.getPropertyValue('--pct')); // trigger anim
    });
  }

  /* Theme toggle */
  const root = document.documentElement;
  const themeBtn = document.getElementById('themeToggle');
  const THEME_KEY='sps_theme';
  function setTheme(mode){
    if(mode==='light'){ root.classList.add('light-theme'); themeBtn&& (themeBtn.textContent='🌞'); }
    else { root.classList.remove('light-theme'); themeBtn&& (themeBtn.textContent='🌗'); }
    localStorage.setItem(THEME_KEY, mode);
  }
  setTheme(localStorage.getItem(THEME_KEY)||'dark');
  themeBtn?.addEventListener('click',()=>{
    const next = root.classList.contains('light-theme') ? 'dark':'light';
    setTheme(next);
  });

  /* Sounds */
  const soundBtn = document.getElementById('soundToggle');
  const SOUND_KEY='sps_sound';
  const ctx = window.AudioContext ? new AudioContext() : null;
  let soundEnabled = (localStorage.getItem(SOUND_KEY)||'on')==='on';
  function tone(freq=440, dur=0.18, type='sine', vol=.25){
    if(!ctx || !soundEnabled) return; const osc = ctx.createOscillator(); const gain=ctx.createGain(); osc.type=type; osc.frequency.value=freq; gain.gain.value=vol; osc.connect(gain).connect(ctx.destination); osc.start(); osc.stop(ctx.currentTime+dur); }
  function chord(base){ [0,4,7].forEach((s,i)=> tone(base*Math.pow(2,s/12), 0.22- i*0.04, 'sine', .18)); }
  function playWin(){ chord(440); }
  function playLose(){ tone(180,.25,'sawtooth',.22); }
  function playDraw(){ tone(320,.12,'triangle',.2); }
  function playClick(){ tone(520,.07,'square',.12); }
  function updateSoundUI(){ soundBtn && (soundBtn.textContent = soundEnabled ? '🔊':'🔈'); }
  updateSoundUI();
  soundBtn?.addEventListener('click',()=>{ soundEnabled=!soundEnabled; localStorage.setItem(SOUND_KEY, soundEnabled?'on':'off'); updateSoundUI(); playClick(); });
  document.addEventListener('pointerdown',e=>{ if(e.target.closest('button')) playClick(); });

  // Round result sound hook
  if(window.__roundResult){
    if(window.__roundResult==='win') playWin(); else if(window.__roundResult==='lose') playLose(); else if(window.__roundResult==='draw') playDraw();
  }

  /* Ripple effect */
  document.addEventListener('click', e=>{
    const btn = e.target.closest('.super-btn, .choice-btn');
    if(!btn) return;
    btn.classList.add('ripple-container');
    const wave = document.createElement('span');
    wave.className='ripple-wave';
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left; const y = e.clientY - rect.top;
    wave.style.left = (x - 10)+'px'; wave.style.top = (y - 10)+'px';
    btn.appendChild(wave);
    setTimeout(()=> wave.remove(), 700);
  });
})();
