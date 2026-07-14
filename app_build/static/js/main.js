// Core AeroAutomate Interactions

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Navigation Menu Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navMenu = document.getElementById('navMenu');

    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const isOpen = navMenu.classList.contains('active');
            mobileMenuBtn.innerHTML = isOpen ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
        });

        // Close mobile menu when a nav link is clicked
        const navLinks = document.querySelectorAll('.nav-link, .nav-cta');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fa-solid fa-bars"></i>';
            });
        });
    }

    // 2. Contact Form AJAX Submission
    const contactForm = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const formAlert = document.getElementById('formAlert');

    if (contactForm && submitBtn && formAlert) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Clear alerts
            formAlert.className = 'form-alert';
            formAlert.textContent = '';
            formAlert.style.display = 'none';

            // Gather inputs
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Client-side validations
            if (!name || !email || !message) {
                showAlert('All fields are required.', 'error');
                return;
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                showAlert('Please enter a valid email address.', 'error');
                return;
            }

            // Set loading state
            setLoading(true);

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, email, message })
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    showAlert(result.message, 'success');
                    contactForm.reset();
                } else {
                    showAlert(result.message || 'An error occurred. Please try again.', 'error');
                }
            } catch (error) {
                console.error('Submission error:', error);
                showAlert('Failed to connect to the server. Please check your network and try again.', 'error');
            } finally {
                setLoading(false);
            }
        });
    }

    // Helper to render form status alerts
    function showAlert(text, type) {
        formAlert.textContent = text;
        formAlert.className = `form-alert ${type}`;
        formAlert.style.display = 'block';
    }

    // Helper to set button loading states
    function setLoading(isLoading) {
        if (isLoading) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Sending Request...</span> <i class="fa-solid fa-spinner fa-spin btn-icon"></i>';
        } else {
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<span>Submit Request</span> <i class="fa-solid fa-paper-plane btn-icon"></i>';
        }
    }
});
