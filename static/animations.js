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

