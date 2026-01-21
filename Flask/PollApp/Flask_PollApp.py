from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Poll Data (in-memory storage) ---
poll_question = "What is your favorite color?"
poll_options = {
    "Red": 0,
    "Blue": 0,
    "Green": 0,
    "Yellow": 0
}

@app.route('/')
def index():
    return render_template('poll.html', question=poll_question, options=poll_options)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form.get('option')
    if selected_option in poll_options:
        poll_options[selected_option] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    total_votes = sum(poll_options.values())
    
    # Calculate percentages for bar chart
    results_with_percentage = []
    for option, votes in poll_options.items():
        percentage = (votes / total_votes * 100) if total_votes > 0 else 0
        results_with_percentage.append({
            'option': option,
            'votes': votes,
            'percentage': round(percentage, 1)
        })
    
    return render_template('results.html', 
                           question=poll_question, 
                           results=results_with_percentage,
                           total_votes=total_votes)

if __name__ == '__main__':
    app.run(debug=True)