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