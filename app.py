

from flask import Flask, render_template, request

app = Flask(__name__)

# render the home page
@app.route('/')
def index():
    return render_template('index.html')

# handle form submission
@app.route('/process', methods=['POST'])
def process():
    parent1 = request.form.get('parent1')  # Example: "Aa"
    parent2 = request.form.get('parent2')  # Example: "Aa"

    # Validate input length
    if len(parent1) != len(parent2) or len(parent1) not in [2, 4]:
        return "Invalid input. Enter monohybrid (2 characters) or dihybrid (4 characters) crosses."

    # Punnett Square
    punnett_square = []
    for p1 in parent1:
        row = []
        for p2 in parent2:
            row.append("".join(sorted(p1 + p2)))  # Combine alleles and sort for consistency
        punnett_square.append(row)

    # Count occurrences of each genotype
    counts = {}
    for row in punnett_square:
        for genotype in row:
            counts[genotype] = counts.get(genotype, 0) + 1

    # Calculate percentages
    total = sum(counts.values())
    percentages = {k: (v / total) * 100 for k, v in counts.items()}

    return render_template(
        'result.html', punnett_square=punnett_square, percentages=percentages
    )

if __name__ == '__main__':
    app.run(debug=True)

