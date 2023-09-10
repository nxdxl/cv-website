// const list_items = document.getElementsByClassName("list-item");
const content_wrapper = document.getElementById("home");
const heading_container = document.getElementById("heading-container");
const rectangle_top_right = document.getElementById("rectangle-top-right");
const rectangle_bottom_left = document.getElementById("rectangle-bottom-left");
const content = document.getElementById("content");
const menu = document.getElementById("menu-container");

const contact = document.getElementById("contact-item");

const list_items = document.querySelectorAll(".list-item");

function hasClass(element, clsName) {
        return(' ' + element.className + ' ').indexOf(' ' + clsName + ' ') > -1;
}

function removeAnimation() {
    content_wrapper.classList.remove("animate-main");
    rectangle_top_right.classList.remove("animate-top-square");
    rectangle_bottom_left.classList.remove("animate-bottom-square");
    content.classList.remove("vanish");
    menu.classList.remove("vanish");
    heading_container.classList.remove("vanish");
    heading_container.classList.add("introduce");
    content.classList.add("introduce");
    menu.classList.add("introduce");
}

function addAnimation() {
    content_wrapper.classList.add("animate-main");
    rectangle_top_right.classList.add("animate-top-square");
    rectangle_bottom_left.classList.add("animate-bottom-square");
    if(hasClass(menu, "introduce")) {
        content.classList.remove("introduce");
        menu.classList.remove("introduce");
        heading_container.classList.remove("introduce");
    }
    setTimeout(removeAnimation, 500);
}

list_items.forEach(item => {
    item.addEventListener("click", function() {
        content.classList.add("vanish");
        heading_container.classList.add("vanish");
        menu.classList.add("vanish");
        setTimeout(addAnimation, 500);
    });
});
