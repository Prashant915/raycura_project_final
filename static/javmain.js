window.onload=git();
function git(){
let btn = document.querySelector(".option");
let opn = document.querySelector(".links");
let cls = document.querySelector(".close");
btn.addEventListener("click", function () {
    opn.classList.toggle("show");
})
cls.addEventListener("click", function () {
    if (opn.classList.contains("show")) {
        opn.classList.remove("show");
    }
})

let pra=document.querySelector(".dev");
let devlop=document.querySelector(".prashant");
pra.addEventListener("mouseover", function(){
    devlop.classList.add("showdev")
})
pra.addEventListener("mouseout", function(){
    devlop.classList.remove("showdev")
})

let nav= document.querySelectorAll(".dropdown1");
let opt=document.querySelector(".y1");
let opt2=document.querySelector(".ppp");
nav.forEach(function(e){
    e.addEventListener("mouseover",function(btn){
        const cl=btn.currentTarget.classList;
        if(cl.contains("ortho")){
            opt.classList.add("showdev")
        }
    })
    e.addEventListener("mouseover",function(btn){
        const cl=btn.currentTarget.classList;
        if(cl.contains("physio")){
            opt2.classList.add("showdev")
        }
    })
    e.addEventListener("mouseout",function(btn){
        const cl=btn.currentTarget.classList;
        if(cl.contains("ortho")){
            opt.classList.remove("showdev")
        }
    })
    e.addEventListener("mouseout",function(btn){
        const cl=btn.currentTarget.classList;
        if(cl.contains("physio")){
            opt2.classList.remove("showdev")
        }
    })
})
}