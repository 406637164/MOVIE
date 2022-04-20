let pic = [
  "https://picsum.photos/id/1/300/200",
  "https://picsum.photos/id/2/300/400",
  "https://picsum.photos/id/3/100/150",
  "https://picsum.photos/id/4/200/300",
  "https://picsum.photos/id/5/300/200",
];
let index = 0;

let close = document.querySelector(".close");
let ad = document.querySelector(".ad");
let img = document.querySelector("img");
let btn_close = document.querySelector(".close");
let control = document.querySelector(".control");
let picShowDom = [ad, control];

let ad_mouseover = () => (close.style.opacity = 1);
let ad_mouseout = () => (close.style.opacity = 0);

ad.addEventListener("mouseover", ad_mouseover);
ad.addEventListener("mouseout", ad_mouseout);

btn_close.addEventListener("click", close_Handler);
control.addEventListener("click", click_ct_Hanler);

function close_Handler(e) {
  // 讓ad / control消失
  // ad.style.display = 'none';
  // control.style.display = 'none';
  picShowDom.forEach((dom) => (dom.style.display = "none"));
}

function click_ct_Hanler(e) {
  if (e.target.classList.contains("ct_left") && index > 0) {
    console.log("ct_left");
    index -= 1;
  }
  // console.log(e.target.classList.contains('ct_left'));

  if (e.target.classList.contains("ct_right") && index < pic.length - 1) {
    console.log("ct_right");
    index += 1;
  }

  console.log(index);
  img.src = pic[index];
}
