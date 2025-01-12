document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("#header-nav a");
    const currentURL = window.location.pathname;

    links.forEach(link => {
        if (link.getAttribute("href") === currentURL) {
            link.classList.add("current");
        }
    });
});
