from django.shortcuts import render


def home(request):
    profile = {
        "name": "Mohamed Saaoudi",
        "headline": "Data Science & Engineering Student · Applied AI · Software & Data Systems",
        "tagline": "A rigorous technical profile building concrete systems at the intersection of data, software, and intelligent engineering.",
        "summary": "Master's student in Data Science & Engineering at Aix-Marseille Université with a dual foundation in mathematics and computer science. I am particularly drawn to data systems, machine learning, backend architecture, and technically demanding environments where precision, structure, and intellectual discipline matter.",
        "location": "Marseille, France",
        "email": "saaoudimohamed71@gmail.com",
        "phone": "+33 7 44 21 44 73",
        "github": "https://github.com/saaoudxteer",
        "linkedin": "https://www.linkedin.com/in/mohamed-saaoudi-b79624248",
        "leetcode": "https://leetcode.com/u/Mrsaaoudi/",
        "cv_url": "/static/showcase/assets/Mohamed_Saaoudi_CV_General_ATS.pdf",
        "cv_label": "Download CV",
    }

    quick_facts = [
        {"label": "Current program", "value": "M.Sc. Data Science & Engineering · AMU"},
        {"label": "Academic base", "value": "B.Sc. Mathematics & Computer Science"},
        {"label": "Internship availability", "value": "From May 2026 · 3 to 6 months"},
        {"label": "Working languages", "value": "French, English, Arabic, Amazigh"},
    ]

    signature_points = [
        {
            "index": "01",
            "title": "Rigor-first mindset",
            "text": "I work best when the objective is clear, the constraints are explicit, and the result can be trusted, explained, and reused.",
        },
        {
            "index": "02",
            "title": "Math × code profile",
            "text": "My background gives me both analytical depth and implementation discipline, which is what I try to reflect in every project.",
        },
        {
            "index": "03",
            "title": "Engineering ambition",
            "text": "I am not interested in superficial output. I care about systems, maintainability, evaluation quality, and long-term technical growth.",
        },
    ]

    about_points = [
        "I work with a structured, engineering-first mindset: define the objective, frame the constraints, build clean pipelines, evaluate rigorously, and document clearly.",
        "My profile is shaped by both mathematics and computer science, which gives me a strong base for analytical reasoning, algorithms, statistics, and system design.",
        "I am especially drawn to domains where technical precision matters: data engineering, machine learning, intelligent systems, backend architecture, networks, and high-stakes decision support.",
        "What differentiates me most is not just curiosity, but discipline: I care about reproducibility, maintainability, clear reasoning, and work that can actually be trusted and reused.",
    ]

    education = [
        {
            "period": "2025 — 2027",
            "title": "M.Sc. in Data Science & Engineering (Year 1)",
            "institution": "Aix-Marseille University · Marseille, France",
            "details": "Core focus on data processing, databases, software engineering, machine learning, and system design. Built on a quantitative track combining probability, statistics, linear algebra, and algorithmics.",
        },
        {
            "period": "2022 — 2025",
            "title": "B.Sc. in Mathematics & Computer Science",
            "institution": "Aix-Marseille University · Marseille, France",
            "details": "Developed solid foundations in algorithms, databases, probability and statistics, operating systems, networking, logic, and computability theory.",
        },
        {
            "period": "2021 — 2022",
            "title": "Baccalaureate equivalent — Mathematics, Physics & Chemistry",
            "institution": "Morocco · Mention Très Bien",
            "details": "A strong scientific base that shaped a rigorous, quantitative academic trajectory.",
        },
    ]

    skill_groups = [
        {
            "title": "Programming & Software",
            "items": ["Python", "SQL", "Java", "Data Structures", "Algorithms", "Clean Code", "REST APIs", "Django"],
        },
        {
            "title": "Data Science & ML",
            "items": ["Machine Learning", "Model Evaluation", "Feature Engineering", "Optimization", "Statistics", "Reproducible Workflows"],
        },
        {
            "title": "Data Engineering & Databases",
            "items": ["ETL Pipelines", "Data Modeling", "MongoDB", "SQL Databases", "Structured Data Flows"],
        },
        {
            "title": "Frameworks & Libraries",
            "items": ["scikit-learn", "XGBoost", "TensorFlow", "Keras", "PyTorch", "Pandas", "Matplotlib", "Seaborn"],
        },
        {
            "title": "Systems, Tooling & Environment",
            "items": ["Git", "Linux", "Docker (basics)", "Jupyter", "Technical Documentation"],
        },
    ]

    projects = [
        {
            "name": "Bank Marketing Prediction",
            "context": "End-to-end machine learning case built on banking marketing data.",
            "objective": "Design a reliable, reproducible prediction workflow capable of turning raw data into a documented evaluation pipeline.",
            "stack": ["Python", "pandas", "scikit-learn", "XGBoost", "Jupyter"],
            "method": "Data cleaning, encoding, feature engineering, stratified evaluation logic, and multi-model comparison with explicit metrics and trade-off analysis.",
            "role": "Designed the workflow, implemented preprocessing and evaluation, structured the notebook, and documented conclusions.",
            "impact": "Demonstrates rigor in experimentation, analytical clarity, and the ability to build reproducible ML pipelines rather than isolated notebooks.",
            "signal": "Shows engineering discipline, evaluation quality, and data reasoning.",
            "github": "https://github.com/saaoudxteer/bank-marketing-project",
        },
        {
            "name": "SmartFire AI",
            "context": "Applied AI project focused on fire risk detection and backend structuring.",
            "objective": "Create a multi-signal risk scoring engine with a maintainable backend architecture and testable prediction logic.",
            "stack": ["Python", "Django", "TensorFlow", "Keras", "PyTorch", "REST API"],
            "method": "Modular architecture, explicit interfaces, iterative delivery, structured data flows, and systematic error analysis around the scoring logic.",
            "role": "Worked on scoring logic, backend structure, and integration of AI components into a usable software architecture.",
            "impact": "Highlights the ability to combine machine learning with software engineering constraints instead of treating them as separate worlds.",
            "signal": "Shows versatility, backend thinking, autonomy, and applied AI execution.",
            "github": "https://github.com/saaoudxteer/FireDetection",
        },
        {
            "name": "Urban Growth Simulation",
            "context": "Quantitative modeling and validation design project.",
            "objective": "Frame a robust modeling problem with clear metrics, scenarios, constraints, and validation logic before implementation ambiguity appears.",
            "stack": ["Quantitative modeling", "Validation design", "Scenario analysis"],
            "method": "Defined objectives, constraints, success criteria, potential data sources, formats, and a temporal cross-validation strategy.",
            "role": "Structured the analytical framing, validation logic, and roadmap for iterative development.",
            "impact": "Shows that I can think upstream: not just code, but define a sound methodology, reduce ambiguity, and make technical work easier to trust.",
            "signal": "Shows analytical maturity, modeling discipline, and systems thinking.",
            "github": "",
        },
    ]

    experiences = [
        {
            "period": "May 2025 — Jul 2025",
            "title": "Data Analyst Intern",
            "org": "BMCI Banque (BNP Paribas Group) · Casablanca, Morocco",
            "points": [
                "Worked on extraction, cleaning, and structuring of heterogeneous banking data for reporting and internal analysis.",
                "Contributed to Python-based ETL automation and data preparation workflows for recurring reporting needs.",
                "Supported KPI tracking, dashboard-oriented outputs, and data quality controls in a finance and risk context.",
                "Gained experience in disciplined delivery, documentation, and work quality expectations in a professional environment.",
            ],
        },
        {
            "period": "2024",
            "title": "Volunteer",
            "org": "COP Climate Event · Marseille, France",
            "points": [
                "Supported logistics coordination and participant assistance in a high-activity event environment.",
                "Reinforced reliability, responsiveness, and operational discipline under real constraints.",
            ],
        },
        {
            "period": "Part-time experience",
            "title": "Team Member",
            "org": "Steak 'n Shake",
            "points": [
                "Developed time management, teamwork under pressure, consistency, and operational seriousness.",
            ],
        },
    ]

    certifications = [
        "IBM Data Science Professional Certificate",
        "Python for Data Science · Kaggle",
        "Networking Fundamentals · Cisco",
    ]

    vision = [
        "Data engineering and large-scale systems",
        "Applied artificial intelligence for real-world decision problems",
        "Optimization, forecasting, and risk-oriented analytics",
        "Software systems that combine reliability, clarity, and measurable value",
        "Networks and cybersecurity as complementary engineering interests",
    ]

    return render(
        request,
        "showcase/home.html",
        {
            "profile": profile,
            "quick_facts": quick_facts,
            "signature_points": signature_points,
            "about_points": about_points,
            "education": education,
            "skill_groups": skill_groups,
            "projects": projects,
            "experiences": experiences,
            "certifications": certifications,
            "vision": vision,
        },
    )
