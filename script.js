window.addEventListener("load",()=>setTimeout(()=>document.querySelector(".loader").classList.add("hide"),500));
const progress=document.querySelector(".progress");
window.addEventListener("scroll",()=>{let h=document.documentElement.scrollHeight-innerHeight;progress.style.width=(scrollY/h*100)+"%"});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add("show")}),{threshold:.12});
document.querySelectorAll(".reveal").forEach(x=>io.observe(x));

const header=document.querySelector(".header"),hamb=document.querySelector(".hamb");
hamb.addEventListener("click",()=>header.classList.toggle("open"));
document.querySelectorAll(".nav a").forEach(a=>a.addEventListener("click",()=>header.classList.remove("open")));

const counters=document.querySelectorAll("[data-count]");
const counterIO=new IntersectionObserver(es=>{
 es.forEach(e=>{
  if(!e.isIntersecting||e.target.dataset.done)return;
  e.target.dataset.done="1";let target=+e.target.dataset.count,start=0,duration=1300,startTime=null;
  function tick(t){if(!startTime)startTime=t;let p=Math.min((t-startTime)/duration,1);e.target.textContent=Math.floor((1-Math.pow(1-p,3))*target).toLocaleString();if(p<1)requestAnimationFrame(tick)}
  requestAnimationFrame(tick);
 });
},{threshold:.7});
counters.forEach(x=>counterIO.observe(x));

document.getElementById("demoForm").addEventListener("submit",e=>{
 e.preventDefault();const s=document.getElementById("success");s.style.display="block";s.textContent="✓ Demo request captured. Thank you!";e.target.reset();
});
document.getElementById("year").textContent=new Date().getFullYear();

document.querySelectorAll(".course").forEach(card=>{
 card.addEventListener("mousemove",e=>{let r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;card.style.transform=`perspective(800px) rotateX(${y*-3}deg) rotateY(${x*3}deg) translateY(-8px)`});
 card.addEventListener("mouseleave",()=>card.style.transform="");
});
