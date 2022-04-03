// THIS WILL CONTROL OPEN AND CLOSE OF HAMBURGER MENU
// const open = document.querySelector("#open-menu");
// const close = document.querySelector("#close-menu");
const toggleMenu = document.querySelector("#menu-toggle-icon");
const openAside = document.querySelector('#aside');

function toggleFunction () {
  toggleMenu.classList.toggle("activated");
  openAside.classList.toggle("activated");
}

toggleMenu.addEventListener('click', toggleFunction);

// SWITCH THEME AND ADDING TO LOCAL STORAGE
const body = document.body;
const themeToggleBtn = document.querySelector("#theme-toggle-btn");
const currentTheme = localStorage.getItem("currentTheme");

if (currentTheme) {
  body.classList.add("light-theme");
}
themeToggleBtn.addEventListener('click', () => {
  body.classList.toggle("light-theme");

  if (body.classList.contains("light-theme")) {
    localStorage.setItem("currentTheme", "themeActive");
  } else {
    localStorage.removeItem("currentTheme")
  }
})


// THIS IS USED ON EVERY FORM PAGE TO MAKE THE LATITUDE, LONGITUDE AND COORDINATE READONLY

if (document.getElementById("id_coordinates")){
  document.querySelector("#id_longitude").readOnly = true;
  document.querySelector("#id_latitude").readOnly = true;
  document.querySelector("#id_coordinates").readOnly = true;
}

// THIS SCRIPT IS FOR (SPECIFIC SEARCH.HTML) THAT DYNAMICALLY EFFECT THE INPUT BEHAVIOR BASED ON THE 
// "SEARCH TYPE ACTION" 
if (document.getElementById("dynamic")){
  dynamic_input.placeholder = result
if (result == 'Search by Location Name') {
    flag.style.display = 'block'
}

if (result == 'Search by Coordinates') {

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      dynamic_input.value = "Geolocation is not supported by this browser.";
    }
  
  function showPosition(position) {
    dynamic_input.value = position.coords.latitude +
    "," + position.coords.longitude;
  }

  dynamic_input.readOnly = true;
  document.getElementById("inp_cord").style.display = 'inline';
}
}




// THIS SCRIPT IS FOR (TREE DETAILS.HTML) IT IS THE ONE THAT POPS OUT THE IFRAME WHEN USER WANTS 
// TO CHECK THE PICTURE OF WHERE THE TREES ARE

function displayIframe(val) {
  var locationTitle = val.innerText
  document.getElementById("pic_cont").style.display = 'block'
  document.getElementById("picture_title").innerText = locationTitle
  
  if (window.innerWidth > 800) {
      document.getElementById("detail-container").style.display = 'grid'
  }
}



// THIS SCRIPT IS FOR (UPLOAD FORM.HTML) IT IS USED TO FETCH AND POULATE THE COORDINATE INPUT
// WHEN USER WANTS TO UPLOAD

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(showPosition);
} else {
  x.value = "Geolocation is not supported by this browser.";
}

function showPosition(position) {
x.value = position.coords.latitude +
"," + position.coords.longitude;
y.value = position.coords.latitude;
z.value = position.coords.longitude;
}

