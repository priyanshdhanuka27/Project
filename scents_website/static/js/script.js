window.addEventListener('scroll', function() {
    const fadeOut = document.querySelector('.fade-out');
    const fadeIn = document.querySelector('.fade-in');
    const windowHeight = window.innerHeight;
    const scrollY = window.scrollY;
    const docHeight = document.body.scrollHeight;

    // Adjust opacity for fade-out effect
    fadeOut.style.opacity = 1 - (scrollY / windowHeight);

    // Adjust opacity for fade-in effect
    fadeIn.style.opacity = (scrollY / (docHeight - windowHeight));
});

// Function to update the cart count
function updateCartCount() {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    let cartCountElement = document.getElementById('cartCount');
    let totalCount = 0;
    cartItems.forEach(item => {
        totalCount += item.quantity || 1;
    });
    cartCountElement.textContent = totalCount;
}

function addToCart(productName, price) {
    fetch('/cart/add/', {  // Ensure this endpoint exists in your Django app
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() // Ensure CSRF protection
        },
        body: JSON.stringify({ name: productName, price: price })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || productName + " added to cart!");
        updateCartCount();
    })
    .catch(error => console.error('Error:', error));
}

// Function to get CSRF token from Django
function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken'))
        ?.split('=')[1];
}


// Call the function initially to set the initial count
updateCartCount();