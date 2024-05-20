from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objs as go
import json
import plotly

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

# Lithium App
@app.route('/lithium-investment')
def lithium_investment_home():
    return render_template('home_lithium.html')

@app.route('/lithium-markets', methods=['GET', 'POST'])
def lithium_markets():
    return render_template('lithium_markets.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/lithium-gpt')
def lithium_gpt():
    return render_template('lithium_gpt.html')

# Sentiment App
@app.route('/sentiment-analysis')
def sentiment_analysis_home():
    return render_template('home_sentiment.html')

@app.route('/news-feed')
def news_feed():
    return render_template('news-feed.html')

@app.route('/sentiment-analysis')
def sentiment_analysis():
    return render_template('sentiment-analysis.html')

@app.route('/zerofox')
def zerofox():
    return render_template('zerofox.html')

@app.route('/brand24')
def brand24():
    return render_template('brand24.html')

@app.route('/sentiment-gpt')
def sentiment_gpt():
    return render_template('sentiment-gpt.html')

@app.route('/report-generator')
def report_generator():
    return render_template('report-generator.html')

# LLM APP
@app.route('/hancock-gpt')
def hancock_gpt():
    return render_template('HancockGPT.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7861)
