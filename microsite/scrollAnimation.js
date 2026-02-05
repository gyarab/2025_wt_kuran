document.addEventListener('DOMContentLoaded', () => {
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        let delay = 0;
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Apply the animation with a staggered delay
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, delay);
                delay += 150; // Stagger subsequent animations
                
                // Stop observing the element once it's visible
                observer.unobserve(entry.target);
            }
        });
    }, options);

    // Select all elements to animate
    const targets = document.querySelectorAll('main > .container > section, main > .container > article, .grid-2 > *, .cards-grid > .card, .gallery img');
    
    // Counter for alternating full-width elements
    let fullWidthCounter = 0;

    targets.forEach(target => {
        target.classList.add('animate-on-scroll');
        const parentIsGrid = target.parentElement.classList.contains('grid-2');
        
        if (parentIsGrid) {
            // Check if it's the first or second child in the grid layout
            if (target === target.parentElement.firstElementChild) {
                target.classList.add('fly-in-left');
            } else {
                target.classList.add('fly-in-right');
            }
        } else {
            // Alternate for full-width elements
            if (fullWidthCounter % 2 === 0) {
                target.classList.add('fly-in-left');
            } else {
                target.classList.add('fly-in-right');
            }
            fullWidthCounter++;
        }
        
        observer.observe(target);
    });
});
