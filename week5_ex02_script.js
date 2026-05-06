/* ==================== */
/* Gallery Filter Script */
/* ==================== */

document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const galleryCards = document.querySelectorAll('.gallery-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');

            // Update active button state
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
            });
            this.classList.add('active');

            // Filter gallery cards
            galleryCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');

                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.classList.remove('hidden');
                    card.style.animation = 'cardFadeIn 0.4s ease-out';
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
});
