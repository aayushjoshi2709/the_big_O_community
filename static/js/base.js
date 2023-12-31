let header_links_container = document.getElementsByClassName("header-links-container")[0]
function toggle_header_menu(){
    if(header_links_container.style.display === 'none')
      header_links_container.style.display = 'block'
    else
      header_links_container.style.display = 'none'
}
header_links_container.addEventListener('click',()=>{
  if(window.screen.width <= 1150)
    toggle_header_menu()
})

function set_theme(theme_name) {
  document.documentElement.className = theme_name;
}

let theme = "Auto";
const switch_theme = (e)=>{
  let element = document.getElementById("themechanger")
  if(theme ==="Auto"){
    console.log("here")
    set_theme("theme-light")
    element.innerHTML = `<i class="fa-solid fa-sun"></i>`
    theme = "Light"
  }else if(theme === "Light"){
    set_theme("theme-dark")
    element.innerHTML = `<i class="fa-solid fa-moon"></i>`
    theme= "Dark";
  }else{
    detect_and_set_theme()
    element.innerHTML = `<i class="fa-solid fa-moon">
    <p>Auto</p>
  </i>`
    theme="Auto"
  }
}

function detect_and_set_theme(){
  const check_dark_theme = window.matchMedia("(prefers-color-scheme: dark)");
  if (check_dark_theme.matches) {
    set_theme("theme-dark")
  } else {
    set_theme("theme-light")
  }
}
window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
  if(theme === "Auto")
	detect_and_set_theme()
})
detect_and_set_theme()