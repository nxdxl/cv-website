const content_wrapper = document.getElementById("home");
const heading_container = document.getElementById("heading-container");
const rectangle_top_right = document.getElementById("rectangle-top-right");
const rectangle_bottom_left = document.getElementById("rectangle-bottom-left");
const content = document.getElementById("content");
const menu_container = document.getElementById("menu-container");
const list_items = document.querySelectorAll(".list-item");
const triangle = document.getElementById("bottom-right-triangle");
const menu = document.getElementById("menu-list");
const menu_button = document.getElementById("open-menu");
const phone_width = 561;

function toggle_phone_menu() {
    if(document.body.clientWidth > phone_width) {
        return;
    }
    if(hasClass(menu, "display-on")) {
        console.log("print");
        menu.classList.remove("display-on");
        menu.classList.add("display-off");
    } else {
        menu.classList.add("display-on");
        menu.classList.remove("display-off");
    }
}

function hasClass(element, clsName) {
        return(' ' + element.className + ' ').indexOf(' ' + clsName + ' ') > -1;
}

function removeAnimation() {
    content_wrapper.classList.remove("animate-main");
    rectangle_top_right.classList.remove("animate-top-square");
    rectangle_bottom_left.classList.remove("animate-bottom-square");
    content.classList.remove("vanish");
    menu_container.classList.remove("vanish");
    heading_container.classList.remove("vanish");
    heading_container.classList.add("introduce");
    content.classList.add("introduce");
    toggle_phone_menu();
    menu_container.classList.add("introduce");
    triangle.classList.remove("rotate");
}

function addAnimation() {
    console.log(document.body.clientWidth);
    if(document.body.clientWidth < phone_width) {
        setTimeout(removeAnimation, 500);
        return;
    }
    content_wrapper.classList.add("animate-main");
    rectangle_top_right.classList.add("animate-top-square");
    rectangle_bottom_left.classList.add("animate-bottom-square");
    if(hasClass(menu_container, "introduce")) {
        content.classList.remove("introduce");
        menu_container.classList.remove("introduce");
        heading_container.classList.remove("introduce");
    }
    setTimeout(removeAnimation, 500);
}

list_items.forEach(item => {
    item.addEventListener("click", function() {
        content.classList.add("vanish");
        heading_container.classList.add("vanish");
        menu_container.classList.add("vanish");
        triangle.classList.add("rotate");
        setTimeout(addAnimation, 500);
    });
});

menu_button.addEventListener("click", () => {toggle_phone_menu()});



