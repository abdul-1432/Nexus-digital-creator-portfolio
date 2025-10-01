# Create the HTML file for the hackathon website
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS - Digital Creative Studio</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@200;300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <span class="logo-text">NEXUS</span>
                <div class="logo-dot"></div>
            </div>
            <ul class="nav-menu">
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-bg"></div>
        <div class="hero-container">
            <div class="hero-content">
                <div class="hero-badge">
                    <span class="badge-text">✨ Available for Projects</span>
                </div>
                <h1 class="hero-title">
                    <span class="title-line">Crafting Digital</span>
                    <span class="title-line gradient-text">Experiences</span>
                    <span class="title-line">That Inspire</span>
                </h1>
                <p class="hero-description">
                    Pushing the boundaries of creative technology through innovative design, 
                    immersive interfaces, and cutting-edge digital solutions that captivate and convert.
                </p>
                <div class="hero-cta">
                    <button class="btn-primary">
                        <span>Explore Work</span>
                        <div class="btn-bg"></div>
                    </button>
                    <button class="btn-secondary">
                        <span>Get in Touch</span>
                    </button>
                </div>
            </div>
            <div class="hero-visual">
                <div class="floating-card card-1">
                    <div class="card-content">UI/UX</div>
                </div>
                <div class="floating-card card-2">
                    <div class="card-content">Brand</div>
                </div>
                <div class="floating-card card-3">
                    <div class="card-content">Motion</div>
                </div>
                <div class="floating-shapes">
                    <div class="shape shape-1"></div>
                    <div class="shape shape-2"></div>
                    <div class="shape shape-3"></div>
                </div>
            </div>
        </div>
        <div class="scroll-indicator">
            <div class="scroll-mouse">
                <div class="scroll-wheel"></div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="section-header">
                <span class="section-number">01</span>
                <h2 class="section-title">About NEXUS</h2>
            </div>
            <div class="about-content">
                <div class="about-text">
                    <h3 class="about-headline">Where creativity meets innovation</h3>
                    <p class="about-paragraph">
                        NEXUS represents the intersection of bold creativity and cutting-edge technology. 
                        We specialize in crafting digital experiences that not only look extraordinary 
                        but perform flawlessly across all platforms.
                    </p>
                    <p class="about-paragraph">
                        Our approach combines strategic thinking with experimental design, resulting in 
                        solutions that push boundaries while delivering measurable business impact.
                    </p>
                    <div class="skills-grid">
                        <div class="skill-item">
                            <span class="skill-name">Visual Design</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="--width: 95%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">User Experience</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="--width: 90%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Motion Graphics</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="--width: 88%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Brand Strategy</span>
                            <div class="skill-bar">
                                <div class="skill-fill" style="--width: 85%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="about-visual">
                    <div class="profile-card">
                        <div class="profile-image"></div>
                        <div class="profile-info">
                            <h4>Creative Director</h4>
                            <p>Specialized in Digital Innovation</p>
                        </div>
                        <div class="profile-stats">
                            <div class="stat">
                                <span class="stat-number">5+</span>
                                <span class="stat-label">Years</span>
                            </div>
                            <div class="stat">
                                <span class="stat-number">100+</span>
                                <span class="stat-label">Projects</span>
                            </div>
                            <div class="stat">
                                <span class="stat-number">50+</span>
                                <span class="stat-label">Clients</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <div class="section-header">
                <span class="section-number">02</span>
                <h2 class="section-title">Featured Projects</h2>
                <p class="section-subtitle">Explore our latest work and creative solutions</p>
            </div>
            <div class="projects-grid">
                <article class="project-card featured">
                    <div class="project-image">
                        <div class="project-overlay">
                            <div class="project-tech">
                                <span class="tech-tag">UI/UX</span>
                                <span class="tech-tag">Branding</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3 class="project-title">NeuroFlow App</h3>
                        <p class="project-description">
                            Revolutionary mental health platform combining AI-driven insights 
                            with intuitive design for personalized wellness journeys.
                        </p>
                        <div class="project-meta">
                            <span class="project-year">2024</span>
                            <div class="project-arrow">→</div>
                        </div>
                    </div>
                </article>
                
                <article class="project-card">
                    <div class="project-image">
                        <div class="project-overlay">
                            <div class="project-tech">
                                <span class="tech-tag">Web Design</span>
                                <span class="tech-tag">Motion</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3 class="project-title">EcoVision Dashboard</h3>
                        <p class="project-description">
                            Sustainable energy monitoring platform with real-time data 
                            visualization and predictive analytics.
                        </p>
                        <div class="project-meta">
                            <span class="project-year">2024</span>
                            <div class="project-arrow">→</div>
                        </div>
                    </div>
                </article>
                
                <article class="project-card">
                    <div class="project-image">
                        <div class="project-overlay">
                            <div class="project-tech">
                                <span class="tech-tag">Branding</span>
                                <span class="tech-tag">3D</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3 class="project-title">Quantum Labs</h3>
                        <p class="project-description">
                            Complete brand identity and digital experience for a cutting-edge 
                            research facility focused on quantum computing.
                        </p>
                        <div class="project-meta">
                            <span class="project-year">2023</span>
                            <div class="project-arrow">→</div>
                        </div>
                    </div>
                </article>
                
                <article class="project-card">
                    <div class="project-image">
                        <div class="project-overlay">
                            <div class="project-tech">
                                <span class="tech-tag">Mobile</span>
                                <span class="tech-tag">AR/VR</span>
                            </div>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3 class="project-title">ArtSpace VR</h3>
                        <p class="project-description">
                            Immersive virtual gallery experience allowing artists to showcase 
                            and sell their work in interactive 3D environments.
                        </p>
                        <div class="project-meta">
                            <span class="project-year">2023</span>
                            <div class="project-arrow">→</div>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services">
        <div class="container">
            <div class="section-header">
                <span class="section-number">03</span>
                <h2 class="section-title">Services</h2>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">
                        <div class="icon-shape icon-1"></div>
                    </div>
                    <h3 class="service-title">Digital Strategy</h3>
                    <p class="service-description">
                        Comprehensive digital transformation strategies that align with your business objectives and drive growth.
                    </p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <div class="icon-shape icon-2"></div>
                    </div>
                    <h3 class="service-title">UI/UX Design</h3>
                    <p class="service-description">
                        User-centered design solutions that prioritize usability while delivering visually stunning interfaces.
                    </p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <div class="icon-shape icon-3"></div>
                    </div>
                    <h3 class="service-title">Brand Identity</h3>
                    <p class="service-description">
                        Complete brand ecosystems from logo design to comprehensive style guides and brand guidelines.
                    </p>
                </div>
                <div class="service-card">
                    <div class="service-icon">
                        <div class="icon-shape icon-4"></div>
                    </div>
                    <h3 class="service-title">Motion Design</h3>
                    <p class="service-description">
                        Dynamic animations and motion graphics that bring your digital experiences to life.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-info">
                    <div class="section-header">
                        <span class="section-number">04</span>
                        <h2 class="section-title">Let's Create Something Amazing</h2>
                    </div>
                    <p class="contact-description">
                        Ready to transform your vision into reality? Let's collaborate on your next 
                        digital project and create experiences that captivate your audience.
                    </p>
                    <div class="contact-details">
                        <div class="contact-item">
                            <span class="contact-label">Email</span>
                            <span class="contact-value">hello@nexusstudio.com</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-label">Phone</span>
                            <span class="contact-value">+1 (555) 123-4567</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-label">Location</span>
                            <span class="contact-value">San Francisco, CA</span>
                        </div>
                    </div>
                    <div class="social-links">
                        <a href="#" class="social-link">Dribbble</a>
                        <a href="#" class="social-link">Behance</a>
                        <a href="#" class="social-link">Instagram</a>
                        <a href="#" class="social-link">LinkedIn</a>
                    </div>
                </div>
                <div class="contact-form-wrapper">
                    <form class="contact-form">
                        <div class="form-group">
                            <input type="text" placeholder="Your Name" class="form-input" required>
                        </div>
                        <div class="form-group">
                            <input type="email" placeholder="Your Email" class="form-input" required>
                        </div>
                        <div class="form-group">
                            <input type="text" placeholder="Project Type" class="form-input">
                        </div>
                        <div class="form-group">
                            <textarea placeholder="Tell us about your project" class="form-textarea" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn-primary form-submit">
                            <span>Send Message</span>
                            <div class="btn-bg"></div>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">
                    <span class="logo-text">NEXUS</span>
                    <div class="logo-dot"></div>
                </div>
                <p class="footer-text">© 2024 NEXUS Studio. Crafting digital experiences that inspire.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''

# Save HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file created successfully: index.html")