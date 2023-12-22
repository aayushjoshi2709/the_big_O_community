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

const swith_theme = (e)=>{
  element = document.getElementById("themechanger")
  if(element.innerHTML ==="Auto"){
    set_theme("theme-light")
    element.innerHTML = "Light"
  }else if(element.innerHTML === "Light"){
    set_theme("theme-dark")
    element.innerHTML = "Dark"
  }else{
    detect_and_set_theme()
    element.innerHTML = "Auto"
  }
}

function set_theme(theme_name) {
  document.documentElement.className = theme_name;
}

function detect_and_set_theme(){
  const check_dark_theme = window.matchMedia("(prefers-color-scheme: dark)");
  if (check_dark_theme.matches) {
    set_theme("theme-dark")
  } else {
    set_theme("theme-light")
  }
}

detect_and_set_theme()