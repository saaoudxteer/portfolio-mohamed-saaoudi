/* ===================================================================
   Mohamed Saaoudi Portfolio — Premium JS
   Features: custom cursor, scroll progress, scroll reveal, stagger
   =================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // ─── SCROLL PROGRESS BAR ────────────────────────────────────────
    const progressBar = document.getElementById('scrollProgress');
    if (progressBar) {
        const updateProgress = () => {
            const scrolled = window.scrollY;
            const total = document.documentElement.scrollHeight - window.innerHeight;
            if (total > 0) {
                progressBar.style.width = `${(scrolled / total) * 100}%`;
            }
        };
        window.addEventListener('scroll', updateProgress, { passive: true });
        updateProgress();
    }

    // ─── NAV — add scrolled class ────────────────────────────────────
    const navbar = document.getElementById('navbar');
    if (navbar) {
        const updateNav = () => {
            navbar.classList.toggle('scrolled', window.scrollY > 30);
        };
        window.addEventListener('scroll', updateNav, { passive: true });
        updateNav();
    }

    // ─── SCROLL REVEAL ───────────────────────────────────────────────
    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.08, rootMargin: '0px 0px -32px 0px' }
    );
    document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

    // ─── STAGGER PILLARS ─────────────────────────────────────────────
    document.querySelectorAll('.pillars-band .pillar').forEach((el, i) => {
        el.style.transitionDelay = `${i * 0.11}s`;
    });
    document.querySelectorAll('.skills-grid .skill-group').forEach((el, i) => {
        el.style.transitionDelay = `${i * 0.07}s`;
    });

    // ─── CUSTOM CURSOR (desktop / hover-capable devices only) ────────
    const cursorDot  = document.getElementById('cursorDot');
    const cursorRing = document.getElementById('cursorRing');
    const hasHover   = window.matchMedia('(hover: hover)').matches;

    if (cursorDot && cursorRing && hasHover) {
        document.body.classList.add('cursor-active');

        let mx = window.innerWidth / 2;
        let my = window.innerHeight / 2;
        let rx = mx, ry = my;
        let rafId;

        // Immediate dot follows mouse exactly
        document.addEventListener('mousemove', (e) => {
            mx = e.clientX;
            my = e.clientY;
            cursorDot.style.left = mx + 'px';
            cursorDot.style.top  = my + 'px';
        });

        // Ring follows with lerp (smooth lag)
        const lerp = (a, b, t) => a + (b - a) * t;
        const animateRing = () => {
            rx = lerp(rx, mx, 0.11);
            ry = lerp(ry, my, 0.11);
            cursorRing.style.left = rx + 'px';
            cursorRing.style.top  = ry + 'px';
            rafId = requestAnimationFrame(animateRing);
        };
        animateRing();

        // Expand ring on interactive elements
        const interactiveSelector = 'a, button, .card, .pillar, .tag, .about-content p, .signals-list li';
        document.querySelectorAll(interactiveSelector).forEach((el) => {
            el.addEventListener('mouseenter', () => cursorRing.classList.add('expand'));
            el.addEventListener('mouseleave', () => cursorRing.classList.remove('expand'));
        });

        // Hide cursor when leaving window
        document.addEventListener('mouseleave', () => {
            cursorDot.style.opacity  = '0';
            cursorRing.style.opacity = '0';
        });
        document.addEventListener('mouseenter', () => {
            cursorDot.style.opacity  = '1';
            cursorRing.style.opacity = '1';
        });
    }

    // ─── SMOOTH ANCHOR SCROLL (offset for sticky nav) ────────────────
    document.querySelectorAll('a[href^="#"]').forEach((link) => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href').slice(1);
            const target   = document.getElementById(targetId);
            if (target) {
                e.preventDefault();
                const offset = 88;
                const top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    // ─── TAG HOVER EFFECT (subtle ripple) ────────────────────────────
    // Micro-interaction: tags get a subtle scale + amber glow on hover
    // This is handled via CSS, but we add a class-based toggle for richer control
    document.querySelectorAll('.tag').forEach((tag) => {
        tag.addEventListener('mouseenter', () => {
            tag.style.transform = 'translateY(-1px)';
        });
        tag.addEventListener('mouseleave', () => {
            tag.style.transform = '';
        });
    });

    // ─── ACTIVE NAV LINK HIGHLIGHT based on scroll position ──────────
    const sections  = document.querySelectorAll('section[id]');
    const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

    if (sections.length && navAnchors.length) {
        const activateLink = () => {
            let current = '';
            sections.forEach((section) => {
                const sectionTop = section.getBoundingClientRect().top;
                if (sectionTop < 140) current = section.id;
            });
            navAnchors.forEach((a) => {
                const isActive = a.getAttribute('href') === `#${current}`;
                a.style.color = isActive ? 'var(--text)' : '';
                a.style.background = isActive ? 'rgba(255,255,255,0.05)' : '';
            });
        };
        window.addEventListener('scroll', activateLink, { passive: true });
        activateLink();
    }

});
