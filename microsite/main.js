// main.js

// --- Globals for pagination ---
let planAkciPage = 0;
const planAkciPageSize = 10;
let taboryPage = 0;
const taboryPageSize = 8;


// --- Rendering Functions ---

function renderPlanAkciTable() {
    if (typeof planAkciData === 'undefined') return;
    const tbody = document.getElementById('plan-akci-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';
    const start = planAkciPage * planAkciPageSize;
    const end = Math.min(start + planAkciPageSize, planAkciData.length);

    for (let i = start; i < end; i++) {
        const row = planAkciData[i];
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.nazev}</td>
            <td>${row.datum}</td>
            <td>${row.vedouci}</td>
        `;
        tbody.appendChild(tr);
    }
    document.getElementById('plan-akci-prev').disabled = planAkciPage === 0;
    document.getElementById('plan-akci-next').disabled = end >= planAkciData.length;
}

function renderUpcomingEvents() {
    if (typeof planAkciData === 'undefined') return;
    const tbody = document.getElementById('upcoming-events-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';
    const upcomingCount = Math.min(3, planAkciData.length);

    for (let i = 0; i < upcomingCount; i++) {
        const row = planAkciData[i];
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.nazev}</td>
            <td>${row.datum}</td>
            <td>${row.vedouci}</td>
        `;
        tbody.appendChild(tr);
    }
}

function renderTaboryTable() {
    if (typeof taboryData === 'undefined') return;
    const tbody = document.getElementById('tabory-tbody');
    if (!tbody) return;

    tbody.innerHTML = '';
    const start = taboryPage * taboryPageSize;
    const end = Math.min(start + taboryPageSize, taboryData.length);

    // Actual data rows
    for (let i = start; i < end; i++) {
        const t = taboryData[i];
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${t.rok}</td><td>${t.misto}</td><td>${t.tema}</td>`;
        tbody.appendChild(tr);
    }

    // Fill with empty rows up to taboryPageSize
    for (let i = end; i < start + taboryPageSize; i++) {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>&nbsp;</td><td></td><td></td>`;
        tbody.appendChild(tr);
    }

    // Disable/enable buttons
    document.getElementById('tabory-prev').disabled = taboryPage === 0;
    document.getElementById('tabory-next').disabled = end >= taboryData.length;
}


// --- Pagination Functions exposed to global scope ---

window.planAkciPrev = function() {
    if (planAkciPage > 0) {
        planAkciPage--;
        renderPlanAkciTable();
    }
}

window.planAkciNext = function() {
    if ((planAkciPage + 1) * planAkciPageSize < planAkciData.length) {
        planAkciPage++;
        renderPlanAkciTable();
    }
}

window.taboryPrev = function() {
    if (taboryPage > 0) {
        taboryPage--;
        renderTaboryTable();
    }
}

window.taboryNext = function() {
    if ((taboryPage + 1) * taboryPageSize < taboryData.length) {
        taboryPage++;
        renderTaboryTable();
    }
}


// --- DOMContentLoaded listener to run initial scripts ---

document.addEventListener('DOMContentLoaded', () => {
    // Initial rendering of tables
    renderPlanAkciTable();
    renderUpcomingEvents();
    renderTaboryTable();

    // Lightbox for photo gallery
    const galleryModal = document.getElementById('galleryModal');
    if (galleryModal) {
        galleryModal.addEventListener('show.bs.modal', event => {
            const button = event.relatedTarget; // Button that triggered the modal
            const imageIndex = button.getAttribute('data-bs-slide-to');
            const galleryCarousel = document.getElementById('galleryCarousel');
            if(galleryCarousel) {
                const carousel = new bootstrap.Carousel(galleryCarousel);
                carousel.to(parseInt(imageIndex));
            }
        });
    }

    // Contact Form Submission (Frontend only for prototype)
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // In a real application, you would collect form data and send it to a backend.
            const formData = {
                name: document.getElementById('contactName').value,
                email: document.getElementById('contactEmail').value,
                subject: document.getElementById('contactSubject').value,
                message: document.getElementById('contactMessage').value
            };

            console.log('Form Data:', formData);

            // Placeholder for backend submission
            alert('Děkujeme za zprávu! Toto je pouze prototyp formuláře a zpráva nebyla odeslána. Pro plnou funkčnost je potřeba implementovat backend.');

            // Optionally, clear the form after "submission"
            contactForm.reset();
        });
    }
});

// --- Footer map initialization (Leaflet + Nominatim geocoding) ---
document.addEventListener('DOMContentLoaded', () => {
    const mapEl = document.getElementById('footer-map');
    const address = 'Nad Panenskou 5, Praha 6';
    if (mapEl && typeof L !== 'undefined') {
        // Initial map (fallback to Prague-ish view until geocoded)
        const map = L.map('footer-map', { scrollWheelZoom: false }).setView([50.091, 14.398], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Try geocoding the address via Nominatim
        fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(address))
            .then(response => response.json())
            .then(results => {
                if (results && results.length > 0) {
                    const best = results[0];
                    const lat = parseFloat(best.lat);
                    const lon = parseFloat(best.lon);
                    map.setView([lat, lon], 17);
                    const marker = L.marker([lat, lon]).addTo(map);
                    marker.bindPopup(`<strong>Klubovna</strong><br>${address}<br><a href="https://www.openstreetmap.org/?mlat=${lat}&mlon=${lon}#map=18/${lat}/${lon}" target="_blank" rel="noopener">Otevřít v OSM</a>`);
                } else {
                    // No results: place a marker near default view
                    L.marker([50.091, 14.398]).addTo(map).bindPopup(`<strong>Klubovna (přibližně)</strong><br>${address}`);
                }
            })
            .catch(err => {
                console.warn('Geocoding failed', err);
                L.marker([50.091, 14.398]).addTo(map).bindPopup(`<strong>Klubovna (přibližně)</strong><br>${address}`);
            });
    }
});
