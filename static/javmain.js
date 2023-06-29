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
  