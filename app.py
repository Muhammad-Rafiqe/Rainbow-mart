from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rainbow Mart - Nowshera | Professional Online Grocery Store</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;-webkit-tap-highlight-color:transparent}
body{background:#f5f7fb;color:#111;padding-bottom:95px}
.top-red{background:#e53935;color:#fff;text-align:center;padding:8px 10px;font-size:11px;font-weight:700;animation:slideDown .5s ease;cursor:pointer}
.header{background:rgba(255,255,255,.95);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);padding:10px 14px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:999;box-shadow:0 4px 20px rgba(0,0,0,.08)}
.logo{display:flex;align-items:center;gap:8px;cursor:pointer;transition:.3s}
.logo:hover{transform:scale(1.05)}
.logo-icon{width:42px;height:42px;background:conic-gradient(from 0deg,#ff0000,#ffff00,#00ff00,#0000ff,#ff0000);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;box-shadow:0 4px 12px rgba(0,0,0,.15);animation:rotate 8s linear infinite}
.logo-text{font-weight:900;font-style:italic;font-size:22px}
.delivery{flex:1;margin-left:12px;cursor:pointer;padding:6px 10px;border-radius:12px;transition:.3s}
.delivery:hover{background:rgba(0,168,232,.1);transform:translateY(-1px)}
.delivery b{font-size:12px;display:flex;align-items:center;gap:5px}
.delivery span{font-size:10px;color:#666}
.profile{width:40px;height:40px;background:linear-gradient(135deg,#f0f0f0,#e0e0e0);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.3s;box-shadow:0 2px 8px rgba(0,0,0,.1)}
.profile:hover{background:linear-gradient(135deg,#00a8e8,#0077b6);color:#fff;transform:scale(1.1) rotate(5deg)}

/* Flash Sale Banner */
.flash-sale-box{margin:10px;background:linear-gradient(135deg,#ff416c,#ff4b2b);border-radius:18px;padding:15px;color:#fff;display:flex;justify-content:space-between;align-items:center;box-shadow:0 8px 20px rgba(255,65,108,.3)}
.flash-timer{background:rgba(0,0,0,.2);padding:6px 12px;border-radius:10px;font-weight:900;font-size:13px;letter-spacing:1px}

.promo-banner{margin:10px;border-radius:18px;overflow:hidden;height:140px;position:relative;background:linear-gradient(135deg,#4a006b,#9c007a);display:flex;align-items:center;justify-content:center;color:#fff;text-align:center;cursor:pointer;transition:.4s;box-shadow:0 8px 20px rgba(74,0,107,.3)}
.promo-banner:hover{transform:translateY(-4px) scale(1.01)}

.cat-title{text-align:center;padding:18px 0 12px;font-size:22px;font-weight:900;position:relative}
.cat-title:before,.cat-title:after{content:'';position:absolute;top:50%;width:22%;height:1px;background:#ddd}
.cat-title:before{left:10%}.cat-title:after{right:10%}

.shop-by-cat{background:linear-gradient(135deg,#00a8e8,#0090c9);padding:16px 12px;border-radius:20px;margin:0 10px;box-shadow:0 8px 24px rgba(0,168,232,.3)}
.cat-grid{display:flex;gap:12px;overflow-x:auto;scrollbar-width:none}
.cat-item{flex:0 0 110px;text-align:center;cursor:pointer;transition:.3s}
.cat-item:hover{transform:translateY(-6px)}
.cat-img{width:110px;height:110px;background:#fff;border-radius:20px;overflow:hidden;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(0,0,0,.12)}
.cat-img img{width:100%;height:100%;object-fit:cover;transition:.4s}
.cat-item:hover .cat-img img{transform:scale(1.1)}
.cat-item p{font-size:11px;font-weight:800;margin-top:8px;color:#fff}

.section-banner{margin:12px 10px;border-radius:18px;overflow:hidden;height:130px;position:relative;display:flex;align-items:center;padding:14px;cursor:pointer;transition:.4s;box-shadow:0 6px 18px rgba(0,0,0,.12)}
.section-banner:hover{transform:translateY(-3px)}

.prod-wrap{background:rgba(238,242,255,.9);backdrop-filter:blur(8px);padding:10px;border-radius:18px;margin:0 10px 10px}
.prod-scroll{display:flex;gap:10px;overflow-x:auto;scrollbar-width:none;padding:4px 2px}
.prod-card{flex:0 0 158px;background:#fff;border-radius:16px;padding:10px;text-align:center;position:relative;box-shadow:0 2px 10px rgba(0,0,0,.06);transition:.35s;cursor:pointer}
.prod-card:hover{transform:translateY(-6px) scale(1.02);box-shadow:0 12px 28px rgba(0,0,0,.15)}
.prod-card img{width:100%;height:100px;object-fit:contain}
.prod-card h3{font-size:12px;font-weight:700;height:32px;overflow:hidden;margin:8px 0 4px;text-align:left}
.wt{font-size:10px;color:#888;text-align:left}
.price{text-align:left;font-weight:800;font-size:14px;margin:6px 0}
.heart{position:absolute;top:10px;right:10px;color:#ccc;transition:.3s;cursor:pointer;width:26px;height:26px;background:rgba(255,255,255,.9);border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(0,0,0,.1)}
.heart.active{color:#ff1a4d;background:#ffe0e8}
.add-btn{background:linear-gradient(135deg,#00a8e8,#0090c9);color:#fff;border:none;width:100%;padding:10px;border-radius:12px;font-weight:800;font-size:12px;margin-top:6px;cursor:pointer;transition:.3s;box-shadow:0 4px 10px rgba(0,168,232,.3)}
.qty-box{display:flex;gap:6px;margin-top:8px;animation:popIn .3s ease}
.qty-box button{flex:0 0 38px;background:linear-gradient(135deg,#00a8e8,#0090c9);color:#fff;border:none;border-radius:10px;height:38px;font-size:18px;font-weight:900;cursor:pointer}
.qty-box span{flex:1;background:#f8f9ff;border:1px solid #e0e6ff;border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800}
.view-all{text-align:right;padding:6px 16px 10px;color:#00a8e8;font-size:13px;font-weight:700;cursor:pointer}

/* Features Highlights */
.features-container{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:15px 10px}
.feature-card{background:#fff;padding:14px 8px;border-radius:16px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,.05)}
.feature-card i{font-size:24px;color:#00a8e8;margin-bottom:6px}
.feature-card h4{font-size:11px;font-weight:800;color:#333}
.feature-card p{font-size:9px;color:#666;margin-top:2px}

/* Brand Grid */
.brands-section{margin:15px 10px;background:#fff;border-radius:20px;padding:16px;box-shadow:0 4px 15px rgba(0,0,0,.05)}
.brands-grid{display:flex;gap:15px;overflow-x:auto;scrollbar-width:none;align-items:center;padding:6px}
.brand-item{flex:0 0 80px;text-align:center;font-weight:800;font-size:12px;color:#555;background:#f8f9ff;padding:12px 8px;border-radius:12px;border:1px solid #eee}

/* Testimonials Section */
.testimonials-section{margin:15px 10px;background:linear-gradient(135deg,#111,#333);color:#fff;border-radius:20px;padding:20px}
.testi-card{background:rgba(255,255,255,.1);backdrop-filter:blur(10px);padding:14px;border-radius:14px;margin-top:10px}
.testi-card p{font-size:12px;font-style:italic;opacity:.9}
.testi-author{font-size:11px;font-weight:800;color:#00a8e8;margin-top:6px}

/* Write Review Box */
.review-form-box{background:#fff;margin:15px 10px;border-radius:20px;padding:18px;box-shadow:0 4px 15px rgba(0,0,0,.05);color:#111}
.review-form-box input, .review-form-box textarea{width:100%;padding:10px 14px;border:1px solid #ddd;border-radius:10px;font-size:13px;outline:none;margin-top:8px;background:#f8f9ff}
.review-form-box button{background:linear-gradient(135deg,#00a8e8,#0077b6);color:#fff;border:none;width:100%;padding:12px;border-radius:10px;font-weight:800;margin-top:10px;cursor:pointer}

/* FAQ Section */
.faq-section{margin:15px 10px;background:#fff;border-radius:20px;padding:18px;box-shadow:0 4px 15px rgba(0,0,0,.05)}
.faq-item{margin-bottom:12px;border-bottom:1px solid #eee;padding-bottom:10px}
.faq-q{font-weight:800;font-size:13px;color:#222;margin-bottom:4px}
.faq-a{font-size:11px;color:#666}

.footer-blue{background:linear-gradient(135deg,#00a8e8,#0077b6);color:#fff;padding:30px 18px 120px}
.bottom-nav{position:fixed;bottom:12px;left:10px;right:10px;background:rgba(255,255,255,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-radius:30px;display:flex;justify-content:space-around;padding:10px 0;box-shadow:0 10px 40px rgba(0,0,0,.18);z-index:1000;border:1px solid rgba(255,255,255,.6)}
.b-nav{font-size:10px;font-weight:600;text-align:center;opacity:.6;cursor:pointer;transition:.3s;padding:4px 12px;border-radius:20px;position:relative}
.b-nav.active{opacity:1;background:rgba(0,168,232,.15);color:#00a8e8;transform:translateY(-2px)}
.b-nav i{font-size:20px;display:block;margin-bottom:2px}
.cart-badge{position:absolute;top:-6px;right:4px;background:linear-gradient(135deg,#000,#333);color:#fff;font-size:10px;width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;animation:bounce 1s infinite}
.whatsapp-float{position:fixed;bottom:100px;right:14px;background:linear-gradient(135deg,#25D366,#128C7E);width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:28px;z-index:999;box-shadow:0 6px 20px rgba(37,211,102,.4);cursor:pointer;animation:float 3s ease-in-out infinite}
.up-float{position:fixed;bottom:170px;right:14px;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(0,0,0,.15);z-index:999;cursor:pointer}

/* Modals & Overlays */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.6);display:none;z-index:20000;align-items:center;justify-content:center}
.modal-overlay.active{display:flex;animation:fadeIn .3s}
.modal-box{background:#fff;width:90%;max-width:360px;border-radius:24px;padding:20px;box-shadow:0 20px 60px rgba(0,0,0,0.3);animation:slideUp .4s ease;z-index:20001;position:relative}

/* Search Box */
.search-box{position:fixed;top:0;left:0;right:0;background:#fff;padding:14px;z-index:21000;transform:translateY(-100%);transition:.4s cubic-bezier(.4,0,.2,1);box-shadow:0 8px 30px rgba(0,0,0,.15)}
.search-box.active{transform:translateY(0)}
.search-input{width:100%;background:#f3f5f7;border:1px solid #e0e6ef;border-radius:50px;padding:14px 18px;font-size:14px;outline:none}
.search-results-container{max-height:60vh;overflow-y:auto;margin-top:10px}

@keyframes slideDown{from{transform:translateY(-100%);opacity:0}to{transform:translateY(0);opacity:1}}
@keyframes slideUp{from{transform:translateY(30px);opacity:0}to{transform:translateY(0);opacity:1}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes popIn{0%{transform:scale(.8);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes rotate{from{rotate:0deg}to{rotate:360deg}}

#cartDrawer{position:fixed;top:0;right:-100%;width:92%;max-width:400px;height:100%;background:#fff;z-index:25000;transition:.4s cubic-bezier(.4,0,.2,1);padding:18px;display:flex;flex-direction:column;box-shadow:-10px 0 40px rgba(0,0,0,.2)}
#cartDrawer.active{right:0}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,0.5);display:none;z-index:15000}
.overlay.active{display:block;animation:fadeIn .3s}
</style>
</head>
<body>
<div class="top-red" onclick="showToast('We are OPEN now! 9AM - 11PM Delivery in Nowshera')">⚡ Open Now! Express Delivery in Nowshera & Peshawar (9:00 AM - 11:00 PM)</div>
<div class="header" id="mainHeader">
<div class="logo" onclick="scrollToTop()"><div class="logo-icon">R</div><div class="logo-text">Rainbow</div></div>
<div class="delivery" onclick="openDelivery()"><b><i class="fa fa-map-marker-alt" style="color:#00a8e8"></i> Delivery to <i class="fa fa-caret-down"></i></b><span id="deliveryText">Nisatta, Nowshera, Peshawar - KPK</span></div>
<div class="profile" onclick="openProfile()"><i class="fa fa-user"></i></div>
</div>

<!-- Flash Sale Timer Banner -->
<div class="flash-sale-box">
<div>
<h3 style="font-size:16px;font-weight:900">🔥 MEGA FLASH SALE</h3>
<p style="font-size:10px;opacity:.9">Extra discounts on fresh items today!</p>
</div>
<div class="flash-timer" id="countdown">05:42:19</div>
</div>

<div class="promo-banner" onclick="showToast('Shaadi Offer - Till 11th Nov 2026!')">
<div><div style="border:3px double gold;padding:10px 20px;border-radius:30px;background:rgba(0,0,0,.15);backdrop-filter:blur(4px)"><h2>Shaadi<br>Khana Abadi</h2><p style="font-size:10px;opacity:.9">Naye Bandhan Shopping Old Nahi</p><p style="background:#fff;color:#8b0050;font-size:10px;font-weight:800;padding:4px 10px;border-radius:20px;margin-top:6px">OFFER TILL 11th NOVEMBER 2026</p></div></div>
</div>

<!-- Why Choose Us Features -->
<div class="features-container">
<div class="feature-card"><i class="fa fa-bolt"></i><h4>Fast Delivery</h4><p>Within 2 Hours</p></div>
<div class="feature-card"><i class="fa fa-shield-alt"></i><h4>100% Fresh</h4><p>Quality Guaranteed</p></div>
<div class="feature-card"><i class="fa fa-tags"></i><h4>Best Prices</h4><p>Market Competitive</p></div>
</div>

<div class="cat-title" id="shopCat">Shop by Category</div>
<div class="shop-by-cat"><div class="cat-grid">
<div class="cat-item" onclick="filterCat('ultra')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=300" onerror="this.src='https://images.unsplash.com/photo-1610832958506-aa56368176cf?w=300'"></div><p>ULTRA FRESH</p></div>
<div class="cat-item" onclick="filterCat('grocery')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=300" onerror="this.src='https://images.unsplash.com/photo-1578911373434-0cb395d2c4d4?w=300'"></div><p>GROCERY</p></div>
<div class="cat-item" onclick="filterCat('dry')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=300" onerror="this.src='https://images.unsplash.com/photo-1573551089778-46a7abc39d9f?w=300'"></div><p>DRY FRUITS</p></div>
<div class="cat-item" onclick="filterCat('dairy')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1550583724-b2692b85b150?w=300" onerror="this.src='https://images.unsplash.com/photo-1488477181946-64290103bbd6?w=300'"></div><p>BREAKFAST & DAIRY</p></div>
<div class="cat-item" onclick="filterCat('bev')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1553456558-aff542a7b319?w=300" onerror="this.src='https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300'"></div><p>BEVERAGES</p></div>
<div class="cat-item" onclick="filterCat('health')"><div class="cat-img"><img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=300" onerror="this.src='https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=300'"></div><p>HEALTH & BEAUTY</p></div>
</div></div>

<div class="cat-title">Ultra Fresh</div>
<div class="section-banner" style="background:linear-gradient(90deg,#0a8a28 60%,#81c784);" onclick="scrollToSec('ultraFresh')"><h2 style="color:#fff;font-size:22px;line-height:1"><span style="font-family:cursive;font-size:16px;opacity:.9">Your</span> Daily<br><span style="background:yellow;color:#000;padding:2px 8px;border-radius:6px;font-size:26px;font-weight:900">Dose of Fresh</span></h2><img src="https://images.unsplash.com/photo-1542838132-92c53300491e?w=200" style="position:absolute;right:10px;width:110px;height:90px;border-radius:12px;object-fit:cover"></div>
<div class="prod-wrap"><div class="prod-scroll" id="ultraFresh"></div></div>
<div class="view-all" onclick="scrollToSec('ultraFresh')">View all →</div>

<div class="cat-title">Beverages</div>
<div class="section-banner" style="background:linear-gradient(90deg,#29b6f6,#81d4fa);" onclick="scrollToSec('beverages')">
<h2 style="color:#fff;font-size:20px;font-weight:900">ONE SIP<br>ENDLESS<br>REFRESHMENT!</h2>
<img src="https://images.unsplash.com/photo-1554866585-cd94860890b7?w=300" style="position:absolute;right:10px;bottom:0;width:150px;height:120px;object-fit:contain">
</div>
<div class="prod-wrap"><div class="prod-scroll" id="beverages"></div></div>
<div class="view-all" onclick="scrollToSec('beverages')">View all →</div>

<div class="cat-title">Health & Beauty</div>
<div class="section-banner" style="background:linear-gradient(90deg,#ce93d8,#f3e5f5);" onclick="scrollToSec('health')"><h2 style="font-family:cursive;color:#6a1b9a;font-size:32px;line-height:.9">Health &<br>Beauty</h2><img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=250" style="position:absolute;right:10px;width:160px;height:100px;object-fit:contain"></div>
<div class="prod-wrap"><div class="prod-scroll" id="health"></div></div>
<div class="view-all" onclick="scrollToSec('health')">View all →</div>

<div class="cat-title">Breakfast & Dairy</div>
<div class="section-banner" style="background:linear-gradient(90deg,#90caf9,#e3f2fd);" onclick="scrollToSec('dairy')"><div><h2 style="color:#0d47a1;font-style:italic;font-size:20px">Breakfast & Dairy</h2><p style="font-size:11px;font-weight:800;color:#1565c0">Fuel Your Morning Right!</p><p style="background:#0d47a1;color:#fff;display:inline-block;padding:5px 12px;border-radius:20px;font-size:10px;margin-top:8px">ORDER NOW →</p></div><img src="https://images.unsplash.com/photo-1550583724-b2692b85b150?w=250" style="position:absolute;right:10px;width:150px;height:100px;object-fit:contain"></div>
<div class="prod-wrap"><div class="prod-scroll" id="dairy"></div></div>
<div class="view-all" onclick="scrollToSec('dairy')">View all →</div>

<div class="cat-title">Frozen Food</div>
<div class="section-banner" style="background:linear-gradient(90deg,#81d4fa,#e1f5fe);" onclick="scrollToSec('frozen')"><h2 style="font-size:26px;color:#0277bd;font-weight:900">the Flavor<br><span style="color:#fff;text-shadow:0 2px 8px #0277bd">Freeze</span> <span style="background:#ffeb3b;color:#000;font-size:10px;padding:5px 10px;border-radius:20px">ORDER NOW</span></h2><img src="https://images.unsplash.com/photo-1568909344668-6f14a07b56a0?w=250" style="position:absolute;right:10px;width:160px;height:100px;object-fit:contain"></div>
<div class="prod-wrap"><div class="prod-scroll" id="frozen"></div></div>
<div class="view-all" onclick="scrollToSec('frozen')">View all →</div>

<div class="cat-title">Baby Products</div>
<div class="section-banner" style="background:linear-gradient(90deg,#80deea,#e0f7fa);" onclick="scrollToSec('baby')"><h2 style="font-weight:900;font-size:24px"><span style="background:#ffeb3b;padding:3px 8px;border-radius:8px">B</span><span style="background:#90caf9;padding:3px 8px;border-radius:8px">A</span><span style="background:#f48fb1;padding:3px 8px;border-radius:8px">B</span><span style="background:#a5d6a7;padding:3px 8px;border-radius:8px">Y</span><br><span style="color:#e91e63;font-size:32px">CARE</span></h2><img src="https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=250" style="position:absolute;right:10px;width:140px;height:100px;object-fit:contain"></div>
<div class="prod-wrap"><div class="prod-scroll" id="baby"></div></div>

<!-- Trusted Brands Section -->
<div class="brands-section">
<h3 style="font-size:14px;font-weight:900;margin-bottom:10px;text-align:center">Trusted Popular Brands</h3>
<div class="brands-grid">
<div class="brand-item">Nestle</div>
<div class="brand-item">K&N's</div>
<div class="brand-item">Olper's</div>
<div class="brand-item">Colgate</div>
<div class="brand-item">Johnsons</div>
<div class="brand-item">National</div>
</div>
</div>

<!-- Customer Testimonials Section -->
<div class="testimonials-section">
<h3 style="font-size:16px;font-weight:900;text-align:center">💬 What Our Customers Say</h3>
<div id="reviewsContainer">
<div class="testi-card">
<p>"Best grocery delivery service in Nowshera! Chicken and vegetables are always fresh and delivered quickly."</p>
<div class="testi-author">- Usman Khan (Nisatta)</div>
</div>
<div class="testi-card">
<p>"Ordering on WhatsApp is so easy and convenient. Highly recommended store!"</p>
<div class="testi-author">- Ayesha Bibi (Nowshera Cantt)</div>
</div>
</div>
</div>

<!-- Write Customer Review Form -->
<div class="review-form-box">
<h3 style="font-size:15px;font-weight:900;margin-bottom:6px"><i class="fa fa-star" style="color:#ffb703"></i> Write Your Review</h3>
<p style="font-size:11px;color:#666;margin-bottom:10px">Share your experience with Rainbow Mart</p>
<input type="text" id="reviewName" placeholder="Your Name (e.g. Ali Khan)">
<textarea id="reviewText" rows="3" placeholder="Write your review here..."></textarea>
<button onclick="submitReview()">Submit Review</button>
</div>

<!-- FAQ Section -->
<div class="faq-section">
<h3 style="font-size:16px;font-weight:900;margin-bottom:12px;text-align:center">❓ Frequently Asked Questions</h3>
<div class="faq-item">
<div class="faq-q">What are your delivery hours?</div>
<div class="faq-a">We deliver daily from 9:00 AM to 11:00 PM across Nowshera and Peshawar.</div>
</div>
<div class="faq-item">
<div class="faq-q">How can I pay for my order?</div>
<div class="faq-a">We currently offer Cash on Delivery (COD) and direct WhatsApp order confirmation.</div>
</div>
<div class="faq-item">
<div class="faq-q">Are the vegetables and meat fresh?</div>
<div class="faq-a">Yes! 100% farm-fresh vegetables and fresh halal meat are sourced daily.</div>
</div>
</div>

<div class="footer-blue">
<h3 style="font-size:32px;font-style:italic;font-weight:900">Rainbow</h3>
<p style="font-size:12px;opacity:.9;margin-top:20px;font-weight:800">Contact Us</p>
<div class="contact-item" onclick="window.open('https://wa.me/923464621962','_blank')" style="cursor:pointer;margin-top:8px"><p style="font-size:11px;opacity:.8">WHATSAPP</p><p style="font-weight:700">+92 346 4621962</p></div>
<div class="contact-item" onclick="window.location.href='mailto:rafiiedu589@gmail.com'" style="cursor:pointer;margin-top:8px"><p style="font-size:11px;opacity:.8">EMAIL</p><p style="font-weight:700">rafiiedu589@gmail.com</p></div>
<div class="contact-item" style="margin-top:8px"><p style="font-size:11px;opacity:.8">ADDRESS</p><p style="font-weight:600;font-size:13px">Rainbow Mart - Nisatta, Nowshera, KPK</p></div>
<p style="text-align:center;margin-top:30px;font-size:12px;opacity:.9">© 2026 Rainbow Mart | Powered by Rafii Edu</p>
</div>

<!-- Search Box -->
<div class="search-box" id="searchBox">
<div style="display:flex;gap:8px;align-items:center">
<input class="search-input" id="searchInput" placeholder="Search fresh chicken, tomato, milk..." onkeyup="searchProd()">
<button onclick="closeSearch()" style="background:#f0f0f0;border:none;width:42px;height:42px;border-radius:50%;font-weight:900;cursor:pointer">X</button>
</div>
<div class="search-results-container" id="searchResults"></div>
</div>

<!-- Profile Modal -->
<div class="modal-overlay" id="profileModal" onclick="closeModals()">
<div class="modal-box" onclick="event.stopPropagation()">
<div style="text-align:center">
<div style="width:80px;height:80px;background:linear-gradient(135deg,#00a8e8,#0077b6);border-radius:50%;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:32px"><i class="fa fa-user"></i></div>
<h2 style="font-weight:900">Rafii Edu</h2>
<p style="color:#666;font-size:13px;margin:6px 0">Rainbow Mart Owner</p>
<div style="background:#f5f7fb;border-radius:16px;padding:12px;margin:14px 0;text-align:left">
<p style="font-size:12px;margin:6px 0"><i class="fa fa-phone" style="color:#00a8e8"></i> +92 346 4621962</p>
<p style="font-size:12px;margin:6px 0"><i class="fa fa-envelope" style="color:#00a8e8"></i> rafiiedu589@gmail.com</p>
<p style="font-size:12px;margin:6px 0"><i class="fa fa-map-marker-alt" style="color:#00a8e8"></i> Nisatta, Nowshera, KPK</p>
</div>
<button onclick="window.open('https://wa.me/923464621962','_blank')" style="background:#25D366;color:#fff;border:none;width:100%;padding:14px;border-radius:12px;font-weight:800;cursor:pointer"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</button>
<button onclick="closeModals()" style="background:#f0f0f0;border:none;width:100%;padding:12px;border-radius:12px;font-weight:700;margin-top:8px;cursor:pointer">Close</button>
</div>
</div>
</div>

<!-- Delivery Location Modal -->
<div class="modal-overlay" id="deliveryModal" onclick="closeModals()">
<div class="modal-box" onclick="event.stopPropagation()">
<h2 style="font-weight:900"><i class="fa fa-map-marker-alt" style="color:#00a8e8"></i> Delivery Location</h2>
<p style="font-size:12px;color:#666;margin:8px 0">Select or type your exact address in Nowshera / Peshawar</p>

<div style="margin:10px 0;">
<input type="text" id="customAddressInput" placeholder="Enter custom address (e.g. Street 4, Nisatta)..." style="width:100%;padding:10px 14px;border:1px solid #ddd;border-radius:10px;font-size:13px;outline:none;background:#f8f9ff;">
<button onclick="saveCustomLocation()" style="background:#25D366;color:#fff;border:none;width:100%;padding:10px;border-radius:10px;font-weight:800;margin-top:6px;cursor:pointer;"><i class="fa fa-save"></i> Save Address</button>
</div>

<hr style="border:0;border-top:1px solid #eee;margin:12px 0;">

<div style="max-height:180px;overflow-y:auto;">
<div onclick="selectLocation('Nisatta, Nowshera')" style="padding:10px;background:#f8f9ff;border:1px solid #e0e6ff;border-radius:10px;margin:6px 0;cursor:pointer"><b>Nisatta, Nowshera</b><p style="font-size:10px;color:#666">Free delivery - 2 hours</p></div>
<div onclick="selectLocation('Peshawar City')" style="padding:10px;background:#f8f9ff;border:1px solid #e0e6ff;border-radius:10px;margin:6px 0;cursor:pointer"><b>Peshawar City</b><p style="font-size:10px;color:#666">Delivery in 3 hours - Rs.99</p></div>
<div onclick="selectLocation('Nowshera Cantt')" style="padding:10px;background:#f8f9ff;border:1px solid #e0e6ff;border-radius:10px;margin:6px 0;cursor:pointer"><b>Nowshera Cantt</b><p style="font-size:10px;color:#666">Free delivery - 2 hours</p></div>
<div onclick="selectLocation('Charsadda Road')" style="padding:10px;background:#f8f9ff;border:1px solid #e0e6ff;border-radius:10px;margin:6px 0;cursor:pointer"><b>Charsadda Road</b><p style="font-size:10px;color:#666">Delivery in 2.5 hours</p></div>
</div>
<button onclick="closeModals()" style="background:#00a8e8;color:#fff;border:none;width:100%;padding:10px;border-radius:10px;font-weight:800;margin-top:10px;cursor:pointer">Close</button>
</div>
</div>

<div class="whatsapp-float" onclick="window.open('https://wa.me/923464621962','_blank')"><i class="fab fa-whatsapp"></i></div>
<div class="up-float" onclick="scrollToTop()"><i class="fa fa-chevron-up"></i></div>

<div class="bottom-nav">
<div class="b-nav active" onclick="scrollToTop()"><i class="fa fa-home"></i>Home</div>
<div class="b-nav" onclick="scrollToCat()"><i class="fa fa-th"></i>Categories</div>
<div class="b-nav" onclick="openSearch()"><i class="fa fa-search"></i>Search</div>
<div class="b-nav" onclick="openCart()" style="position:relative"><i class="fa fa-shopping-cart"></i><span class="cart-badge" id="cartBadge">0</span>Cart</div>
<div class="b-nav" onclick="openSupport()"><i class="fa fa-headset"></i>Support</div>
</div>

<div id="overlay" class="overlay" onclick="closeCart();closeModals();closeSearch()"></div>
<div id="cartDrawer">
<div style="display:flex;justify-content:space-between;align-items:center"><h2 style="font-weight:900">YOUR CART</h2><span onclick="closeCart()" style="font-weight:900;font-size:22px;cursor:pointer;background:#f0f0f0;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center">X</span></div>
<div id="cartItems" style="flex:1;margin-top:16px;overflow-y:auto"></div>
<div style="border-top:1px solid #eee;padding-top:12px">
<div style="display:flex;justify-content:space-between;font-weight:900;font-size:18px"><span>Total</span><span>Rs. <span id="total">0</span></span></div>
<p style="font-size:11px;color:#666;margin:6px 0">Contact: +92 346 4621962 | rafiiedu589@gmail.com</p>
<button style="background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;border:none;width:100%;padding:16px;border-radius:14px;font-weight:900;cursor:pointer;box-shadow:0 6px 16px rgba(37,211,102,.3)" onclick="checkout()"><i class="fab fa-whatsapp"></i> ORDER ON WHATSAPP</button>
</div>
</div>
<div id="toast" style="position:fixed;bottom:120px;left:50%;transform:translateX(-50%) translateY(100px);background:rgba(0,0,0,.85);backdrop-filter:blur(12px);color:#fff;padding:12px 20px;border-radius:50px;font-size:13px;font-weight:600;z-index:99999;opacity:0;transition:.4s;pointer-events:none;box-shadow:0 8px 24px rgba(0,0,0,.3)">Toast</div>

<script>
const products = {
ultraFresh: [
{name:"Fresh Chicken Thigh With Bone",wt:"1Kg",price:"Rs. 580.00",priceNum:580,img:"https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=300"},
{name:"Fresh Tomato / Tamatar",wt:"1Kg",price:"Rs. 120.00",priceNum:120,img:"https://images.unsplash.com/photo-1561136594-7f68413baa99?w=300"},
{name:"Fresh Onion / Piyaz",wt:"1Kg",price:"Rs. 140.00",priceNum:140,img:"https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?w=300"},
{name:"Fresh Potato",wt:"1Kg",price:"Rs. 90.00",priceNum:90,img:"https://images.unsplash.com/photo-1518977676608-bd36c2ca4f0d?w=300"}
],
beverages: [
{name:"Aquafina",wt:"1.5Ltr",price:"Rs. 84.00",priceNum:84,img:"https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=300"},
{name:"Nestle Pure Life Water Bottle",wt:"500Ml",price:"Rs. 64.00",priceNum:64,img:"https://images.unsplash.com/photo-1523369364227-24934d3dc789?w=300"},
{name:"Mountain Dew",wt:"1.5Ltr",price:"Rs. 180.00",priceNum:180,img:"https://images.unsplash.com/photo-1553456558-aff542a7b319?w=300"},
{name:"Haleeb Fruity",wt:"1Ltr",price:"Rs. 220.00",priceNum:220,img:"https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300"}
],
health: [
{name:"Meclay London Shampoo Colour...",wt:"660Ml",price:"Rs. 1,194.00",priceNum:1194,img:"https://images.unsplash.com/photo-1526947425960-945c6aed9c3f?w=300"},
{name:"Butterfly Pads Dreamy Nights...",wt:"8Pcs",price:"Rs. 314.00",priceNum:314,img:"https://images.unsplash.com/photo-1584305574586-0a373f7b027f?w=300"},
{name:"Ponds Face Wash",wt:"100G",price:"Rs. 450.00",priceNum:450,img:"https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=300"},
{name:"Colgate Toothpaste",wt:"200G",price:"Rs. 180.00",priceNum:180,img:"https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=300"}
],
dairy: [
{name:"Egg Loose Farmi",wt:"6Pcs",price:"Rs. 122.00",priceNum:122,img:"https://images.unsplash.com/photo-1486090200949-6d9798a548cd?w=300"},
{name:"Olpers Milk",wt:"1Ltr",price:"Rs. 349.00",priceNum:349,img:"https://images.unsplash.com/photo-1550583724-b2692b85b150?w=300"},
{name:"National Mango Jam",wt:"400G",price:"Rs. 420.00",priceNum:420,img:"https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=300"},
{name:"Bread Plain",wt:"1Pc",price:"Rs. 120.00",priceNum:120,img:"https://images.unsplash.com/photo-1509440159596-0249088772ff?w=300"}
],
frozen: [
{name:"K&Ns Hot Tenders",wt:"780Gm",price:"Rs. 1,389.00",priceNum:1389,img:"https://images.unsplash.com/photo-1568909344668-6f14a07b56a0?w=300"},
{name:"K&Ns Wings",wt:"1Kg",price:"Rs. 860.00",priceNum:860,img:"https://images.unsplash.com/photo-1604908177223-81e0605f2c3a?w=300"},
{name:"K&Ns Nuggets",wt:"1Kg",price:"Rs. 990.00",priceNum:990,img:"https://images.unsplash.com/photo-1568909344668-6f14a07b56a0?w=300"},
{name:"Sufi Chicken",wt:"1Kg",price:"Rs. 850.00",priceNum:850,img:"https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=300"}
],
baby: [
{name:"Johnsons Baby Cream",wt:"100Gm",price:"Rs. 795.00",priceNum:795,img:"https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=300"},
{name:"Nexton Baby Shampoo",wt:"125Ml",price:"Rs. 460.00",priceNum:460,img:"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=300"},
{name:"Molfix Diapers",wt:"60Pcs",price:"Rs. 2450.00",priceNum:2450,img:"https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=300"},
{name:"Bona Papa Lotion",wt:"200Ml",price:"Rs. 650.00",priceNum:650,img:"https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=300"}
]
};

let cart=[], total=0, count=0, qtyMap={};
function render(id, list){
let html='';
list.forEach((p,i)=>{
let key=id+'_'+i;
let qty=qtyMap[key]||0;
let qtyHtml = qty>0 ? `<div class="qty-box"><button onclick="event.stopPropagation();changeQty('${id}',${i},-1)">−</button><span>${qty}</span><button onclick="event.stopPropagation();changeQty('${id}',${i},1)">+</button></div>` : `<button class="add-btn" onclick="event.stopPropagation();addCart('${id}',${i})">Add To Cart</button>`;
html+=`<div class="prod-card" onclick="addCart('${id}',${i})"><div class="heart ${qty>0?'active':''}" onclick="event.stopPropagation();toggleHeart(this)"><i class="${qty>0?'fas':'far'} fa-heart"></i></div><img src="${p.img}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=300'"><h3>${p.name}</h3><p class="wt">${p.wt}</p><p class="price">${p.price}</p>${qtyHtml}</div>`;
});
document.getElementById(id).innerHTML=html;
}
Object.keys(products).forEach(k=>render(k,products[k]));

function toggleHeart(el){el.classList.toggle('active');let icon=el.querySelector('i');icon.classList.toggle('far');icon.classList.toggle('fas');el.style.transform='scale(1.4)';setTimeout(()=>el.style.transform='scale(1)',200);showToast(el.classList.contains('active')?'Added to Wishlist ❤️':'Removed')}
function addCart(cat,i){
let key=cat+'_'+i;
qtyMap[key]=(qtyMap[key]||0)+1;
render(cat,products[cat]);
let p=products[cat][i];
let existing=cart.findIndex(c=>c.key===key);
if(existing>-1){cart[existing].qty++;cart[existing].total=cart[existing].qty*cart[existing].priceNum}
else{cart.push({key:key,name:p.name,wt:p.wt,price:p.price,priceNum:p.priceNum,img:p.img,qty:1,total:p.priceNum})}
recalc();showToast(p.name+' added! 🛒');
}
function changeQty(cat,i,d){
let key=cat+'_'+i;
qtyMap[key]=(qtyMap[key]||0)+d;
if(qtyMap[key]<=0){qtyMap[key]=0;let idx=cart.findIndex(c=>c.key===key);if(idx>-1)cart.splice(idx,1)}
else{let idx=cart.findIndex(c=>c.key===key);if(idx>-1){cart[idx].qty+=d;cart[idx].total=cart[idx].qty*cart[idx].priceNum}}
render(cat,products[cat]);recalc();
}
function recalc(){
total=0;let itemCount=0;
cart.forEach(c=>{total+=c.total;itemCount+=c.qty});
count=itemCount;
document.getElementById('cartBadge').innerText=count>0?count:0;
document.getElementById('total').innerText=total;
let html='';cart.forEach((it,i)=>{html+=`<div style="display:flex;gap:10px;margin:12px 0;padding:12px;background:rgba(248,249,255,.8);border-radius:14px;animation:slideUp .3s"><img src="${it.img}" style="width:54px;height:54px;border-radius:10px;object-fit:contain;background:#fff;padding:4px"><div style="flex:1"><div style="font-weight:700;font-size:12px">${it.name}</div><div style="font-size:11px;color:#666">${it.wt} - ${it.price}</div><div style="display:flex;gap:6px;margin-top:6px"><button onclick="changeQtyCart(${i},-1)" style="width:28px;height:28px;border-radius:8px;border:1px solid #ddd;background:#fff;font-weight:900;cursor:pointer">−</button><span style="font-weight:800;font-size:13px;padding:0 8px">${it.qty}</span><button onclick="changeQtyCart(${i},1)" style="width:28px;height:28px;border-radius:8px;border:none;background:#00a8e8;color:#fff;font-weight:900;cursor:pointer">+</button><span style="margin-left:8px;font-weight:800;font-size:12px">Rs.${it.total}</span></div></div><div onclick="removeCart(${i})" style="font-weight:900;color:#bbb;cursor:pointer;width:24px;height:24px;display:flex;align-items:center;justify-content:center;background:#f0f0f0;border-radius:50%">X</div></div>`});
document.getElementById('cartItems').innerHTML=html||'<p style="color:#999;text-align:center;margin-top:40px">Cart empty<br><span style="font-size:11px">Add fresh grocery now!</span></p>';
}
function changeQtyCart(idx,d){cart[idx].qty+=d;if(cart[idx].qty<=0){let key=cart[idx].key;qtyMap[key]=0;cart.splice(idx,1);Object.keys(products).forEach(k=>render(k,products[k]));}else{cart[idx].total=cart[idx].qty*cart[idx].priceNum;let key=cart[idx].key;qtyMap[key]=cart[idx].qty}recalc()}
function removeCart(idx){let key=cart[idx].key;qtyMap[key]=0;cart.splice(idx,1);Object.keys(products).forEach(k=>render(k,products[k]));recalc();showToast('Item removed')}
function openCart(){document.getElementById('cartDrawer').classList.add('active');document.getElementById('overlay').classList.add('active');recalc()}
function closeCart(){document.getElementById('cartDrawer').classList.remove('active');document.getElementById('overlay').classList.remove('active')}
function openProfile(){document.getElementById('profileModal').classList.add('active');document.getElementById('overlay').classList.add('active')}
function openDelivery(){document.getElementById('deliveryModal').classList.add('active');document.getElementById('overlay').classList.add('active')}
function closeModals(){document.querySelectorAll('.modal-overlay').forEach(m=>m.classList.remove('active'));document.getElementById('overlay').classList.remove('active')}
function openSearch(){document.getElementById('searchBox').classList.add('active');document.getElementById('searchInput').focus();document.getElementById('overlay').classList.add('active')}
function closeSearch(){document.getElementById('searchBox').classList.remove('active');document.getElementById('overlay').classList.remove('active');document.getElementById('searchResults').innerHTML='';document.getElementById('searchInput').value='';}
function scrollToTop(){window.scrollTo({top:0,behavior:'smooth'});showToast('Top ↑');updateActiveNav(0)}
function scrollToCat(){document.getElementById('shopCat').scrollIntoView({behavior:'smooth'});updateActiveNav(1);showToast('Shop by Category')}
function scrollToSec(id){document.getElementById(id).scrollIntoView({behavior:'smooth',block:'center'});showToast('Viewing '+id)}
function openSupport(){window.open('https://wa.me/923464621962?text=Salam%20Rainbow%20Mart%20Support!%20Need%20help%20-%20+92%20346%204621962','_blank');showToast('Opening WhatsApp...')}

function selectLocation(loc){
document.getElementById('deliveryText').innerText=loc;
showToast('Delivery: '+loc+' ✓');
closeModals();
}

function saveCustomLocation(){
let customLoc = document.getElementById('customAddressInput').value.trim();
if(customLoc.length > 2){
document.getElementById('deliveryText').innerText = customLoc;
showToast('Address saved: '+customLoc+' ✓');
closeModals();
}else{
showToast('Please enter a valid address!');
}
}

function submitReview(){
let name = document.getElementById('reviewName').value.trim();
let text = document.getElementById('reviewText').value.trim();
if(name.length > 1 && text.length > 3){
let container = document.getElementById('reviewsContainer');
let newCard = document.createElement('div');
newCard.className = 'testi-card';
newCard.innerHTML = `<p>"${text}"</p><div class="testi-author">- ${name}</div>`;
container.prepend(newCard);
document.getElementById('reviewName').value = '';
document.getElementById('reviewText').value = '';
showToast('Thank you for your review! ⭐');
}else{
showToast('Please fill in name and review message!');
}
}

function filterCat(cat){showToast('Category: '+cat.toUpperCase()+' clicked!');if(cat==='ultra')scrollToSec('ultraFresh');else if(cat==='bev')scrollToSec('beverages');else if(cat==='dairy')scrollToSec('dairy');else if(cat==='health')scrollToSec('health');else scrollToSec('ultraFresh')}
function updateActiveNav(idx){document.querySelectorAll('.b-nav').forEach((el,i)=>{el.classList.toggle('active',i===idx)})}
function showToast(msg){let t=document.getElementById('toast');t.innerText=msg;t.style.opacity='1';t.style.transform='translateX(-50%) translateY(0)';setTimeout(()=>{t.style.opacity='0';t.style.transform='translateX(-50%) translateY(100px)'},2500)}

function searchProd(){
let q=document.getElementById('searchInput').value.toLowerCase();
let resBox=document.getElementById('searchResults');
if(q.length<1){resBox.innerHTML='';return;}
let all=[];Object.values(products).forEach(list=>all.push(...list));
let filtered=all.filter(p=>p.name.toLowerCase().includes(q));
let html=`<p style="font-size:12px;font-weight:700;margin:8px 0">${filtered.length} results found for "${q}"</p><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">`;
filtered.forEach(p=>{
html+=`<div style="background:#fff;border-radius:12px;padding:8px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.05)"><img src="${p.img}" style="width:100%;height:70px;object-fit:contain"><p style="font-size:11px;font-weight:700;height:28px;overflow:hidden">${p.name}</p><p style="font-size:12px;font-weight:800;color:#00a8e8">${p.price}</p></div>`;
});
html+='</div>';
resBox.innerHTML=filtered.length>0?html:'<p style="text-align:center;color:#888;margin-top:20px;font-size:12px">No products found!</p>';
}

function checkout(){if(cart.length===0){showToast('Cart khali hai! Add items first 🛒');return}let loc=document.getElementById('deliveryText').innerText;let msg='Salam Rainbow Mart Nowshera!%0A%0AGrocery Order:%0A%0A';cart.forEach(it=>{msg+=`${it.name} | ${it.wt} | Qty:${it.qty} | Rs.${it.total}%0A`});msg+=`%0ATOTAL = Rs.${total}%0ADelivery Address: ${loc}%0A%0AName:%0APhone:%0A%0AContact:+92 346 4621962%0AEmail:rafiiedu589@gmail.com`;window.open('https://wa.me/923464621962?text='+msg,'_blank');showToast('Opening WhatsApp...');}

let time = 5 * 3600 + 42 * 60 + 19;
setInterval(() => {
let h = Math.floor(time / 3600), m = Math.floor((time % 3600) / 60), s = time % 60;
document.getElementById('countdown').innerText = `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
if(time > 0) time--;
}, 1000);

document.querySelectorAll('.b-nav').forEach((el,i)=>{el.addEventListener('click',()=>updateActiveNav(i))});
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    print("="*60)
    print(" Rainbow Mart - WITH CUSTOMER REVIEWS FORM!")
    print(" Contact: +92 346 4621962 | rafiiedu589@gmail.com")
    print(" Open: http://127.0.0.1:5000")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=True)
