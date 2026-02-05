document.addEventListener('DOMContentLoaded', function () {
    const winterCampBtn = document.getElementById('zimni-tabor-btn');
    const summerCampBtn = document.getElementById('letni-tabor-btn');
    const winterCamp = document.getElementById('zimni-tabor');
    const summerCamp = document.getElementById('letni-tabor');

    // Function to handle the fade-in effect
    function showContent(element) {
        element.style.display = 'block';
        // Trigger reflow
        element.getBoundingClientRect();
        element.classList.add('fade-in');
    }

    function hideContent(element) {
        element.style.display = 'none';
        element.classList.remove('fade-in');
    }

    if (winterCampBtn && summerCampBtn && winterCamp && summerCamp) {
        winterCampBtn.addEventListener('click', () => {
            hideContent(summerCamp);
            showContent(winterCamp);
            winterCampBtn.classList.add('active');
            summerCampBtn.classList.remove('active');
        });

        summerCampBtn.addEventListener('click', () => {
            hideContent(winterCamp);
            showContent(summerCamp);
            summerCampBtn.classList.add('active');
            winterCampBtn.classList.remove('active');
        });

        // Initially show winter camp with fade-in
        showContent(winterCamp);
    }
});