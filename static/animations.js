const submit_button = document.getElementById("submit-button");
const contact_form = document.getElementById("contact-form");

submit_button.addEventListener("click", () => {
    contact_form.submit();
});

const about = document.getElementById("home");
const projects = document.getElementById("projects");
const skills = document.getElementById("skills");
const contact = document.getElementById("contact");

const about_button = document.getElementById("about-menu-button");
const projects_button = document.getElementById("projects-menu-button");
const skills_button = document.getElementById("skills-menu-button");
const contact_button = document.getElementById("contact-menu-button");

about_button.addEventListener("click", () => {
    about.scrollIntoView({ behavior: "smooth" });
});

projects_button.addEventListener("click", () => {
    projects.scrollIntoView({ behavior: "smooth" });
});

skills_button.addEventListener("click", () => {
    skills.scrollIntoView({ behavior: "smooth" });
});

contact_button.addEventListener("click", () => {
    contact.scrollIntoView({ behavior: "smooth" });
});

const about_button_two = document.getElementById("about-menu-button-two");
const projects_button_two = document.getElementById("projects-menu-button-two");
const skills_button_two = document.getElementById("skills-menu-button-two");
const contact_button_two = document.getElementById("contact-menu-button-two");

about_button_two.addEventListener("click", () => {
    about.scrollIntoView({ behavior: "smooth" });
});

projects_button_two.addEventListener("click", () => {
    projects.scrollIntoView({ behavior: "smooth" });
});

skills_button_two.addEventListener("click", () => {
    skills.scrollIntoView({ behavior: "smooth" });
});

contact_button_two.addEventListener("click", () => {
    contact.scrollIntoView({ behavior: "smooth" });
});

navlist = document.getElementById("nav-list");
burger = document.getElementById("menu-burger");

function has_class(element, class_name) {
    return element.classList.contains(class_name);
}

function add_class(element, class_name) {
    element.classList.add(class_name);
}

function remove_class(element, class_name) {
    element.classList.remove(class_name);
}

function show_nav() {
    add_class(navlist, "active");
    remove_class(navlist, "inactive");
}

function hide_nav() {
    add_class(navlist, "inactive");
    remove_class(navlist, "active");
}

function burger_menu_to_x() {
    add_class(burger, "active");
}

function x_to_burger() {
    remove_class(burger, "active");
}

function check_screen_size() {
    var screen_width = window.innerWidth || document.documentElement.clientWidth;
    var breakpoint = 730;
    
    if(has_class(navlist, "active")) {
        hide_nav();
        x_to_burger();
    } else {
        show_nav();
        burger_menu_to_x();
    }
}

burger.addEventListener("click", check_screen_size);

document.addEventListener("click", function(event) {
    if(burger.contains(event.target)) {
        return;
    }
    if(has_class(navlist, "active") && has_class(burger, "active")) {
        hide_nav();
        x_to_burger();
    }
});
