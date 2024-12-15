document.getElementById('imageInput').addEventListener('change', handleImageUpload);
document.getElementById('colorCount').addEventListener('change', updateColorCount);

let colorCount = 10;

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const img = new Image();
        const reader = new FileReader();
        
        reader.onload = function(e) {
            img.src = e.target.result;
        };

        reader.readAsDataURL(file);
        
        img.onload = function() {
            // Show image preview
            const imagePreview = document.getElementById('imagePreview');
            imagePreview.src = img.src;
            imagePreview.style.display = 'block';

            // Process the image
            processImage(img);
        };
    }
}

function updateColorCount() {
    colorCount = parseInt(document.getElementById('colorCount').value, 10);
}

function processImage(img) {
    const canvas = document.getElementById('imageCanvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);
    
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const colors = extractColors(imageData.data);
    displayColors(colors);
}

function extractColors(data) {
    const colorMap = {};
    const length = data.length;
    
    for (let i = 0; i < length; i += 4) {
        const r = data[i];
        const g = data[i + 1];
        const b = data[i + 2];
        const rgb = `rgb(${r},${g},${b})`;
        
        if (colorMap[rgb]) {
            colorMap[rgb]++;
        } else {
            colorMap[rgb] = 1;
        }
    }
    
    // Convert to array and sort by frequency
    const sortedColors = Object.entries(colorMap)
        .sort((a, b) => b[1] - a[1])
        .slice(0, colorCount)
        .map(([color]) => color);
    
    // Reduce similar colors
    return reduceSimilarColors(sortedColors);
}

function reduceSimilarColors(colors) {
    const tolerance = 50; // Tolerance level for color similarity
    const reducedColors = [];
    
    colors.forEach(color => {
        const [r, g, b] = color.match(/\d+/g).map(Number);
        let added = false;
        
        for (const existingColor of reducedColors) {
            const [er, eg, eb] = existingColor.match(/\d+/g).map(Number);
            if (Math.abs(r - er) < tolerance && Math.abs(g - eg) < tolerance && Math.abs(b - eb) < tolerance) {
                added = true;
                break;
            }
        }
        
        if (!added) {
            reducedColors.push(color);
        }
    });
    
    return reducedColors;
}

function displayColors(colors) {
    const colorPalette = document.getElementById('colorPalette');
    colorPalette.innerHTML = '';
    
    colors.forEach(color => {
        const div = document.createElement('div');
        div.classList.add('color-box');
        div.style.backgroundColor = color;
        
        const colorInfo = document.createElement('div');
        colorInfo.classList.add('color-info');
        colorInfo.textContent = `${color} (${hexToRgb(color)})`;
        
        div.appendChild(colorInfo);
        colorPalette.appendChild(div);
    });
}

function hexToRgb(color) {
    const [r, g, b] = color.match(/\d+/g);
    return `#${parseInt(r).toString(16).padStart(2, '0')}${parseInt(g).toString(16).padStart(2, '0')}${parseInt(b).toString(16).padStart(2, '0')}`;
}
