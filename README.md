
 <!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title> GS Luxuria Perfumes - Premium Fragrances</title>  
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">  
    <style>  
        * {  
            margin: 0;  
            padding: 0;  
            box-sizing: border-box;  
        }  
  
        body {  
            font-family: 'Arial', sans-serif;  
            line-height: 1.6;  
            color: #333;  
            overflow-x: hidden;  
        }  
  
        /* Header */  
        header {  
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);  
            color: white;  
            padding: 1rem 0;  
            position: fixed;  
            width: 100%;  
            top: 0;  
            z-index: 1000;  
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);  
        }  
  
        nav {  
            display: flex;  
            justify-content: space-between;  
            align-items: center;  
            max-width: 1200px;  
            margin: 0 auto;  
            padding: 0 2rem;  
        }  
  
        .logo {  
            font-size: 1.8rem;  
            font-weight: bold;  
            color: #ffd700;  
        }  
  
        .nav-links {  
            display: flex;  
            list-style: none;  
            gap: 2rem;  
        }  
  
        .nav-links a {  
            color: white;  
            text-decoration: none;  
            transition: color 0.3s;  
        }  
  
        .nav-links a:hover {  
            color: #ffd700;  
        }  
  
        .cart-icon {  
            position: relative;  
            font-size: 1.5rem;  
            cursor: pointer;  
        }  
  
        .cart-count {  
            position: absolute;  
            top: -8px;  
            right: -8px;  
            background: #ff4757;  
            color: white;  
            border-radius: 50%;  
            width: 20px;  
            height: 20px;  
            font-size: 0.8rem;  
            display: flex;  
            align-items: center;  
            justify-content: center;  
        }  
  
        .menu-toggle {  
            display: none;  
            font-size: 1.5rem;  
            cursor: pointer;  
        }  
  
        /* Hero Section */  
        .hero {  
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect fill="%231a1a2e" width="1200" height="600"/><circle fill="%23ffd700" opacity="0.1" cx="200" cy="200" r="150"/><circle fill="%23ff6b9d" opacity="0.1" cx="1000" cy="400" r="200"/><path fill="%23ff4757" opacity="0.05" d="M0 500 Q300 300 600 500 T1200 500"/></svg>');  
            background-size: cover;  
            height: 150vh;  
            display: flex;  
            align-items: center;  
            justify-content: center;  
            text-align: center;  
            color: white;  
            margin-top: 70px;  
        }  
  
        .hero-content h1 {  
            font-size: 3.5rem;  
            margin-bottom: 1rem;  
            animation: fadeInUp 1s ease;  
        }  
  
        .hero-content p {  
            font-size: 1.3rem;  
            margin-bottom: 2rem;  
            animation: fadeInUp 1s ease 0.2s both;  
        }  
  
        .cta-button {  
            display: inline-block;  
            background: linear-gradient(45deg, #ffd700, #ffed4e);  
            color: #1a1a2e;  
            padding: 1rem 2.5rem;  
            text-decoration: none;  
            border-radius: 50px;  
            font-weight: bold;  
            font-size: 1.1rem;  
            transition: transform 0.3s, box-shadow 0.3s;  
            animation: fadeInUp 1s ease 0.4s both;  
        }  
  
        .cta-button:hover {  
            transform: translateY(-3px);  
            box-shadow: 0 10px 30px rgba(255,215,0,0.4);  
        }  
  
        /* Products Section */  
        .products {  
            padding: 5rem 2rem;  
            max-width: 500px;  
            margin: 0 auto;  
        }  
  
        .section-title {  
            text-align: center;  
            font-size: 2.5rem;  
            margin-bottom: 3rem;  
            color: #1a1a2e;  
        }  
  
        .products-grid {  
            display: grid;  
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  
            gap: 2rem;  
        }  
  
        .product-card {  
            background: white;  
            border-radius: 20px;  
            overflow: hidden;  
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);  
            transition: transform 0.3s, box-shadow 0.3s;  
            cursor: pointer;  
        }  
  
        .product-card:hover {  
            transform: translateY(-10px);  
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);  
        }  
  
        .product-image {  
            height: 250px;  
            background: linear-gradient(45deg, #ff6b9d, #ffd700);  
            display: flex;  
            align-items: center;  
            justify-content: center;  
            font-size: 4rem;  
            color: white;  
        }  
  
        .product-info {  
            padding: 1.5rem;  
        }  
  
        .product-title {  
            font-size: 1.3rem;  
            margin-bottom: 0.5rem;  
            color: #1a1a2e;  
        }  
  
        .product-price {  
            font-size: 1.5rem;  
            font-weight: bold;  
            color: #ff4757;  
            margin-bottom: 1rem;  
        }  
  
        .product-add {  
            width: 100%;  
            background: linear-gradient(45deg, #1a1a2e, #16213e);  
            color: white;  
            border: none;  
            padding: 0.8rem;  
            border-radius: 10px;  
            font-size: 1rem;  
            cursor: pointer;  
            transition: background 0.3s;  
        }  
  
        .product-add:hover {  
            background: linear-gradient(45deg, #ffd700, #ffed4e);  
            color: #1a1a2e;  
        }  
  
        /* Cart Modal */  
        .cart-modal {  
            display: none;  
            position: fixed;  
            top: 0;  
            left: 0;  
            width: 100%;  
            height: 100%;  
            background: rgba(0,0,0,0.8);  
            z-index: 2000;  
        }  
  
        .cart-content {  
            position: absolute;  
            top: 50%;  
            left: 50%;  
            transform: translate(-50%, -50%);  
            background: white;  
            max-width: 500px;  
            width: 90%;  
            max-height: 80vh;  
            overflow-y: auto;  
            border-radius: 20px;  
            padding: 2rem;  
        }  
  
        .close-cart {  
            float: right;  
            font-size: 2rem;  
            cursor: pointer;  
            color: #999;  
        }  
  
        .cart-item {  
            display: flex;  
            justify-content: space-between;  
            align-items: center;  
            padding: 1rem 0;  
            border-bottom: 1px solid #eee;  
        }  
  
        .cart-total {  
            font-size: 1.5rem;  
            font-weight: bold;  
            text-align: center;  
            margin: 1rem 0;  
            color: #1a1a2e;  
        }  
  
        .checkout-btn {  
            width: 100%;  
            background: linear-gradient(45deg, #ff4757, #ff6b9d);  
            color: white;  
            border: none;  
            padding: 1rem;  
            border-radius: 10px;  
            font-size: 1.1rem;  
            cursor: pointer;  
        }  
  
        /* Footer */  
        footer {  
            background: #1a1a2e;  
            color: white;  
            text-align: center;  
            padding: 3rem 2rem 1rem;  
        }  
  
        /* Animations */  
        @keyframes fadeInUp {  
            from {  
                opacity: 0;  
                transform: translateY(30px);  
            }  
            to {  
                opacity: 1;  
                transform: translateY(0);  
            }  
        }  
  
        /* Mobile Responsive */  
        @media (max-width: 768px) {  
            .menu-toggle {  
                display: block;  
            }  
  
            .nav-links {  
                display: none;  
                position: absolute;  
                top: 100%;  
                left: 0;  
                width: 100%;  
                background: #1a1a2e;  
                flex-direction: column;  
                padding: 1rem;  
            }  
  
            .nav-links.active {  
                display: flex;  
            }  
  
            .hero-content h1 {  
                font-size: 2.5rem;  
            }  
  
            .products-grid {  
                grid-template-columns: 1fr;  
            }  
  
            .section-title {  
                font-size: 2rem;  
            }  
        }  
    </style>  
</head>  
<body>  
    <!-- Header -->  
    <header>  
        <nav>  
            <div class="logo">Luxuria</div>  
            <ul class="nav-links">  
                <li><a href="#home">Home</a></li>  
                <li><a href="#products">Shop</a></li>  
                <li><a href="#about">About</a></li>  
                <li><a href="#contact">Contact</a></li>  
            </ul>  
            <div class="cart-icon" onclick="toggleCart()">  
                <i class="fas fa-shopping-cart"></i>  
                <span class="cart-count" id="cartCount">0</span>  
            </div>  
            <div class="menu-toggle" onclick="toggleMenu()">  
                <i class="fas fa-bars"></i>  
            </div>  
        </nav>  
    </header>  
  
    <!-- Hero Section -->  
    <section class="hero" id="home">  
        <div class="hero-content">  
            <h1>Luxuria Perfumes</h1>  
            <p>Discover the essence of elegance with our premium fragrance collection</p>  
            <a href="#products" class="cta-button">Shop Now</a>  
        </div>  
    </section>  
  
    <!-- Products Section -->  
    <section class="products" id="products">  
        <h2 class="section-title">Our Collection</h2>  
        <div class="products-grid">  
            <div class="product-card" data-name="Eternal Rose" data-price="89.99">  
                <div class="product-image">  
                    <i class="fas fa-spray-can"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Eternal Rose</h3>  
                    <div class="product-price">$89.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
  
            <div class="product-card" data-name="Ocean Breeze" data-price="79.99">  
                <div class="product-image">  
                    <i class="fas fa-wind"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Ocean Breeze</h3>  
                    <div class="product-price">$79.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
  
            <div class="product-card" data-name="Midnight Velvet" data-price="99.99">  
                <div class="product-image">  
                    <i class="fas fa-moon"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Midnight Velvet</h3>  
                    <div class="product-price">$99.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
  
            <div class="product-card" data-name="Golden Ember" data-price="119.99">  
                <div class="product-image">  
                    <i class="fas fa-fire"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Golden Ember</h3>  
                    <div class="product-price">$119.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
  
            <div class="product-card" data-name="Wild Orchid" data-price="94.99">  
                <div class="product-image">  
                    <i class="fas fa-seedling"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Wild Orchid</h3>  
                    <div class="product-price">$94.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
  
            <div class="product-card" data-name="Citrus Dawn" data-price="69.99">  
                <div class="product-image">  
                    <i class="fas fa-sun"></i>  
                </div>  
                <div class="product-info">  
                    <h3 class="product-title">Citrus Dawn</h3>  
                    <div class="product-price">$69.99</div>  
                    <button class="product-add" onclick="addToCart(this)">Add to Cart</button>  
                </div>  
            </div>  
        </div>  
    </section>  
  
    <!-- Cart Modal -->  
    <div class="cart-modal" id="cartModal">  
        <div class="cart-content">  
            <span class="close-cart" onclick="toggleCart()">&times;</span>  
            <h2>Shopping Cart</h2>  
            <div id="cartItems"></div>  
            <div class="cart-total" id="cartTotal">$0.00</div>  
            <button class="checkout-btn" onclick="checkout()">Proceed to Checkout</button>  
        </div>  
    </div>  
  
    <!-- Footer -->  
    <footer>  
        <p>&copy; 2024 Luxuria Perfumes. All rights reserved. | Made with <i class="fas fa-heart" style="color: #ff4757;"></i></p>  
    </footer>  
  
    <script>  
        let cart = [];  
        let cartCount = 0;  
  
        // Mobile menu toggle  
        function toggleMenu() {  
            const navLinks = document.querySelector('.nav-links');  
            navLinks.classList.toggle('active');  
        }  
  
        // Cart functions  
        function addToCart(button) {  
            const productCard = button.closest('.product-card');  
            const name = productCard.dataset.name;  
            const price = parseFloat(productCard.dataset.price);  
  
            const existingItem = cart.find(item => item.name === name);  
            if (existingItem) {  
                existingItem.quantity += 1;  
            } else {  
                cart.push({ name, price, quantity: 1 });  
            }  
  
            cartCount++;  
            updateCartDisplay();  
            showNotification(`${name} added to cart!`);  
        }  
  
        function updateCartDisplay() {  
            document.getElementById('cartCount').textContent = cartCount;  
        }  
  
        function toggleCart() {  
            const modal = document.getElementById('cartModal');  
            modal.style.display = modal.style.display === 'block' ? 'none' : 'block';  
            if (modal.style.display === 'block') {  
                displayCartItems();  
            }  
        }  
  
        function displayCartItems() {  
            const cartItems = document.getElementById('cartItems');  
            const cartTotal = document.getElementById('cartTotal');  
              
            if (cart.length === 0) {  
                cartItems.innerHTML = '<p>Your cart is empty</p>';  
                cartTotal.textContent = '$0.00';  
                return;  
            }  
  
            let total = 0;  
            cartItems.innerHTML = cart.map(item => {  
                const itemTotal = item.price * item.quantity;  
                total += itemTotal;  
                return `  
                    <div class="cart-item">  
                        <span>${item.name} x${item.quantity}</span>  
                        <span>$${itemTotal.toFixed(2)}</span>  
                    </div>  
                `;  
            }).join('');  
  
            cartTotal.textContent = `Total: $${total.toFixed(2)}`;  
        }  
  
        function checkout() {  
            if (cart.length === 0) {  
                alert('Your cart is empty!');  
                return;  
            }  
            alert('Thank you for your order! This is a demo - redirecting to payment...');  
            cart = [];  
            cartCount = 0;  
            updateCartDisplay();  
            toggleCart();  
        }  
  
        function showNotification(message) {  
            // Simple notification  
            const notification = document.createElement('div');  
            notification.style.cssText = `  
                position: fixed;  
                top: 100px;  
                right: 20px;  
                background: #4ecdc4;  
                color: white;  
                padding: 1rem 2rem;  
                border-radius: 10px;  
                z-index: 3000;  
                animation: slideIn 0.3s ease;  
            `;  
            notification.textContent = message;  
            document.body.appendChild(notification);  
              
            setTimeout(() => {  
                notification.remove();  
            }, 3000);  
        }  
  
        // Close cart when clicking outside  
        window.onclick = function(event) {  
            const modal = document.getElementById('cartModal');  
            if (event.target === modal) {  
                toggleCart();  
            }  
        }  
  
        // Smooth scrolling for navigation links  
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {  
            anchor.addEventListener('click', function (e) {  
                e.preventDefault();  
                const target = document.querySelector(this.getAttribute('href'));  
                if (target) {  
                    target.scrollIntoView({  
                        behavior: 'smooth',  
                        block: 'start'  
                    });  
                }  
            });  
        });  
  
        // Add CSS for notification animation  
        const style = document.createElement('style');  
        style.textContent = `  
            @keyframes slideIn {  
                from { transform: translateX  
