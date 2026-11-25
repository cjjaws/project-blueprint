from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/safety")
def safety():
    return render_template("safety.html")

mentors = [
    {
        "id": 1,
        "name": "Marcus Reed",
        "title": "Senior Software Engineer",
        "company": "Google",
        "bio": "Morehouse grad. Builds search infrastructure.",
        "field": "Software",
        "tags": ["Internships", "Coding interviews", "College CS"],
    },
    {
        "id": 2,
        "name": "Sarah Johnson",
        "title": "Product Manager",
        "company": "Microsoft",
        "bio": "Ex-Amazon product manager. Passionate about user experience.",
        "field": "Product",
        "tags": ["Product strategy", "User research", "Leadership"],
    },
    {
        "id": 3,
        "name": "David Kim",
        "title": "Data Scientist",
        "company": "Meta",
        "bio": "Stanford graduate. Specializes in machine learning and data analysis.",
        "field": "Data Science",
        "tags": ["Machine learning", "Statistics", "Python"],
    },
    {
        "id": 4,
        "name": "Emily Chen",
        "title": "UX Designer",
        "company": "Apple",
        "bio": "Carnegie Mellon graduate. Focuses on creating intuitive user experiences.",
        "field": "Design",
        "tags": ["User experience", "Prototyping", "Visual design"],
    },
    {
        "id": 5,
        "name": "James Wilson",
        "title": "DevOps Engineer",
        "company": "Amazon",
        "bio": "University of Washington graduate. Expert in cloud infrastructure and automation.",
        "field": "DevOps",
        "tags": ["Cloud computing", "CI/CD", "Linux"],
    },
    {
        "id": 6,
        "name": "Lisa Rodriguez",
        "title": "Sales Director",
        "company": "Salesforce",
        "bio": "Harvard MBA. Drives sales growth and customer satisfaction.",
        "field": "Sales",
        "tags": ["Sales strategy", "Negotiation", "Leadership"],
    }
]

@app.route("/mentors")
def mentor_list():
    return render_template("mentors.html", mentors=mentors)