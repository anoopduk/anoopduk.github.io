// script.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Update the Current Year in the Footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        const currentYear = new Date().getFullYear();
        currentYearSpan.textContent = currentYear;
    }

    // 2. Back to Top Button Functionality
    const upArrow = document.getElementById('up-arrow');

    // Function to Show or Hide the Back to Top Button
    const toggleUpArrow = () => {
        if (window.scrollY > 300) { // Threshold: 300px
            upArrow.classList.add('show');
        } else {
            upArrow.classList.remove('show');
        }
    };

    // Event Listener for Scroll to Toggle the Button Visibility
    window.addEventListener('scroll', toggleUpArrow);

    // Event Listener for Click on the Up Arrow to Scroll to Top Smoothly
    upArrow.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent Default Anchor Behavior
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Smooth Scrolling
        });
    });

    // Optional: Initial Check in Case the User Reloads While Scrolled Down
    toggleUpArrow();
});

