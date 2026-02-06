// Struktura PDF souborů podle roku
const typkoPdfs = {
    2003: [
        'Typko200.pdf', 'Typko201.pdf', 'Typko202.pdf', 'Typko203.pdf',
        'Typko204.pdf', 'Typko205.pdf', 'Typko206.pdf', 'Typko207.pdf'
    ],
    2004: [
        'Typko208.pdf', 'Typko209.pdf', 'Typko210.pdf', 'Typko211.pdf',
        'Typko212.pdf', 'Typko213.pdf', 'Typko214.pdf', 'Typko215.pdf',
        'Typko216.pdf', 'Typko217.pdf'
    ],
    2005: [
        'Typko218.pdf', 'Typko219.pdf', 'Typko220.pdf', 'Typko221.pdf',
        'Typko222.pdf', 'Typko223.pdf', 'Typko224.pdf', 'Typko226.pdf',
        'Typko227.pdf', 'Typko228.pdf', 'Typko229.pdf'
    ],
    2006: [
        'Typko230.pdf', 'Typko231.pdf', 'Typko232.pdf', 'Typko233.pdf',
        'Typko234.pdf', 'Typko235.pdf', 'Typko236.pdf', 'Typko237.pdf',
        'Typko238.pdf', 'Typko239.pdf', 'Typko240.pdf'
    ],
    2007: [
        'Typko241.pdf', 'Typko242.pdf', 'Typko243.pdf', 'Typko244.pdf',
        'Typko247.pdf', 'Typko248.pdf', 'Typko249.pdf', 'Typko250.pdf',
        'Typko251.pdf'
    ],
    2008: [
        'Typko252.pdf', 'Typko253.pdf', 'Typko254.pdf', 'Typko255.pdf',
        'Typko256.pdf', 'Typko257.pdf', 'Typko258.pdf', 'Typko259.pdf',
        'Typko260.pdf', 'Typko261.pdf', 'Typko262.pdf'
    ],
    2009: [
        'Typko263.pdf', 'Typko264.pdf', 'Typko265.pdf', 'Typko266.pdf',
        'Typko267.pdf', 'Typko268.pdf', 'Typko269.pdf', 'Typko271.pdf',
        'Typko272.pdf', 'Typko273.pdf'
    ],
    2010: [
        'Typko274.pdf', 'Typko275.pdf', 'Typko276.pdf', 'Typko277.pdf',
        'Typko278.pdf', 'Typko279.pdf', 'Typko280.pdf', 'Typko281.pdf'
    ],
    2011: [
        'Typko282.pdf', 'Typko283.pdf'
    ]
};

function initTypkoArchive() {
    const archiveContainer = document.getElementById('typko-archive');
    
    if (!archiveContainer) return;
    
    // Seřadit roky vzestupně
    const years = Object.keys(typkoPdfs)
        .map(Number)
        .sort((a, b) => a - b);
    
    // Vytvořit HTML obsah
    let html = '';
    
    years.forEach(year => {
        const pdfs = typkoPdfs[year];
        
        html += `<article class="typko-year">
            <h3>${year}</h3>
            <div class="pdf-grid">`;
        
        pdfs.forEach(pdf => {
            const fileNumber = pdf.replace('Typko', '').replace('.pdf', '');
            const thumbnailPath = `images/typko-thumbs/${year}/${pdf.replace('.pdf', '.png')}`;
            html += `
                <a href="typko_pdfs/${year}/${pdf}" target="_blank" class="pdf-link" title="${pdf}">
                    <img src="${thumbnailPath}" alt="Náhled ${pdf}" class="pdf-thumbnail" loading="lazy">
                    <span class="pdf-label">Typko #${fileNumber}</span>
                </a>`;
        });
        
        html += `</div>
        </article>`;
    });
    
    archiveContainer.innerHTML = html;
}

// Inicializovat archív když je stránka načtena
document.addEventListener('DOMContentLoaded', initTypkoArchive);
