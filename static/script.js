document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('phish-form');
    const submitBtn = document.getElementById('submit-btn');
    const urlInput = document.getElementById('url-input');

    if (form) {
        form.addEventListener('submit', (e) => {
            // Change button state
            submitBtn.disabled = true;
            submitBtn.textContent = 'Analyzing Neural Patterns...';
            submitBtn.style.opacity = '0.7';
            
            // Subtle pulse animation on input
            urlInput.style.borderColor = 'var(--secondary)';
        });
    }

    // Auto-focus input on load
    if (urlInput) {
        urlInput.focus();
    }

    // Smooth entry for results if they exist
    const results = document.getElementById('results');
    if (results) {
        results.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});
